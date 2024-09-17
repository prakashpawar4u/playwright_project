import psycopg2
import random
import time


# Database connection details
db_host = "192.168.56.114"
db_name = "mytest"
db_user = "postgres"
db_password = "postgres"


# Create the table tl_details
def create_tl_details_table():
    try:
        conn = psycopg2.connect(
            host=db_host, database=db_name, user=db_user, password=db_password
        )
        cursor = conn.cursor()

        # Create the table
        create_table_query = """
        CREATE TABLE tl_details (
            tl_name VARCHAR(255) PRIMARY KEY,
            topology JSONB,
            tl_status VARCHAR(20)
        );
        """
        cursor.execute(create_table_query)
        conn.commit()
        print("Table tl_details created successfully!")

    except (Exception, psycopg2.Error) as error:
        print(f"Error creating table: {error}")

    finally:
        if conn:
            cursor.close()
            conn.close()


# Insert initial data into the table
def insert_initial_data():
    try:
        conn = psycopg2.connect(
            host=db_host, database=db_name, user=db_user, password=db_password
        )
        cursor = conn.cursor()

        # Insert data
        insert_data_query = """
        INSERT INTO tl_details (tl_name, topology, tl_status)
        VALUES
            ('Single Cell', '{"CU": 1, "DU": 1, "RU": 1}', 'unlocked'),
            ('intraDU', '{"CU": 1, "DU": 1, "RU": 2}', 'locked'),
            ('HO', '{"CU": 2, "DU": 2, "RU": 3}', 'maintenance');
        """
        cursor.execute(insert_data_query)
        conn.commit()
        print("Initial data inserted successfully!")

    except (Exception, psycopg2.Error) as error:
        print(f"Error inserting data: {error}")

    finally:
        if conn:
            cursor.close()
            conn.close()


# Method to change tl_status
def change_tl_status():
    try:
        conn = psycopg2.connect(
            host=db_host, database=db_name, user=db_user, password=db_password
        )
        cursor = conn.cursor()

        # Select a random tl_name
        cursor.execute("SELECT tl_name FROM tl_details;")
        tl_names = cursor.fetchall()
        random_tl_name = random.choice(tl_names)[0]

        # Update tl_status to 'locked'
        update_locked_query = f"""
        UPDATE tl_details
        SET tl_status = 'locked'
        WHERE tl_name = '{random_tl_name}';
        """
        cursor.execute(update_locked_query)
        conn.commit()
        print(f"{random_tl_name} status changed to 'locked'")

        # Sleep for a random duration between 3 to 10 seconds
        sleep_duration = random.uniform(3, 10)
        print(f"Sleeping for {sleep_duration:.2f} seconds...")
        time.sleep(sleep_duration)

        # Update tl_status back to 'unlocked'
        update_unlocked_query = f"""
        UPDATE tl_details
        SET tl_status = 'unlocked'
        WHERE tl_name = '{random_tl_name}';
        """
        cursor.execute(update_unlocked_query)
        conn.commit()
        print(f"{random_tl_name} status changed back to 'unlocked'")

    except (Exception, psycopg2.Error) as error:
        print(f"Error changing tl_status: {error}")

    finally:
        if conn:
            cursor.close()
            conn.close()


# # Call the functions to create the table and insert initial data
# create_tl_details_table()
# insert_initial_data()

# Call the method to change tl_status
change_tl_status()
