CRUD Operation

C - Create
R - Read
U - Update
D - Delete

--Create
insert into
    employees (id, name, email, department, salary)
values
    (1, "John", "john@gmail.com", "IT", 3500);

--Read
select * from employees;

--Update
update employees set salary = 3700 where id=1;

--Delete
delete from employees where id=1;

