import psycopg2
import random
import time


jobs = {
    111: {
        "Feature1": [
            {"TC1": {"Topology": {"CU": 2, "DU": 2, "RU": 3}, "priority": 0}},
            {"TC2": {"Topology": {"CU": 1, "DU": 1, "RU": 1}, "priority": 0}},
            {"TC3": {"Topology": {"CU": 1, "DU": 1, "RU": 1}, "priority": 1}},
            {"TC4": {"Topology": {"CU": 1, "DU": 1, "RU": 1}, "priority": 2}},
            {"TC5": {"Topology": {"CU": 1, "DU": 1, "RU": 2}, "priority": 2}},
            {"TC6": {"Topology": {"CU": 2, "DU": 2, "RU": 2}, "priority": 1}},
            {"TC7": {"Topology": {"CU": 1, "DU": 1, "RU": 2}, "priority": 3}},
        ]
    },
    222: {
        "Feature2": [
            {"TC1": {"Topology": {"CU": 1, "DU": 1, "RU": 1}, "priority": 0}},
            {"TC2": {"Topology": {"CU": 1, "DU": 1, "RU": 1}, "priority": 1}},
            {"TC3": {"Topology": {"CU": 1, "DU": 1, "RU": 1}, "priority": 1}},
            {"TC4": {"Topology": {"CU": 1, "DU": 1, "RU": 1}, "priority": 2}},
            {"TC5": {"Topology": {"CU": 1, "DU": 1, "RU": 2}, "priority": 2}},
            {"TC6": {"Topology": {"CU": 2, "DU": 2, "RU": 2}, "priority": 4}},
            {"TC7": {"Topology": {"CU": 1, "DU": 1, "RU": 2}, "priority": 5}},
        ]
    },
}


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

    def _get_tl_status(self, action):
        conn = self._get_connection()
        cursor = conn.cursor()
        get_query = "select * from tl_details"
        cursor.execute(get_query)
        tl_status = cursor.fetchall()
        print("#~" * 80)
        print(f"TL status {action} updating:: \n {tl_status}")
        conn.close()

    def _lock_tl(self, tl_name, status):
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

    def _unlock_tl(self, tl_name, status):
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

    def _update_tl_status(self, tl_name):
        self._get_tl_status("Before")
        self._lock_tl(tl_name, "locked")
        # lock_duration = random.uniform(10, 15)
        # tl unlock logic with thread should come here

    def _get_unlocked_tl_(self):
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            try:
                # Execute SQL query to fetch unlocked TL data
                cursor.execute(
                    "SELECT tl_name, topology FROM tl_details WHERE tl_status = 'unlocked'"
                )
                unlocked_tl_data = cursor.fetchall()
                return unlocked_tl_data
            except Exception as e:
                print(f"Error fetching TL data: {e}")
        except Exception as e:
            print(f"Error connecting to the database: {e}")
        finally:
            cursor.close()
            conn.close()

    def tc_scheduler(self, tc_name, tc_topology):
        tl_data = self._get_all_tl_names()

        for tl_name, tl_topology, tl_status in tl_data:
            time.sleep(3)
            # import pdb
            # pdb.set_trace()
            if tl_topology == tc_topology and tl_status == "unlocked":
                # Schedule test case on matching topology
                print("Matching Topology:: ")
                self._get_tl_status("Before updating")
                print(f"Scheduled {tc_name} on {tl_name} (matching topology)")
                self._update_tl_status(tl_name, "locked")
                self._get_tl_status(f"{tl_name } LOCKED CHECK")
                return tl_name

            elif (
                all(tl_topology[key] >= tc_topology[key] for key in tc_topology)
                and tl_status == "unlocked"
            ):
                # Schedule test case on higher configuration
                self._get_tl_status("Before updating")
                print(f"Scheduled {tc_name} on {tl_name} (HIGHER CONFIGURATION)")
                self._update_tl_status(tl_name, "locked")
                self._get_tl_status(f"{tl_name } LOCKED CHECK")
                return tl_name

        # No suitable TL found
        print(f"No available TL for {tc_name} with topology {tc_topology}")
        return None

    def extract_tc_by_priority(self, job_id):
        # Initialize an empty dictionary to store TCs
        tc_by_priority = {}

        # Iterate over the job_id dictionary
        for feature, tc_list in jobs[job_id].items():
            for tc in tc_list:
                for tc_name, tc_info in tc.items():
                    priority = tc_info["priority"]
                    if priority not in tc_by_priority:
                        tc_by_priority[priority] = []
                    tc_by_priority[priority].append(
                        {tc_name: {"Feature": feature, **tc_info}}
                    )

        return tc_by_priority

    def schedule_test_cases(self, jobs, unlocked_tls):
        # Sort unlocked TLs by topology (higher topology first)
        unlocked_tls.sort(key=lambda x: x[1]["RU"], reverse=True)
        # Initialize a dictionary to store scheduled test cases
        scheduled_test_cases = {}

        for job_id, features in jobs.items():
            for feature, test_cases in features.items():
                for test_case in test_cases:
                    tc_name, tc_info = test_case.popitem()
                    tc_topology = tc_info["Topology"]
                    tc_priority = tc_info["priority"]

                    # Find an unlocked TL with the same topology or higher
                    for tl_name, tl_topology in unlocked_tls:
                        if tl_topology == tc_topology:
                            print("Scheduling on Matching Topology")
                            if tl_name not in scheduled_test_cases:
                                scheduled_test_cases[tl_name] = []
                            scheduled_test_cases[tl_name].append((tc_name, tc_priority))
                            break
                        elif tl_topology["RU"] > tc_topology["RU"]:
                            # Schedule on the next available TL with higher topology
                            print("Scheduling on higher configurations")
                            if tl_name not in scheduled_test_cases:
                                scheduled_test_cases[tl_name] = []
                            scheduled_test_cases[tl_name].append((tc_name, tc_priority))
                            break

        return scheduled_test_cases

    def _get_matching_topology(self, tl):
        tl_name, target_topology = tl[0], tl[1]
        self.tc_by_priority = tl_manager.extract_tc_by_priority(111)
        closest_match = None
        closest_priority = float("inf")
        # Initialize a dictionary to store scheduled test cases
        scheduled_test_cases = {}

        for priority, test_cases in sorted(self.tc_by_priority.items()):
            for test_case in test_cases:
                for tc_id, details in test_case.items():
                    if details["Topology"] == target_topology:
                        print(
                            f"Exact Match is found for {tc_id} having {details['priority']} scheduling on {tl_name}"
                        )
                        self._update_tl_status(tl_name)
                        tc_name, tc_info = test_case.popitem()
                        tc_topology = tc_info["Topology"]
                        tc_priority = tc_info["priority"]
                        print("Scheduling on Matching Topology")
                        if tl_name not in scheduled_test_cases:
                            scheduled_test_cases[tl_name] = []
                        scheduled_test_cases[tl_name].append((tc_name, tc_priority))

                        return f"Found exact match: {tc_id} with priority {priority}, Details: {details}"

                    elif (
                        details["Topology"]["RU"] <= target_topology["RU"]
                        and details["Topology"]["DU"] <= target_topology["DU"]
                        and details["Topology"]["CU"] <= target_topology["CU"]
                    ):
                        if priority < closest_priority:
                            closest_match = (tc_id, priority, details)
                            closest_priority = priority
                            print("Scheduling on higher configurations")
                            if tl_name not in scheduled_test_cases:
                                scheduled_test_cases[tl_name] = []
                            scheduled_test_cases[tl_name].append((tc_name, tc_priority))

        if closest_match:
            return f"Found lower topology match: {closest_match[0]} with priority {closest_match[1]}, Details: {closest_match[2]}"
        else:
            return "No match found"


if __name__ == "__main__":
    # def extract_tc_by_priority(job_id):
    #     # Initialize an empty dictionary to store TCs
    #     tc_by_priority = {}

    #     # Iterate over the job_id dictionary
    #     for feature, tc_list in jobs[job_id].items():
    #         for tc in tc_list:
    #             for tc_name, tc_info in tc.items():
    #                 priority = tc_info["priority"]
    #                 if priority not in tc_by_priority:
    #                     tc_by_priority[priority] = []
    #                 tc_by_priority[priority].append({tc_name: {"Feature": feature, **tc_info}})

    #     return tc_by_priority

    tl_manager = TLManager()
    while True:
        unlocked_tls = tl_manager._get_unlocked_tl_()
        try:
            print(f"Number of Unlocked TLs are {len(unlocked_tls)} {unlocked_tls}")
            for tl in unlocked_tls:
                tl_manager._get_matching_topology(tl)
        except:
            print("None of the TL's are in unlocked state")
        time.sleep(3)
        print(f"sleep for 3 seconds")
