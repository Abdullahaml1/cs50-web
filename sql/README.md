# SQL
pronounced squel


| **Commands**                       | **Description**         | **More Info** |
|------------------------------------|-------------------------|---------------|
| `use <databease name>`             | switch to the database  |               |
| `CREATE DATABASE <databases name>` | create new database     |               |
| `SHOW TABLES`                      | list tables in database |               |
| `show databases`                   | list databases          |               |
| `DROP TABLE <table name>`          | remove table            |               |
| `DESCRIBE <table name>`            | shows  structure table  |               |



`ALTER TABLE <table name>`
| **Commands**                                                                      | **Description**    | **Example**                                                         |
|-----------------------------------------------------------------------------------+--------------------+---------------------------------------------------------------------|
|                                                                                   | rename table       |                                                                     |
| `RENAME  COLUMN <old attribute name> to <new attribute name>`                     | rename attribute   |                                                                     |
| `MODIFY COLUMN <attribute name> <new Type>`                                       | redefines the type | `alter table customers modify customer_name varchar(100) not null;` |
| `ADD (<new attribute name> <type>, <new attribute name> <type>)`                  | add new column     |                                                                     |
| `DROP <column name>`                                                              | remove column      |                                                                     |
| `ADD CONSTRAINT <your constraint name> CONSTRAINT_TYPE (cloumn1,column2,...... )` | add constraint     |                                                                     |


EX: 
```sql
alter table customers modify customer_name varchar(100) not null;
```



**CONSTRAINT**
| **Commands**                                                                                            | **Description**         | **Example** |
|---------------------------------------------------------------------------------------------------------+-------------------------+-------------|
| `CONSTRAINT <name it> PRIMARY KEY (cloumn1, column2, ....)`                                             | setting primary key     |             |
| `CONSTRAINT <name it> FOREIGN KEY (column1_yourtable, ...) REFERENCES other_table(column1_to_link,...)` | foreign key constraint  |             |
| `CONSTRAINT <name it> UNIQUE(column1, column2, ......)`                                                 | unique value for column |             |

# 1.Working with Tables

## Create Table
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
CONSTRAINT mobile_un UNIQUE (supplier_mobile)

);

create table products
( product_id int(10) not null,
supplier_id int(10) not null,
CONSTRAINT product_pk PRIMARY KEY (product_id),
CONSTRAINT fk_supplier_product foreign key (supplier_id) REFERENCES suppliers(supplier_id)
);



```

# 2.Working with Containers


# 3.Working with Data

# 4.Retrieving Data
