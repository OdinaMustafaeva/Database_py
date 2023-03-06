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

![image](https://user-images.githubusercontent.com/113756535/223029416-82a284e4-49bb-432d-ac0a-462ccbe3613a.png)

    
```
    create table boards(
      id serial unique not null ,
      user_id serial not null ,
      board varchar(150) not null
);
   ```
    
Boards table 

![image](https://user-images.githubusercontent.com/113756535/223029350-b9d5d2c4-3e14-4424-a809-8ea60f776c2d.png)

  
```
  create table lists(
    id serial unique not null ,
    user_id serial not null ,
    list varchar(150) not null
);
  ```
  
Lists table

![image](https://user-images.githubusercontent.com/113756535/223029443-19e4585a-c5f1-4cf3-bf3a-5a210e71f2fa.png)


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
      
members table 

## RUN
   ## /START
    ![image](https://user-images.githubusercontent.com/113756535/223029622-2345f59c-9338-461c-adac-8fa2fd2f4888.png)

    ```py
    @bot.message_handler(commands=["register"])
    def register_handler(message):
        if not check_chat_id_from_csv(message.chat.id):
            bot.send_message(message.chat.id, messages.SEND_TRELLO_USERNAME)
            bot.register_next_step_handler(message, get_trello_username)
        else:
            bot.send_message(message.chat.id, messages.ALREADY_REGISTERED)
    ```


    ```py
    def check_chat_id_from_csv(chat_id):
        sql = "select user_id from users"
        cur.execute(sql)
        conection.commit()
        b = cur.fetchall()
        return chat_id in [int(row.get("user_id")) for row in b]
    ```

![image](https://user-images.githubusercontent.com/113756535/223030165-2981ca28-96f5-4589-9df4-b88a5085a14b.png)
