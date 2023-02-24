## TASK NO 21:

      select *
      from employees
      where hire_date > '1993-12-31' and hire_date<'1995-01-01'

![image](https://user-images.githubusercontent.com/113756535/221051514-6d237342-d65b-47fa-b213-2977b54a8fc3.png)

![image](https://user-images.githubusercontent.com/113756535/221051552-006e6e0d-d1ac-4cf0-bd94-99337899904e.png)


## TASK NO 22:

      select first_name, last_name, title, city,home_phone
      from employees
      where region is not null
      order by first_name desc 

![image](https://user-images.githubusercontent.com/113756535/221052033-3daf5a01-0aa2-4b05-80ba-c5ea3e60847d.png)


![image](https://user-images.githubusercontent.com/113756535/221052073-07323eff-4c51-453a-96f8-9c3dc54be1df.png)



## TASK NO 23:

      select *
      from orders
      where customer_id = 'VINET'

![image](https://user-images.githubusercontent.com/113756535/221052454-a57e260a-b452-4eef-8cc1-4e57c5a14231.png)

![image](https://user-images.githubusercontent.com/113756535/221052474-5a0b2fa0-d53f-4252-ae18-3dbbbb61d443.png)


## TASK NO 24:

      select *
      from orders
      where order_date > '1995-12-31'
        and order_date < '1997-01-01'

![image](https://user-images.githubusercontent.com/113756535/221052757-0e7b4311-cfb4-41d6-9b2e-2b197104b2fe.png)

![image](https://user-images.githubusercontent.com/113756535/221052806-22c0ab67-d442-4927-b574-1f20149e87c1.png)


## TASK NO 25:

      select *
      from orders
      where ship_region is not null

![image](https://user-images.githubusercontent.com/113756535/221052951-e9cc56ef-bbc6-4a21-b7d4-ca00921f1fe8.png)

![image](https://user-images.githubusercontent.com/113756535/221052981-1b948eac-4869-42fc-aa2d-dc3ffa158654.png)


## TASK NO 26:

    select *
    from orders
    where order_id between 10300 and 10400

![image](https://user-images.githubusercontent.com/113756535/221053181-1a53f3ea-4438-42d1-933f-5e26b6ab84b0.png)


![image](https://user-images.githubusercontent.com/113756535/221053212-995b14ab-b123-4772-bbab-c9d7fc1bba46.png)


## TASK NO 27:

      select sum(unit_price)
      from order_details

![image](https://user-images.githubusercontent.com/113756535/221053443-f239afae-7ebc-4a52-998c-bcdaebcbcf8a.png)

![image](https://user-images.githubusercontent.com/113756535/221053470-f7648b12-ef70-49e8-905f-7dfe5f5ba742.png)


