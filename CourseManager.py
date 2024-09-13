import sqlite3
from Course import Course, courses, courses_dict
import CourseParser

class CourseManager:

    @staticmethod
    def load_all_courses(pages):
        CourseParser.load_pages(pages)

    @staticmethod
    def create_db():
        conn = sqlite3.connect('courses.db')
        cur = conn.cursor()

        courses_table = '''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            subject TEXT NOT NULL,
            number INTEGER NOT NULL
        )
        '''

        relationships_table = '''
        CREATE TABLE IF NOT EXISTS requisites (
            id INTEGER PRIMARY KEY,
            course_id INTEGER,
            requisites_id INTEGER,
            FOREIGN KEY(course_id) REFERENCES courses(id),
            FOREIGN KEY(requisites_id) REFERENCES courses(id)
        )
        '''

        cur.execute(courses_table)
        cur.execute(relationships_table)

        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def add_courses_to_db(courses):
        conn = sqlite3.connect('courses.db')
        cur = conn.cursor()

        insert_command = '''
        INSERT INTO courses (name, subject, number)
        VALUES (?, ?, ?)
        '''

        # Convert courses to a list of tuples (name, subject, number)
        course_data = [(course.name, course.subject, course.number) for course in courses]

        cur.executemany(insert_command, course_data)

        conn.commit()
        cur.close()
        conn.close()
