# SQL
pronounced squel

`.sql` extension for sql statements script to execute it
```bash
mysql -u "username" -p "password" < /tmp/myfile.sql
```

and from mysql shell
```sql
source file.sql
```


## Table structure (DDL Data Definition Lamguage)

| **Commands**                                                                   | **Description**             | **More Info** |
|--------------------------------------------------------------------------------|-----------------------------|---------------|
| `show databases`                                                               | list databases              |               |
| `use <databease name>`                                                         | switch to the database      |               |
| `CREATE DATABASE <databases name>`                                             | create new database         |               |
| `SHOW TABLES`                                                                  | list tables in database     |               |
| `DROP TABLE <table name>`                                                      | remove table                |               |
| `DESCRIBE <table name>`                                                        | shows  structure table      |               |




### `ALTER TABLE <table name>`
| **Commands**                                                                      | **Description**    | **Example**                                                         |
|-----------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------|
|                                                                                   | rename table       |                                                                     |
| `RENAME  COLUMN <old attribute name> to <new attribute name>`                     | rename attribute   |                                                                     |
| `MODIFY COLUMN <attribute name> <new Type>`                                       | redefines the type | `alter table customers modify customer_name varchar(100) not null;` |
| `ADD (<new attribute name> <type>, <new attribute name> <type>)`                  | add new column     |                                                                     |
| `DROP <column name>`                                                              | remove column      |                                                                     |
| `ADD CONSTRAINT <your constraint name> CONSTRAINT_TYPE (cloumn1,column2,...... )` | add constraint     |                                                                     |
| `DROP CONSTRAINT <constraint_name>`                                               | remove constraint  |                                                                     |
| `DROP CHECK <check name>`                                                         | for mysql only     |                                                                     |
| `DISABLE CONSTRAINT <constraint name>`                                            | disable constraint |                                                                     |
| `ENABLE CONSTRAINT <constraint name>`                                             | enable constraint |                                                                     |


EX: 
```sql
alter table customers modify customer_name varchar(100) not null;
```

### CONSTRAINT
| **Commands**                                                                                            | **Description**                        | **Example** |
|---------------------------------------------------------------------------------------------------------|----------------------------------------|-------------|
| `CONSTRAINT <name it> PRIMARY KEY (cloumn1, column2, ....)`                                             | setting primary key                    |             |
| `CONSTRAINT <name it> FOREIGN KEY (column1_yourtable, ...) REFERENCES other_table(column1_to_link,...)` | foreign key constraint                 |             |
| `CONSTRAINT <name it> UNIQUE(column1, column2, ......)`                                                 | unique value for column                |             |
| `CONSTRAINT <name_it> CHECK(<condtion to apply on cloumns>)`                                            | like <, >, ==, BETWEEN, IN constraints |             |


### Create Table
```sql
CREATE TABLE table_name 
(<column1 name> DATATYPE null /not null,
 <column2 name> DATATYPE null /not null,
 <column3 name> DATATYPE null /not null,
 CONSTRAINT <your constraint name> CONSTRAINT_TYPE (cloumn1, column2, ....)
);
```

ex: 
```sql
CREATE TABLE suppliers 
(supplier_id INT(10) not NULL,
supplier_nmae VARCHAR(50) not NULL,
contact_name VARCHAR(50),
supplier_mobile VARCHAR(15),
Type VARCHAR(50),
City VARCHAR(50),
CONSTRAINT sup_pk PRIMARY KEY (supplier_id),
CONSTRAINT mobile_un UNIQUE (supplier_mobile),
CONSTRAINT check_city CHECK (City in ('Alex', 'Cairo'))

);

create table products
( product_id int(10) not null,
supplier_id int(10) not null,
price int(6) not null, 
CONSTRAINT product_pk PRIMARY KEY (product_id),
CONSTRAINT fk_supplier_product foreign key (supplier_id) REFERENCES suppliers(supplier_id),
CONSTRAINT price_check CHECK (price BETWEEN 1 and 10000) --there is another way to do it: CHECK(price >= 1 AND price <=10000)
);

```


## Manipulating Data (DML)


| **Commands**                                                                   | **Description**                      | **More Info** |
|--------------------------------------------------------------------------------|--------------------------------------|---------------|
| `INSERT INTO <table name> VLUES(value1, value2,...)`                           | insert into row                      |               |
| `INSERT INTO <table name> (coulmnx, columny, ...) VALUES(valuex, valuey, ...)` | insert into defined columns          |               |
| `UPDATE <table name> SET <column name> = <value> WHERE <condition>`            | update column in rows with condition |               |
| `DELETE FROM <table name>`                                                     | deletes all rows in table            |               |
| `DELETE FROM <table name> WHERE <condtion>`                                    | deletes rows with condition          |               |


### condition
| **symbol**                                          | **Meaning**                               | **Example**           |
|-----------------------------------------------------|-------------------------------------------|-----------------------|
| `<, >, =`                                           |                                           |                       |
| 'AND, OR, NOT'                                      |                                           |                       |
| `<column name> LIKE '<string with wild cards>'`     | matching wild cards of string             | `name LIKE '%Ahmed%'` |
| `<column name> IN (<value1>, <value2>, ....)`       | if column is in set of values             |                       |
| `<column name> IN (SELECT <statment>)`              | if column is in set of values from select |                       |
| `<column name> BETWEEN <min value> AND <max value>` |                                           |                       |

### wild cards
| **Symbol*** | **Description**                                     | **Example**                            |
|-------------|-----------------------------------------------------|----------------------------------------|
| %           | Represents zero or more characters                  | bl% finds bl, black, blue, and blob    |
| _           | Represents a single character                       | h_t finds hot, hat, and hit            |
| []          | Represents any single character within the brackets | h[oa]t finds hot and hat, but not hit  |
| ^           | Represents any character not in the brackets        | h[^oa]t finds hit, but not hot and hat |
| -           | Represents a range of characters                    | c[a-b]t finds cat and cbt              |



Example for `UPDATE`
```sql
UPDATE <table name>
SET <column name> = <value of the column>
WHERE <condtion> -- if WHERE key word does not exist it will update the coumn for all values in table
```

```sql
UPDATE supplier
SET supplier_name = 'Ahmed'
WHERE supplier_id = 100;
```


## Retrieving Data

| **Commands**                                                                                                                 | **Description**                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| `SELECT * FROM <table name>`                                                                                                 | retrieving all table data                                                                                                                               |
| `SELECT * FROM <table name> WHERE <condition`                                                                                | retrieving rows with condition (select)                                                                                                                 |
| `SELECT <columnx>, <cloumny>,... FROM <table name>`                                                                          | retrieving all table data with provided columns  (project)                                                                                              |
| `SELECT <columnx>, <cloumny>,... FROM <table name> WHERE <conditon>`                                                         | retrieving rows with condition with provided columns (select + project)                                                                                 |
| `SELECT <columnx>, <cloumny>,... FROM <table_x>, <table_y>,... WHERE <conditon>`                                             | retrieving rows with condition with provided columns (join+ select + project)                                                                           |
| `SELECT <aggregate function>(<column name or '*' for COUNT>) FROM <table_name>  WHERE <conditon>`                            | gets the aggregate function output from column with condtion                                                                                            |
| `SELECT <aggr_func_x>(<col_name>), <aggr_func_y>(<col_name>),... FROM <table_name> WHERE <conditon>`                         | gets the aggregates function output from column with condtion                                                                                           |
| `SELECT <column_x>,... <aggr_func>(<column_x>),... WHERE <condition> GROUP BY <column_x>`                                    | retrieves a table with (<column_x>, aggregate funciton(<column_x>))  after applying condition                                                           |
| `SELECT <column_x>,... <aggr_func>(<column_x>),... WHERE <condition> GROUP BY <column_x> HAVING <condtion on aggr_func>`     | retrieves a table with (<column_x>, aggregate funciton(<column_x>))  after applying condition on the table and condition on aggregate function (HAVING) |
| `SELECT <col_x>, <col_y>, <col_z> FROM <table_name> WHERE <condtion> OREDR BY <col_x>` <ASC or DESC>                         | retrieves table with columns ordered (ascending or descending of col_x)                                                                                 |
| `SELECT <col_x>, <col_y>, <col_z> FROM <table_name> WHERE <condtion> OREDR BY <col_x>` <ASC or DESC>, <col_y>` <ASC or DESC> | retrieves table with columns ordered (ascending or descending of col_x)  and every row in col_x ordered with (col_y ascending or descending)            |
| `SELECT <columnx>&#124;&#124; '<a word>' &#124;&#124; <cloumny> as <new name>,... FROM <table name>`                                             | concatenate the columns and change the diplay name to <new name>                                                                                        |

Example for `SELECT`
```sql
SELECT <clumnx>, clumny>, .....From <table name>
WHERE <condtion> -- if WHERE key word does not exist it will update the coumn for all values in table
```

```sql
UPDATE supplier
supplier_id, supplier_name
WHERE supplier_id = 100;

```

Example of `SELECT` and `JOIN`
```sql
SELECT <table_x>.<column_name>, <table_y>.<column_name>, ....
FROM <table_x>, <table_y>, <table_z>,....
WHERE <condtions>
```

```sql
SELECT suppliers.supplier_id, supplier_name, product_id, product_name
FROM suppliers, products
WHERE suppliers.supplier_id = products.supplier_id;
```

Example on aggregate function
```sql
SELECT COUNT(*)
FROM products
WHERE NOT City = 'Alex';
```

Example on GROUP BY
```sql
SELECT department_number, COUNT(*)
FROM employees
WHERE sallery > 2000
GROUP BY department_number;
```
Output:
| department_number | COUNT(*) |
|-------------------|----------|
|                 1 |       10 |
|                 2 |        4 |
|                 3 |        9 |
|                 4 |        8 |

Example on GROUP BY and HAVING
```sql
SELECT department_number, COUNT(*)
FROM employees
WHERE sallery > 2000
GROUP BY department_number
HAVING COUNT(*) > 5;
```
Output:
| department_number | COUNT(*) |
|-------------------|----------|
|                 1 |       10 |
|                 3 |        9 |
|                 4 |        8 |


Example on ORDER BY
```sql
SELECT department_number, sallery
FROM employees
WHERE sallery >100
ORDER BY department DESC;
```
Output:
| department_number | salary |
|-------------------|--------|
|                 4 |    200 |
|                 4 |    500 |
|                 4 |    150 |
|                 3 |    800 |
|                 3 |    200 |
|                 1 |    700 |

```sql
SELECT department_number, salary
FROM employees
WHERE sallery >100
ORDER BY department_number DESC, salary ASC;
```
Output:
| department_number | salary |
|-------------------|--------|
|                 4 |    150 |
|                 4 |    150 |
|                 4 |    500 |
|                 3 |    200 |
|                 3 |    800 |
|                 1 |    700 |







# 1.Working with Tables


# 2.Working with Containers


# 3.Working with Data

# 4.Retrieving Data
