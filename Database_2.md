## BOOK SHOP DATABASE

![image](https://user-images.githubusercontent.com/113756535/222557055-3648d929-621c-493c-bdfb-5815e5891485.png)

## Create tables 
  book table
  ```sql
  create table if not exists book(
    book_id serial not null unique,
    book_name varchar(100) not null,
    book_price serial not null ,
    book_authors varchar(60) not null ,
    book_year date,
    book_color varchar(20)
  );
  ```
  there is book's information

  ```sql
  create table if not exists customers(
    customer_id serial not null unique ,
    customer_name varchar(50) not null ,
    customer_address varchar(100) not null unique ,
    customer_phone_number serial not null unique
 );
  ```
  customer's information

  ```sql
  create table if not exists sold_books(
    book_id serial not null,
    customer_id serial not null ,
    date_buy date not null
 );
  ```
  sold books information
  
```sql
create table book_type(
     id serial not null,
     about varchar(100) not null ,
     book_id serial nott null,
     page serial not null ,
     language varchar(50) not null
 );
```
 book type


## Insert into 
  ```sql
insert into books(book_id, book_name, book_price, book_authors, book_year, book_color)
VALUES (1, 'ikki eshik orasi', 43000, 'Utkir Hoshimov', '1986-01-01','red'),
       (2, 'Fotima onamiz', 150000, 'saodat', '2009-01-01', 'white'),
       (3, 'IT Life', 99000, 'A.Th.JOHN', '2011-01-01', 'black'),
       (4, 'Tactic listening basic', 35000,'H.Y.JACK', '1999-01-01', 'yellow'),
       (5, 'matematika', 56000, 'V.kim', '2017-01-01', 'blue');
  ```
  books 
  
![image](https://user-images.githubusercontent.com/113756535/222690527-1e1a894d-5c6a-4db0-863d-b70942d4e0a1.png)

```sql
insert into customers(customer_id, customer_name, customer_address, customer_phone_number, customer_age)
VALUES (1, 'Lisa', 'Uzb/tashkent/312cdscfe3xs', '1234431', 25),
        (2, 'Mila', 'Uzb/tashkent/465rgdfgdsf', '988766', 32),
        (3, 'Jin', 'Uzb/tashkent/9129376savhbssv', '67564', 22),
        (4, 'hela', 'London/00r93249348', '123456', 36),
        (5, 'Ila', 'Uzb/2389743896532', '44325', 19);
```

customers

![image](https://user-images.githubusercontent.com/113756535/222691020-07390c74-6de6-4b77-b9cd-3a7bd7eca937.png)

```sql
insert into sold_books(book_id, customer_id, date_buy)
values (1, 5, '2023-03-03'),
       (2,4,'2023-02-25'),
       (3,3, '2022-09-05'),
       (4, 2, '2023-01-01'),
       (5, 1, '2022-12-27');
```
sold books

![image](https://user-images.githubusercontent.com/113756535/222988675-23a32b1e-ebf7-43c4-bbb0-0c93dcb2a022.png)


```sql
insert into book_type(id, book_id, about, page, language)
  values (1, 2,'grammar ielts',76,'english'),
  (2, 3,'Python',780,'russia'),
  (3, 2,'Fotima life',66000,'uzbek'),
  (4, 5,'5 class math',350,'uzbek'),
  (5, 1,'people life',450,'uzbek');

```

![image](https://user-images.githubusercontent.com/113756535/222988689-df16fc4b-187e-4748-ac6e-0e55c561dd75.png)



