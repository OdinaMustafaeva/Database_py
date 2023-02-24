## TASK NO 1 :

    select * 
    from categories

![image](https://user-images.githubusercontent.com/113756535/221043420-f82bb870-2ff6-4d13-a25d-e0e87c7c41d2.png)


![image](https://user-images.githubusercontent.com/113756535/221038863-238b4518-5af4-496c-aa68-e9994579c711.png)

## TASK NO 2 :

    select category_name, description 
    from categories
  
  

![image](https://user-images.githubusercontent.com/113756535/221043476-e800531b-9f9c-49be-ae4a-e8644a0e8400.png)


![image](https://user-images.githubusercontent.com/113756535/221039102-4a2bb7a4-5878-4669-a65c-c34c5dc6a7d5.png)

## TASK NO 3 :

    select category_name as nomi, description as tavsifi 
    from categories


![image](https://user-images.githubusercontent.com/113756535/221043537-b23cb6bb-611d-40c7-8508-32d6b5b27dd1.png)


![image](https://user-images.githubusercontent.com/113756535/221039789-05075fe8-57a5-477b-90e6-958b8af2b453.png)

## TASK NO 4 :

  select * 
  from categories 
  where category_name ='Confections'

  ![image](https://user-images.githubusercontent.com/113756535/221043586-b809e82e-c669-4f41-a5bb-5b2bb07da255.png)


  ![image](https://user-images.githubusercontent.com/113756535/221041335-4369c93b-3921-44d0-97aa-b95857877d3d.png)

## TASK NO 5 :

    select *
    from categories
    where category_name ='Confections' or category_name='Seafood'

  ![image](https://user-images.githubusercontent.com/113756535/221043640-d9e9d30a-cbb7-4587-9844-87bd274ccf61.png)


  ![image](https://user-images.githubusercontent.com/113756535/221041732-f6abcb24-02de-4a67-8673-7608fe909545.png)


## TASK NO 6 :

       select *
       from categories
       limit 3 offset 5

![image](https://user-images.githubusercontent.com/113756535/221043141-d7008650-d7dd-46a9-8779-dd6013ea231a.png)

![image](https://user-images.githubusercontent.com/113756535/221042357-efdff9bf-00a5-43d4-97a4-f7e04c5f3ce5.png)

## TASK NO 7:

       select description
       from categories
       order by description DESC 

![image](https://user-images.githubusercontent.com/113756535/221043057-a1442058-3070-4057-95ad-3cc7e8995f15.png)

![image](https://user-images.githubusercontent.com/113756535/221042988-beb7ecd4-ef09-449b-a1c3-10ecd50c2a10.png)

## TASK NO 8 :

       select *
       from customers

![image](https://user-images.githubusercontent.com/113756535/221044414-986b834d-96ac-4ddd-9079-36caaab7ea56.png)

![image](https://user-images.githubusercontent.com/113756535/221044501-88de546c-be59-480e-9156-d64689b1da46.png)

## TASK NO 9:

       select company_name  as companiya_nomi,
              contact_name  as chqarish_ismi,
              contact_title as ulanish_title,
              address       as manzil,
              city          as shahar,
              region        as mintaqa,
              postal_code   as postal_kodi,
              country       as davlat,
              phone         as tel_raqam,
              fax           as fax
       from customers


![image](https://user-images.githubusercontent.com/113756535/221045415-35812042-4082-458b-b4bf-5824b92d43be.png)


![image](https://user-images.githubusercontent.com/113756535/221045532-6e563390-f0d7-4738-8fac-3072d41ea2da.png)

## TASK NO 11:
  
    select *
    from customers
    where city='London'

![image](https://user-images.githubusercontent.com/113756535/221046246-a1b98e1d-0f1c-4906-9a9e-839d4c4ad71a.png)

![image](https://user-images.githubusercontent.com/113756535/221046288-8cc4bda0-ffa3-4898-8cbe-d82287f35648.png)

## TASK NO 12:

    select *
    from customers
    where customers.region is null

![image](https://user-images.githubusercontent.com/113756535/221046568-463bc8c3-e113-4a0a-a52a-cb72fdc8b700.png)

![image](https://user-images.githubusercontent.com/113756535/221046642-e1a26003-48a8-403b-97e3-a342edb87a19.png)

## TASK NO 13:

    select *
    from customers
    where customers.region is not null

![image](https://user-images.githubusercontent.com/113756535/221046743-42837f1a-95ed-4e02-a6bf-cade90260396.png)

![image](https://user-images.githubusercontent.com/113756535/221046813-2e4cd53c-16cb-4f13-bb21-0492dc3e5405.png)

## TASK NO 14:

    select *
    from customers
    where country != 'Germany'

![image](https://user-images.githubusercontent.com/113756535/221047108-1238c9b0-8447-4961-8af7-12d5e80b9acc.png)

![image](https://user-images.githubusercontent.com/113756535/221047155-600467dd-5e3d-4c08-b11a-ec11cdb7691f.png)


## TASK NO 15:

    select count(*) as mintaqalar_soni
    from customers
    where country = 'Germany'

![image](https://user-images.githubusercontent.com/113756535/221047522-15b28208-eed5-4c05-9d51-8e851bf635c9.png)


![image](https://user-images.githubusercontent.com/113756535/221047491-652d29ce-cee5-4bff-baf3-8ba41a882c7f.png)

## TASK NO 16:

       select *
       from customers
       where fax is not null
       order by company_name

![image](https://user-images.githubusercontent.com/113756535/221048307-8c092ca8-c912-45e2-be00-68b4479ef7f7.png)

![image](https://user-images.githubusercontent.com/113756535/221048354-7719eb6a-5516-4ff1-bd1b-1990ef43a230.png)


## TASK NO 17:

       select *
       from employees

![image](https://user-images.githubusercontent.com/113756535/221048575-1e947734-451b-4833-a15c-cb2fb0fd5e60.png)

![image](https://user-images.githubusercontent.com/113756535/221048594-97c1a17d-c0a0-40fa-bf05-d9194e54c8dc.png)


## TASK NO 18:

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


## TASK NO 19:

       select first_name
       from employees
       where title_of_courtesy = 'Mr.'
       order by first_name

![image](https://user-images.githubusercontent.com/113756535/221049702-41f1727b-dc1f-43ec-a01a-46609ede4a65.png)

![image](https://user-images.githubusercontent.com/113756535/221049736-9bf77d9e-da23-49f0-ba48-f3a1edeb75f6.png)


## TASK NO 20:

       select count(*)
       from employees
       where title = 'Sales Representative'

![image](https://user-images.githubusercontent.com/113756535/221050022-bedea1f7-c209-498d-baf3-ec54bc327019.png)

![image](https://user-images.githubusercontent.com/113756535/221050053-1777060b-5082-4e6e-81bc-b7b76d8cdc4d.png)



