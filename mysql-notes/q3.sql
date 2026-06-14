--Inserting more sample data

-- run below query to add new record
insert into
    employees (id, name, email, department, salary)
values
    (1, "John", "john@gmail.com", "IT", 3500);

-- run below query to add new record
insert into
    employees (id, name, email, department, salary)
values
    (2, "Mike", "mike@gmail.com", "Admin", 2700);

-- run below query to add new record
insert into
    employees (id, name, email, department, salary)
values
    (3, "Amy", "amy@gmail.com", "IT", 3000);

-- run below query to add new record
insert into
    employees (id, name, email, department, salary)
values
    (4, "Cathy", "cathy@gmail.com", "HR", 3200);

-- run below query to add new record
insert into
    employees (id, name, email, department, salary)
values
    (5, "Brian", "brian@gmail.com", "HR", 4500);

--verify if all data has been inserted
select * from employees;