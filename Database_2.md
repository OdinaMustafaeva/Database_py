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
create table if not exists information_technology_books(
    book_id serial not null ,
    book_about varchar(100) not null ,
    book_page serial not null ,
    book_language varchar(50) not null
);
```
information_technology books 

```sql
create table if not exists english_books(
    book_id serial not null ,
    book_about varchar(100) not null ,
    book_page serial not null ,
    book_language varchar(50) not null
);
```
english books

```sql
create table if not exists novel_books(
    book_id serial not null ,
    book_about varchar(100) not null ,
    book_page serial not null ,
    book_language varchar(50) not null
);
```
novel books

```sql
create table if not exists math_books(
    book_id serial not null ,
    book_about varchar(100) not null ,
    book_page serial not null ,
    book_language varchar(50) not null
);
```

math books


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

![image](https://user-images.githubusercontent.com/113756535/222691210-079d6cd3-9fd3-40e9-b083-a26c717d3452.png)

```sql
insert into english_books(book_id, book_about, book_page, book_language)
values (2, 'grammar ielts', 76, 'english');
```
english books 

![image](https://user-images.githubusercontent.com/113756535/222691441-adb1cdda-3c4f-48c3-a0b4-f50b75058216.png)

```sql
insert into information_technology_books(book_id, book_about, book_page, book_language)
VALUES (3, 'Python', 780, 'russia');
```
information technology 

![image](https://user-images.githubusercontent.com/113756535/222691733-4dc89f5a-9221-4b1e-8ca1-9da361abe6b9.png)

```sql
insert into islamic_books(book_id, book_about, book_page, book_language)
values (2, 'Fotima life', 66000, 'uzbek');
```
islamic books

![image](https://user-images.githubusercontent.com/113756535/222691907-8e1b3b22-ffb2-4778-9af6-9d02ce88051c.png)

```sql
insert into math_books(book_id, book_about, book_page, book_language)
values (5, '5 class math', 350, 'uzbek');
```
math books

![image](https://user-images.githubusercontent.com/113756535/222692105-5edfdef8-29f5-47a5-97e8-dd0ef65d3d8e.png)

```sql
insert into novel_books(book_id, book_about, book_page, book_language)
values (1, 'people life', 450, 'uzbek');
```
novel books 

![image](https://user-images.githubusercontent.com/113756535/222692319-958e0fd3-311e-4074-a3a0-decb7752b325.png)


