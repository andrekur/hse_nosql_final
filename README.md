# hse_nosql_final

Финальная работа по NoSQL by **andrekur**

## Установка
```
git clone https://github.com/andrekur/hse_nosql_final.git
cd hse_nosql_final
mv env.example .env
sudo docker-compose up -d
```

В ```.env``` файле прописаны все порты и конфигурация проекта.
<br>

## Структура проекта
```./data_gen/main.py``` - генератор данных для БД
<br>```./indexes/all_index.js``` - код для создания индексов в БД
<br>```./queries/all-queries.js``` - 10 запросов к БД
<br>```./schemas/{название_схемы}.js``` - схемы для каждой коллекции, согласно заданию<br>
<br>

## Отчет
```./Курепин_МИНДА241_NOSQL_ДЗ_ФИНАЛ.pdf``` - отчет по работе
<br>

## Контейнера
1. **Mongo** - целевая БД
3. **data_gen** - генерация данных для БД Mongo 