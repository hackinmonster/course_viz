import requests
from bs4 import BeautifulSoup
import re
from Course import Course, courses, courses_dict

class CourseParser:
    @staticmethod
    def load_courses_from_page(page):
        base_url = "https://catalog.charlotte.edu/content.php?filter%5B27%5D=-1&filter%5B29%5D=&filter%5Bkeyword%5D=&filter%5B32%5D=1&filter%5Bcpage%5D=" + str(page) + "&cur_cat_oid=38&expand=1&navoid=4596&print=1#acalog_template_course_filter"
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        course_data = soup.findAll('td', class_='width')
        course_id = 0

        for course in course_data:
            course_text = course.find('h3').get_text(strip=True).split(' - ')
            course_name = course_text[1]
            course_text = course_text[0].split(' ')
            course_subject = course_text[0]
            course_number = course_text[1]
            course_id += 1

            new_course = Course(course_id, course_name, course_subject, course_number)
            courses.append(new_course)

            key = f"{new_course.subject} {new_course.number}"
            courses_dict[key] = (new_course, course_id)

    @staticmethod
    def load_requisites_from_page(page):
        base_url = "https://catalog.charlotte.edu/content.php?filter%5B27%5D=-1&filter%5B29%5D=&filter%5Bkeyword%5D=&filter%5B32%5D=1&filter%5Bcpage%5D=" + str(page) + "&cur_cat_oid=38&expand=1&navoid=4596&print=1#acalog_template_course_filter"
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        course_data = soup.findAll('td', class_='width')

        for course in course_data:
            course_text = course.find('h3').get_text(strip=True).split(' - ')
            course_text = course_text[0].split(' ')
            course_subject = course_text[0]
            course_number = course_text[1]

            key = f"{course_subject} {course_number}"
            course_pattern = r'\b[A-Z]{4} \d{4}\b'
            prereq_section = course.find('strong', string="Prerequisite(s):")

            if prereq_section is None:
                pass
            else:
                prereq_text = ' '.join(sibling.text.strip() for sibling in prereq_section.find_next_siblings('a'))
                prereqs = re.findall(course_pattern, prereq_text)

                if key not in courses_dict: 
                    pass
                else:
                    course_obj, course_id = courses_dict[key]

                    for prereq in prereqs:
                        if prereq in courses_dict: 
                            requisite_obj, requisite_id = courses_dict[prereq]
                            course_obj.requisites.append(requisite_obj)
                            

            


    @staticmethod
    def load_all_courses(pages):
        for page in range(1, pages + 1):
            CourseParser.load_courses_from_page(page)
        
    @staticmethod
    def load_all_relationships(pages):
        for page in range(1, pages + 1):
            CourseParser.load_relationships_from_page(page)



