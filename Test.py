import sqlite3
from CourseParser import CourseParser
from CourseManager import CourseManager
from Course import Course, courses, courses_dict

class Test:

    #id
    #name
    #subject
    #number

    @staticmethod
    def add_em_1():
        CourseParser.load_all_courses(37)

        CourseManager.create_db()

        CourseManager.add_courses_to_db(courses)


    @staticmethod
    def check_em_1(search_name):

        conn = sqlite3.connect('courses.db')
        cur = conn.cursor()

        cur.execute("SELECT name FROM courses WHERE name LIKE ?", ('%' + search_name + '%',))

        print(cur.fetchall())

        cur.close()
        conn.close()


#Test.add_em_1()

Test.check_em_1("Engineering")
