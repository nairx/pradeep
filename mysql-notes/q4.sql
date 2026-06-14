--Querying

select * from employees;

select name,email,department from employees order by name;

select * from employees where department = "IT";

select * from employees where salary > 3000;

select * from employees where salary > 3000 and department = "HR";

select * from employees where salary > 3000 or department = "HR";

select * from employees where salary > 3000 and salary < 4000;

select * from employees where salary >= 3200 and salary < 4000;

select * from employees where salary > 3000 and department in ("HR","IT");



