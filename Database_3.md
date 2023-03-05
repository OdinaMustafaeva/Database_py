## DATABASE TRELLO

## CREATE DATABASE:
    CREATE DATABASE trello;

    ...

![image](https://user-images.githubusercontent.com/113756535/222974276-1b5f82ce-cee5-4e4f-a220-de41160d9d40.png)

## Create Table:
```sql
    create table users(
    user_id serial unique not null ,
    first_name varchar(50) not null ,
    last_name varchar(50) default 0,
    trello_username varchar(80) not null
);
   ```
    
Users table 
    
```sql
    create table boards(
      id serial unique not null ,
      user_id serial not null ,
      board varchar(150) not null
);
   ```
    
Boards table 
  
```sql
  create table lists(
    id serial unique not null ,
    user_id serial not null ,
    list varchar(150) not null
);
  ```
  
Lists table

```sql
   create table cards(
    id serial unique not null ,
    user_id serial not null ,
    card varchar(150) not null
);
  ```
   
Cards table 

```sql
     create table members(
      id serial unique not null ,
      user_id serial not null ,
      member varchar(150) not null
 );
   ```
      
Crads table 

