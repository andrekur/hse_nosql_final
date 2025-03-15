// Индекс для поиск всех студентов определенного факультета и группы

db.Students.createIndex({ "faculty._id": 1, "group_name": 1 });