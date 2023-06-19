import sqlite3
from .tables import *

class Database:
    def __init__(self):
        self.db_file = 'database/student_registration.db'
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_file)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def create_tables(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS student (
                id INTEGER PRIMARY KEY,
                name TEXT,
                faculty TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS registration (
                student_id INTEGER,
                date TEXT,
                entry_time TEXT,
                FOREIGN KEY (student_id) REFERENCES student(id)
            )
        ''')
        self.connection.commit()
        self.disconnect()

    def insert_student(self, student):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO student (id, name, faculty)
            VALUES (?, ?, ?)
        ''', (student.id, student.name, student.faculty))
        self.connection.commit()
        self.disconnect()

    def insert_registration(self, registration):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO registration (student_id, date, entry_time)
            VALUES (?, ?, ?)
        ''', (registration.student_id, registration.date, registration.entry_time))
        self.connection.commit()
        self.disconnect()

    def get_student_by_id(self, student_id):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM student WHERE id = ?', (student_id,))
        row = cursor.fetchone()
        self.disconnect()
        if row:
            return Student(row[0], row[1], row[2])
        return None

    def student_exists(self, student_id):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute('SELECT id FROM student WHERE id = ?', (student_id,))
        row = cursor.fetchone()
        self.disconnect()
        if row:
            return True
        return False

    def get_registration_by_id(self, registration_id):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM registration WHERE id = ?', (registration_id,))
        row = cursor.fetchone()
        self.disconnect()
        if row:
            return Registration(row[0], row[1], row[2])
        return None
