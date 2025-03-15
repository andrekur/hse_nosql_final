// Индекс для поиск/сортировки студентов по дате поступления

db.Students.createIndex({ admission_date: 1 });