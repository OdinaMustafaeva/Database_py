## DATABASE TRELLO

## CREATE DATABASE:
    CREATE DATABASE trello;

    ...

![image](https://user-images.githubusercontent.com/113756535/222974276-1b5f82ce-cee5-4e4f-a220-de41160d9d40.png)

```py
import psycopg2
import psycopg2.extras

conection = psycopg2.connect(
    dbname='trello',
    user='postgres',
    password='43201',
    host='localhost',
    port=5432
)
cur = conection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
 ```

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

    
```sql
    create table boards(
      id serial unique not null ,
      user_id serial not null ,
      board varchar(150) not null
);
   ```
    
Boards table 

![image](https://user-images.githubusercontent.com/113756535/223029350-b9d5d2c4-3e14-4424-a809-8ea60f776c2d.png)

  
```sql
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


## NEW user /register

![image](https://user-images.githubusercontent.com/113756535/223031796-2d8dad2e-dca4-452d-87bc-cc3a584d8ae1.png)

```py
def get_trello_username(message):
    write_chat_to_csv(message)
    bot.send_message(message.chat.id, messages.ADD_SUCCESSFULLY)
```

```py
 def write_chat_to_csv(message):
    print("Chat add successfully.")
    sql = "insert into users(user_id, first_name, last_name, trello_username) values (%s, %s, %s, %s)"
    cur.execute(sql, (message.chat.id, message.from_user.first_name, message.from_user.last_name, message.text))
    conection.commit()
```

![image](https://user-images.githubusercontent.com/113756535/223032308-415a4482-dbe7-4c5d-b42f-b67124b2d5ab.png)


## /boards
![image](https://user-images.githubusercontent.com/113756535/223031125-df42b214-da4d-459f-992b-836ec5507a15.png)

```py
@bot.message_handler(commands=["boards"])
def get_boards(message):
    if not check_chat_id_from_csv(message.chat.id):
        bot.send_message(message.chat.id, messages.TRELLO_USERNAME_NOT_FOUND)
    else:
        trello_username = get_trello_username_by_chat_id(message.chat.id)
        if trello_username:
            bot.send_message(
                message.chat.id, messages.SELECT_BOARD,
                reply_markup=get_inline_boards_btn(trello_username)
            )
        else:
            bot.send_message(message.chat.id, messages.TRELLO_USERNAME_NOT_FOUND)
  ```

```py
    inline_boards_btn = InlineKeyboardMarkup()
    sql = f"select board from boards where trello_username={trello_usernae}"
    cur.execute(sql)
    conection.commit()
    b = cur.fetchall()
    for i in b:
        inline_boards_btn.add(
            InlineKeyboardButton(i[0], callback_data=f'{trello_usernae}')
        )

    return inline_boards_btn
```

