import sqlite3

class DB_Manager:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_capital(self, country):
        """Получает столицу страны из базы данных"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT capital_exonym FROM countries_and_capitals WHERE country_exonym = ?", (country,))
        result = cursor.fetchone()
        conn.close()

        return result[0] 
