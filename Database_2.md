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
  there is book's information and there
