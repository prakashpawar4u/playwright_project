# db_singleton.py
import psycopg2
from psycopg2 import sql


class DatabaseSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, dbname, user, password, host, port):
        if not hasattr(self, "connection"):
            self.connection = psycopg2.connect(
                dbname=dbname, user=user, password=password, host=host, port=port
            )
            self.cursor = self.connection.cursor()

    def query(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def validate_feature_names(self, expected_features):
        query = "SELECT feature FROM release_management"
        results = self.query(query)
        print(results)
        features = [row[0] for row in results]
        return set(features) == set(expected_features)

    def validate_titles(self, expected_titles):
        query = "SELECT title FROM testcase_details"
        results = self.query(query)
        print(results)
        titles = [row[0] for row in results]
        return set(titles) == set(expected_titles)
