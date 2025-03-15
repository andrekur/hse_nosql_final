// Общий файл с индексами

// Индекс для поиск всех студентов группы
db.Students.createIndex({ group_name: 1 });

// Индекс для поиск всех студентов определенного факультета и группы
db.Students.createIndex({ 'faculty._id': 1, 'group_name': 1 });

// Индекс для поиск/сортировки студентов по дате поступления
db.Students.createIndex({ admission_date: 1 });

// Индекс для поиск всех Преподавателей, кто может вести данный курс
db.Teachers.createIndex({ 'courses._id': 1 });

// Индекс для поиск и сортировки курсов по его названию
db.Courses.createIndex({ name: 1 });
db.Courses.createIndex({ name: 'text' });