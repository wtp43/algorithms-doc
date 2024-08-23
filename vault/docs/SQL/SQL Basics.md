# SQL

### Data Types
- BIGINT, INT, MEDIUMINT, SMALLINT, TINYINT
- DOUBLE, FLOAT, DECIMAL
	- double and float are not as precise as decimal
- CHAR: suitable for fixed text
- VARCHAR(45): each item in the column can store 45 characters
- TEXT, LONGTEXT: text data whose maximum length is unknown
- DATE, MONTH, YEAR, DATETIME, TIMESTAMP
	- To query the year from a date in postgres do: `SELECT date_part('year', now())`
- NULL
- RANGE
	- `'(30, 35]':: int4range`
	- `'[9:30, 12:00)'::timerange`
	- `'[2022-05-02, 2022-06-01]'::daterange`
	- can be unbounded: `'[5,)`

### Column Attribute Functions
- NOT NULL
- AUTO_INCREMENT or SERIAL in postgres
- DEFAULT: default value

### Functions
- DELETE FROM
- INSERT INTO
### WHERE
#### Range conditions
- IN, BETWEEN, LIKE
- % is wildcard in LIKE, to match one character, use `_`

```sql
SELECT * FROM table WHERE id IN (1, 3);
SELECT * FROM table WHERE id BETWEEN 1 AND 3
SELECT * FROM table WHERE name LIKE '%c%'
```

### IF (MYSql), CASE(Postgres)
```sql
IF(condition, value_if_true, value_if_false)
CASE
	WHEN bool THEN 1
	ELSE 0
END
```

### COALESCE
- returns the first of its arguments that is not null
`SELECT COALESCE(SUM(x), 0)`
### RANGE

### JSON
- `->` operator pulls the value out as json (preserving the type of the field)
- `->>` operator gets it as text

### UPDATE
```python
UPDATE table
SET col1 = val1,
	col2 = val2
WHERE condition;
# or use case in val1
# optionally return the updated rows
RETURNING *
RETURNING * | output_expression AS output_name
```


### Auxiliary SELECT
- DISTINCT
- LIMIT 
- OFFSET:skip first x items
- ORDER BY
- GROUP BY: supports aggregate function statements
	- A queried column must also be in the group by

- pagination can be done with LIMIT and OFFSET
```sql
SELECT COUNT(*) AS c
FROM table
GROUP BY c

SELECT DISTINCT id
from views
```
#### DISTINCT vs GROUP BY
https://stackoverflow.com/questions/4477552/mysql-what-is-the-difference-between-group-by-and-distinct
- use DISTINCT if no aggregate functions are queried

### CURSOR Pagination
> Continue at the cursor

```sql
#MYSQL
SET @lastID = 5;

SELECT * FROM employees
WHERE id > @lastEmployeeID
ORDER BY id asc, name desc?<
LIMIT 5;


#POSTGRES

```

- MYSql: 
### Aggregate Functions
>Aggregate functions are not allowed in WHERE 
>Aggregate functions are allowed in HAVING, ORDER BY
https://leetcode.com/problems/sales-person/description/
- COUNT
- SUM
- AVG
- MIN,MAX
	- can be used to get the earliest or latest date

Example:

| date_id   | make_name | lead_id | partner_id |
| --------- | --------- | ------- | ---------- |
| 2020-12-8 | toyota    | 0       | 1          |
| 2020-12-8 | toyota    | 1       | 0          |
| 2020-12-8 | toyota    | 1       | 2          |
| 2020-12-7 | toyota    | 0       | 2          |
| 2020-12-7 | toyota    | 0       | 1          |
| 2020-12-8 | honda     | 1       | 2          |
| 2020-12-8 | honda     | 2       | 1          |
| 2020-12-7 | honda     | 0       | 1          |
| 2020-12-7 | honda     | 1       | 2          |
| 2020-12-7 | honda     | 2       | 1          |

Output:

| date_id    | make_name | unique_leads | unique_partners |
| ---------- | --------- | ------------ | --------------- |
| 2020-12-07 | honda     | 3            | 2               |
| 2020-12-07 | toyota    | 1            | 2               |
| 2020-12-08 | honda     | 2            | 2               |
| 2020-12-08 | toyota    | 2            | 3               |

```sql
SELECT
    date_id,
    make_name,
    COUNT(DISTINCT lead_id) AS unique_leads,
    COUNT(DISTINCT partner_id) AS unique_partners
FROM
    DailySales
GROUP BY date_id, make_name;
```

#### Querying with MAX/MIN
Example: Get all records that are not the minimum or maximum
```sql
WITH q AS
    (SELECT activity, COUNT(DISTINCT id) AS user_cnts
    FROM Friends
    GROUP BY activity
    )
SELECT activity
from q 
WHERE user_cnts NOT IN (SELECT MAX(user_cnts) FROM q)
AND user_cnts NOT IN (SELECT MIN(user_cnts) FROM q)
```


### Subquery
In the actual database system, a table often has dozens of columns. If `JOIN` is used to combine tables according to certain conditions, it may cause many redundant columns to be fetched.
```sql
SELECT email FROM 
(
  select email, count(email) as num
  from Person
  group by email
) as subquery_name
where num > 1;

# Equals: returns only 1 record
SELECT * FROM `new_schema`.`orders`
WHERE user_id = (
  SELECT id FROM `new_schema`.`users`
  WHERE name LIKE '%j%'
);

# Contains: can return multiple records
SELECT * FROM `new_schema`.`orders`
WHERE user_id IN (
  SELECT id FROM `new_schema`.`users`
  WHERE name LIKE '%j%'
);
```

### JOINS
- LEFT JOIN
	- all columns from both tables are displayed
	- left table is treated as the main table
	- all records from the left are included
	- if any specific record of the main table does not include any attached table records, the values of the columns in the attached table will be set to NULL
- RIGHT JOIN
	- opposite of left join
- INNER JOIN
	- returns intersection
- FULL OUTER JOIN
	- returns union
Example:
```sql
A    B
-    -
1    3
2    4
3    5
4    6

INNER JOIN
select * from a INNER JOIN b on a.a = b.b;

a | b
--+--
3 | 3
4 | 4

LEFT OUTER JOIN
select * from a LEFT OUTER JOIN b on a.a = b.b;

a |  b
--+-----
1 | null
2 | null
3 |    3
4 |    4

RIGHT OUTER JOIN
select * from a RIGHT OUTER JOIN b on a.a = b.b;

a    |  b
-----+----
3    |  3
4    |  4
null |  5
null |  6


FULL OUTER JOIN
select * from a FULL OUTER JOIN b on a.a = b.b;

 a   |  b
-----+-----
   1 | null
   2 | null
   3 |    3
   4 |    4
null |    6
null |    5
```



## Foreign Key, Transaction, ACID, Index, User Privilege
https://leetcode.com/explore/learn/card/sql-language/685/intermediate-sql/4347/

## MISC/Common Mistakes

### Distinction between AND and WHERE when Joining Tables
https://leetcode.com/problems/sales-person/description/
```sql
select o.sales_id
from Orders as o LEFT JOIN Company as c on c.com_id = o.com_id
	and c.name = 'RED'

VS

where c.name = 'RED'
```
- Since a LEFT JOIN is used, if c.name is not 'RED', a default NULL value is set
- Using WHERE will actually filter the records to only include c.name = 'RED'
- Alternatively, using AND with an INNER JOIN will also produce the intended query