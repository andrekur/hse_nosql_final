from models import (
  Students, Teachers, Courses, Faculties
)
from pymongo import MongoClient

from dotenv import dotenv_values

CONFIG = dotenv_values('./.env')

MONGO_URI = f"mongodb://{CONFIG['DB_MONGO_USER']}:{CONFIG['DB_MONGO_PASSWORD']}@{CONFIG['DB_MONGO_HOST']}:{CONFIG['DB_MONGO_PORT']}/"
DB_MONGO_NAME_DB = CONFIG['DB_MONGO_NAME_DB']


if __name__ == '__main__':
	client = MongoClient(MONGO_URI)

	db = client[DB_MONGO_NAME_DB]

	course_collection = db['Courses']
	course = Courses()
	course_result = course.gen_data(1000)
	course_ids = course_collection.insert_many(course_result).inserted_ids

	teacher_collection = db['Teachers']
	teacher = Teachers(course_result)
	teacher_result = teacher.gen_data(200)
	teacher_ids = teacher_collection.insert_many(teacher_result).inserted_ids

	faculty_collection = db['Faculties']
	faculty = Faculties(teacher_result)
	faculty_result = faculty.gen_data(200)
	faculty_ids = faculty_collection.insert_many(faculty_result).inserted_ids

	student_collection = db['Students']
	student = Students(course_result, teacher_result, faculty_result)
	student_result = student.gen_data(200)
	student_ids = student_collection.insert_many(student_result).inserted_ids
