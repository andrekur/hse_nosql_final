import random
from datetime import date
from datetime import timedelta
from datetime import datetime as dt

from faker import Faker
from faker_commerce import Provider


class BaseFakeGenClass:
	def __init__(self) -> None:
		self._fake = Faker()
		self._fake.add_provider(Provider)

	def _prepared_gen(self, *args, **kwargs):
		return []

	def _after_gen(self, result, *args, **kwargs):
		return result

	def gen_data(self, count=0):
		result = self._prepared_gen()

		for _ in range(count):
			result.append({
				field: getattr(self, f'{field}_gen_func')() if getattr(self, f'{field}_gen_func') else None
				for field in self.fields
			})

		return self._after_gen(result)

class Students(BaseFakeGenClass):
	def __init__(self, courses, teachers, faculties) -> None:
		self.fields = ('first_name', 'last_name', 'email', 'phone', 'admission_date', 'docs', 'courses', 'additional_info', 'faculty', 'group_name')
		self.model_name = 'Students'
		self.colum_id = 'student_id'
		self._courses = courses
		self._faculties = faculties
		self._teachers = teachers
		super().__init__()

	def first_name_gen_func(self):
		return self._fake.first_name()

	def last_name_gen_func(self):
		return self._fake.last_name()

	def email_gen_func(self):
		return self._fake.email()

	def phone_gen_func(self):
		return '1' + self._fake.phone_number()[:random.randint(12, 16)]

	def admission_date_gen_func(self):
		return self._fake.date_time_between(start_date=date(2022, 1, 1), end_date=date(2023, 1, 1))
	
	def faculty_gen_func(self):
		faculty = random.choice(self._faculties)

		return {
			'_id': faculty['_id'],
			'name': faculty['name']
		}
	
	def group_name_gen_func(self):
		arr = [chr(random.randint(ord("a"), ord("z"))) for _ in range(3)]
		return f'{"".join(arr)}-{random.randint(10, 99)}'

	def docs_gen_func(self):
		return [
			{
				'name': self._fake.text(30),
				'link': f'https://placehold.it/{random.randint(1, 100000)}',
				'description': self._fake.text(50)
			}
			for _ in range(5)
		]

	def courses_gen_func(self):
		items = []

		for _ in range(3, random.randint(5, 20)):
			course =  random.choice(self._courses)
			items.append({
				'course_id': course['_id'],
				'course_name': course['name'],
				'year': (dt.now() - timedelta(5 * random.randint(300, 360))).year,
				'semester': random.choice([1, 2, 3, 4]),
			})

		for item in items:
			is_credit = bool(random.randint(-1, 1))
			is_success = bool(random.randint(-1, 1))

			if is_credit:
				item['grade'] = {
					'credit': is_success
				}
			else:
				item['grade'] = {
					'credit': random.choice([3, 4, 5]) if is_success else None
				}

			teacher = random.choice(self._teachers)
			item['maintainer'] = teacher['_id']
			item['maintainer_fio'] = teacher['first_name'] + '  ' + teacher['last_name']
		
		return items
	
	def additional_info_gen_func(self):
		data = {
			'about_me': self._fake.text(30),
			'other_contacts': {
				'icq': self._fake.text(30),
				'telegram': self._fake.text(30),
				'other': 'moydodyr.ru',
			},
			'free_in_time': f'{random.randint(00, 18)}-{random.randint(19, 24)}'
		}
		
		# моделируем фейк изъятие
		del data[random.choice(('about_me', 'other_contacts', 'free_in_time'))]
	
		return data
 

class Courses(BaseFakeGenClass):
	def __init__(self) -> None:
		self.fields = ('name', 'description', )
		self.model_name = 'Courses'
		self.colum_id = 'course_id'
		super().__init__()

	def name_gen_func(self):
		return self._fake.text(50)

	def description_gen_func(self):
		return self._fake.text(200)
	
	def docs_gen_func(self):
		return [{
			'name': self._fake.text(30),
			'link': f'https://placehold.it/{random.randint(1, 100000)}',
			'description': self._fake.text(50)
		} for _ in range(0, random.randint(0, 3))]


class Teachers(BaseFakeGenClass):
	def __init__(self, courses) -> None:
		self.fields = ('first_name', 'last_name', 'email', 'phone', 'created_at', 'docs', 'additional_info', 'courses')
		self.model_name = 'Teachers'
		self.colum_id = 'teacher_id'
		self._courses = courses
		super().__init__()

	def first_name_gen_func(self):
		return self._fake.first_name()

	def last_name_gen_func(self):
		return self._fake.last_name()

	def email_gen_func(self):
		return self._fake.email()

	def phone_gen_func(self):
		return '1' + self._fake.phone_number()[:random.randint(12, 16)]
	
	def courses_gen_func(self): # которые он может читать

		items = random.choices(self._courses, k=random.randint(3, 8))
		result = [{
			'_id': item['_id'],
			'name': item['name']
		} for item in items]

		return result

	def created_at_gen_func(self):
		return self._fake.date_time_between(start_date=date(1800, 1, 1), end_date=date(2023, 1, 1))

	def docs_gen_func(self):
		return [
			{
				'name': self._fake.text(30),
				'link': f'https://placehold.it/{random.randint(1, 100000)}',
				'description': self._fake.text(50)
			}
			for _ in range(5)
		]
	
	def additional_info_gen_func(self):
		coffee = [
    		'Эспрессо',
    		'Американо',
    		'Капучино',
    		'Латте',
    		'Мокка'
		]

		data = {
			'about_me': self._fake.text(30),
			'other_contacts': {
				'icq': self._fake.text(30),
				'telegram': self._fake.text(30),
				'other': 'moydodyr.ru',
			},
			'free_in_time': f'{random.randint(00, 18)}-{random.randint(19, 24)}',
			'coffee': random.choice(coffee)
		}
		
		# моделируем фейк изъятие
		del data[random.choice(('free_in_time', 'coffee'))]
		del data[random.choice(('about_me', 'other_contacts', ))]

		return data



class Faculties(BaseFakeGenClass):
	def __init__(self, teachers) -> None:
		self.fields = ('name', 'description', 'email', 'teamlead', 'placeholder', 'created_at', 'docs')
		self.model_name = 'Faculties'
		self.colum_id = 'faculty_id'
		self._teachers = teachers
		super().__init__()

	def name_gen_func(self):
		return self._fake.text(40)

	def description_gen_func(self):
		return self._fake.text(400)

	def placeholder_gen_func(self):
		items = random.choices(self._teachers, k=random.randint(2, 15))

		return [{
			'_id': item['_id'],
			'first_name': item['first_name'],
			'last_name': item['last_name'],
		} for item in items]

	def email_gen_func(self):
		return self._fake.email()
	
	def teamlead_gen_func(self):
		item =  random.choice(self._teachers)

		return {
			'_id': item['_id'],
			'first_name': item['first_name'],
			'last_name': item['last_name'],
		}

	def created_at_gen_func(self):
		return self._fake.date_time_between(start_date=date(1800, 1, 1), end_date=date(2023, 1, 1))

	def docs_gen_func(self):
		return [
			{
				'name': self._fake.text(30),
				'link': f'https://placehold.it/{random.randint(1, 100000)}',
				'description': self._fake.text(50)
			}
			for _ in range(5)
		]
