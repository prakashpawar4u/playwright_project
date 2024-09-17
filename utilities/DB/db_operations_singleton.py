import psycopg2
import random
import time


class TLManager:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(TLManager, cls).__new__(cls)
            cls.instance._initialize()
        return cls.instance

    def _initialize(self):
        # Database connection details
        self.db_host = "192.168.56.114"
        self.db_name = "mytest"
        self.db_user = "postgres"
        self.db_password = "postgres"

    def _get_connection(self):
        return psycopg2.connect(
            host=self.db_host,
            database=self.db_name,
            user=self.db_user,
            password=self.db_password,
        )

    def _get_all_tl_names(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT tl_name FROM tl_details;")
        tl_names = cursor.fetchall()
        conn.close()
        return tl_names

    def _update_tl_status(self, tl_name, status):
        conn = self._get_connection()
        cursor = conn.cursor()
        update_query = f"""
        UPDATE tl_details
        SET tl_status = '{status}'
        WHERE tl_name = '{tl_name}';
        """
        cursor.execute(update_query)
        conn.commit()
        conn.close()

    def _get_tl_status(self, action):
        conn = self._get_connection()
        cursor = conn.cursor()
        get_query = "select * from tl_details"
        cursor.execute(get_query)
        tl_status = cursor.fetchall()
        print("#~" * 80)
        print(f"TL Status {action} updating:: \n {tl_status}")
        conn.close()

    def change_tl_status(self):
        while True:
            tl_names = self._get_all_tl_names()
            for tl_name in tl_names:
                tl_name = tl_name[0]
                lock_duration = random.uniform(3, 7)
                self._get_tl_status("Before")
                print("Proceeding with update TL status")
                self._update_tl_status(tl_name, "locked")
                print(
                    f"{tl_name} status changed to 'locked' for {lock_duration:.2f} seconds"
                )
                self._get_tl_status("After")
                time.sleep(lock_duration)
                self._update_tl_status(tl_name, "unlocked")
                print(f"{tl_name} status changed back to 'unlocked'")
                time.sleep(1)  # Sleep for 1 second between TLs


if __name__ == "__main__":
    tl_manager = TLManager()
    tl_manager.change_tl_status()
