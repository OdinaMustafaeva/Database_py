## TASK NO 11:
  
    select *
    from customers
    where city='London'

![image](https://user-images.githubusercontent.com/113756535/221046246-a1b98e1d-0f1c-4906-9a9e-839d4c4ad71a.png)

![image](https://user-images.githubusercontent.com/113756535/221046288-8cc4bda0-ffa3-4898-8cbe-d82287f35648.png)

TASK NO 12:

select *
from customers
where customers.region is null

![image](https://user-images.githubusercontent.com/113756535/221046568-463bc8c3-e113-4a0a-a52a-cb72fdc8b700.png)

![image](https://user-images.githubusercontent.com/113756535/221046642-e1a26003-48a8-403b-97e3-a342edb87a19.png)

TASK NO 13:

select *
from customers
where customers.region is not null

![image](https://user-images.githubusercontent.com/113756535/221046743-42837f1a-95ed-4e02-a6bf-cade90260396.png)

![image](https://user-images.githubusercontent.com/113756535/221046813-2e4cd53c-16cb-4f13-bb21-0492dc3e5405.png)

TASK NO 14:

select *
from customers
where country != 'Germany'

![image](https://user-images.githubusercontent.com/113756535/221047108-1238c9b0-8447-4961-8af7-12d5e80b9acc.png)

![image](https://user-images.githubusercontent.com/113756535/221047155-600467dd-5e3d-4c08-b11a-ec11cdb7691f.png)


TASK NO 15:

select count(*) as mintaqalar_soni
from customers
where country = 'Germany'

![image](https://user-images.githubusercontent.com/113756535/221047522-15b28208-eed5-4c05-9d51-8e851bf635c9.png)


![image](https://user-images.githubusercontent.com/113756535/221047491-652d29ce-cee5-4bff-baf3-8ba41a882c7f.png)


