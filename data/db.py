import os
import sqlite3


def find_master_by_recording_id(recording_id):
    res = execute_user_database_query(f'SELECT user_id FROM masters WHERE show_id = {recording_id};')
    return res[0][0] if len(res) > 0 and len(res[0]) > 0 else None


def get_user_info_by_id(user_id):
    res = execute_user_database_query(f'SELECT name, email FROM users WHERE id = {user_id};')
    if res is None or len(res) < 0 or len(res[0]) < 0:
        return {}
    return {'user': res[0][0], 'email': res[0][1]}


def execute_user_database_query(query):
    sqlite_connection = None
    try:
        dirname = os.path.dirname(__file__)
        path_to_db = os.path.join(dirname, '../encora.db')
        sqlite_connection = sqlite3.connect(path_to_db)
        cursor = sqlite_connection.cursor()

        cursor.execute(query)
        res = cursor.fetchall()

        cursor.close()
        return res
    except sqlite3.Error as error:
        print("Unable to connect to user database", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
    return None
