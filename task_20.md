TASKS FROM 15 TO 20

TASK NO 16:

select *
from customers
where fax is not null
order by company_name

![image](https://user-images.githubusercontent.com/113756535/221048307-8c092ca8-c912-45e2-be00-68b4479ef7f7.png)

![image](https://user-images.githubusercontent.com/113756535/221048354-7719eb6a-5516-4ff1-bd1b-1990ef43a230.png)


TASK NO 17:

select *
from employees

![image](https://user-images.githubusercontent.com/113756535/221048575-1e947734-451b-4833-a15c-cb2fb0fd5e60.png)

![image](https://user-images.githubusercontent.com/113756535/221048594-97c1a17d-c0a0-40fa-bf05-d9194e54c8dc.png)


TASK NO 18:

select employee_id       as id,
       last_name         as familya,
       title             as title,
       title_of_courtesy as oilaviy_malumot,
       birth_date        as tugilgan_kun,
       address           as manzil,
       city              as shahar,
       region            as milat,
       postal_code       as post_kodi,
       country           as davlat,
       home_phone        as uy_telofon_raqami,
       photo             as rasm,
       notes             as bildirishnomalar
from employees



![image](https://user-images.githubusercontent.com/113756535/221049262-7de53e63-27c6-4e96-8333-4b1d6eea0502.png)

![image](https://user-images.githubusercontent.com/113756535/221049297-7adb4ef7-43c2-481a-96b9-7cab29c8a510.png)


TASK NO 19:

select first_name
from employees
where title_of_courtesy = 'Mr.'
order by first_name

![image](https://user-images.githubusercontent.com/113756535/221049702-41f1727b-dc1f-43ec-a01a-46609ede4a65.png)

![image](https://user-images.githubusercontent.com/113756535/221049736-9bf77d9e-da23-49f0-ba48-f3a1edeb75f6.png)


TASK NO 20:

select count(*)
from employees
where title = 'Sales Representative'

![image](https://user-images.githubusercontent.com/113756535/221050022-bedea1f7-c209-498d-baf3-ec54bc327019.png)

![image](https://user-images.githubusercontent.com/113756535/221050053-1777060b-5082-4e6e-81bc-b7b76d8cdc4d.png)
