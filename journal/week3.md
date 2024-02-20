## Helpful Docker commands

```bash
docker ps

or

docker ps -a
```
This command shows a list of all running containers, their IDs, images, command being executed, creation time, status, ports, and name. The variation with the option **-a**, shows all containers, including those that are not currently running. In the context of the Docker command docker ps, the ps stands for **"process status".**


## Docker Commands with PSQL

To connect to the 'cruddur' database in PostgreSQL, you can use the **\c** command followed by the name of the database.
Here's how you do it:

*1.* First, ensure you are in the PostgreSQL command line interface. You can access it using the Docker command:

```bash
docker exec -it cruddur-to-rails-db-1 psql -U postgres
```
After connecting, at the prompt, enter the following command:
```psql
\c cruddur
```


*1.1* You can also access (outside of the Docker PostgreSQL container) with the command:

```bash
psql postgresql://postgres:password@127.0.0.1:5432/cruddur
```
If the response is:

```bash
psql: error: connection to server at "127.0.0.1", port 5432 failed: FATAL:  database "cruddur" does not exist
```
Then the 'cruddur' database needs to be created. This can be done via Rails.

```bash
rails db:create
```

If needed, establishing a connection to Postgress is done with the command:

```bash
psql -U postgres -h localhost
```


*2.* To list all databases, you should use the command below. This command displays the databases along with their owners, encoding, collation, ctype, and access privileges. This is how you can get an overview of all the databases present in your PostgreSQL instance.

```sql
\l or \list
```


*3.* Once in the PostgreSQL CLI, connect to the 'cruddur' database by executing:

```sql
\c cruddur
```
Now that you're connected to the 'cruddur' database in PostgreSQL, here are some common commands you can use to explore and interact with the database:

```sql
\dt                            List Tables
\d table_name                  Describe a table
SELECT * FROM table_name;      Query data
\du                            List Users and Their Roles
\s                             View Query History
SELECT current_database();     Show Current Database

CREATE TABLE new_table_name (             Create a New Table
    column1_name column1_datatype,
    column2_name column2_datatype,
    ...
);


INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);           Insert Data: To insert data into a table:


UPDATE table_name SET column = value WHERE condition;                                  Update Data: To update existing data:


DELETE FROM table_name WHERE condition;                                                Delete Data: To delete data from a table:

```