// 1.	Поиск информации о Студенте по его идентификатору
db.Students.find({_id: ObjectId('67d5aaf7ba7587ca4ecc07fc')}, { docs: 0, courses: 0});

//2.	Поиск студентов, состоящих в одной группе
db.Students.find({ group_name: 'kms-13'}, { docs: 0, courses: 0, faculty: 0});

// 3.	Поиск студентов с долгами (есть дисциплины без зачетов/оценок)
db.Students.find({
    $or: [
      { 'courses.grade.credit': false }, // нет экзамена
      { 'courses.grade.credit': null } // нет зачета
    ]
});

// Запросы количества
db.Students.find({ $or: [
    { 'courses.grade.credit': false },
    { 'courses.grade.credit': null } ]
}).count(); // есть хоть один долг по дисциплине
db.Students.find({ 'courses.grade.credit': null }).count(); // не сдан экзамен
db.Students.find({ 'courses.grade.credit': false  }).count(); // не сдан зачет

// 4.	Поиск преподавателя по идентификатору
db.Teachers.find({_id: ObjectId('67d5a5495fe1b373ef5aec90')}, { docs: 0});

// 5.	Поиск всех Преподавателей, кто может преподавать определенный курс
db.Teachers.find(
  {'courses._id': ObjectId('67d5a5495fe1b373ef5ae8a5')},
  {first_name: 1, last_name: 1, phone: 1}
);

// 6.	Добавление нового Преподавателя

db.Teachers.insertOne({
    first_name: 'Дмитрий',
    last_name: 'Калугин-Балашов',
    email: 'test-email@example.com',
    phone: '1234567890',
    created_at: new Date(),
    additional_info: {
      about_me: 'Преподаватель дисциплины Нереляционные базы данных',
      other_contacts: {
        telegram: '@test'
      }
    }
  });

db.Teachers.find({'_id': ObjectId('67d5c8b9c6545d28046b140c')});

// 7.	Добавление преподавателю нового курс
db.Teachers.updateOne(
    { _id: ObjectId('67d5c8b9c6545d28046b140c') },
    { $push: { courses: { _id: ObjectId('67d5a5495fe1b373ef5ae8a7'), name: 'NoSQL' }}}
  );

// 8.	Поиск курса по ключевому слову
db.Courses.find({ $text: { $search: 'pattern' } }, {_id: 0, description: 0});

// 9.   Удалим информацию о курсе у студента, предположим он перевелся

db.Students.find(
  {_id: ObjectId('67d5a54b5fe1b373ef5aee37')},
  { first_name: 1, last_name: 1, courses: 1}
);

db.Students.updateOne(
    { _id: ObjectId('67d5a54b5fe1b373ef5aee37') },
    { $pull: { courses: { course_id: ObjectId('67d5a5495fe1b373ef5aea56') }}}
);

// 10.   Найдем статистку по принятию студентов по годам

db.Students.aggregate([
    {
      $group: {
        _id: { $year: '$admission_date' },
        count: { $sum: 1 }
      }
    },
    { $sort: { _id: 1 } }
]);
