// Индекс для поиск и сортировки курсов по его названию

db.Courses.createIndex({ name: 1 });
db.Courses.createIndex({ name: 'text' });