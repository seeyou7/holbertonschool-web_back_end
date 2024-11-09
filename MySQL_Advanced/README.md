# MySQL Advanced

![Flowchart of MySQL Advanced Tasks](images/flowchart.webp)

This repository contains a collection of advanced MySQL scripts designed to help you master SQL techniques such as table creation with constraints, indexing for optimization, triggers, stored procedures, functions, and views. Each script addresses specific data-handling requirements and simulates real-world applications, helping you learn to write efficient, maintainable SQL code for complex database solutions.

---

## Scripts

### 0 - Unique Users Table
Creates a `users` table with unique constraints on `email` and other requirements for user data. This script ensures data integrity by enforcing uniqueness and setting constraints directly at the database level.

### 1 - Users Table with Country Enum
Expands the `users` table by adding a `country` column with an enumeration (`ENUM`) of allowed values. This enforces a limited selection of countries (`US`, `CO`, `TN`), ensuring consistent data and simplifying queries that filter by country.

### 2 - Rank Bands by Country Fans
Aggregates the fan count by band origin and orders them by popularity. This query is useful in data analysis, where you want to rank categories based on the sum of a specific attribute, such as popularity.

### 3 - Lifespan of Glam Rock Bands
Lists bands whose main style includes "Glam rock" and calculates their lifespan (years active) based on their `formed` and `split` years. It showcases how to handle NULL values and compute derived data dynamically.

### 4 - Trigger to Decrease Item Quantity
Creates a trigger, `decrease_order`, which automatically reduces the quantity of an item in inventory after a new order is added. This automation is essential in inventory management systems to maintain accurate stock levels.

### 5 - Trigger to Reset Email Validation
Defines a trigger, `reset_valid_email`, that resets the `valid_email` field if a user updates their email address. This ensures that any change to a user’s email address requires revalidation, maintaining data integrity.

### 6 - Stored Procedure to Add Bonus
Implements a stored procedure, `AddBonus`, to add a new correction (or bonus) for a student based on their project. This automation allows seamless entry of bonus scores and ensures project consistency by creating a project entry if it doesn’t exist.

### 7 - Stored Procedure to Compute Average Score
Creates a stored procedure, `ComputeAverageScoreForUser`, that calculates and stores a user's average score based on their corrections. This procedure is helpful in educational applications where average scores need to be displayed or analyzed.

### 8 - Index on First Letter of Name
Creates an index, `idx_name_first`, on the first character of the `name` column in the `names` table. This partial index optimizes queries that search based on the first letter, improving search performance for large datasets.

### 9 - Composite Index on First Letter and Score
Builds a composite index, `idx_name_first_score`, on the first character of `name` and `score`. This index is particularly useful for applications needing fast searches based on the initial letter and score ranges, enhancing query speed significantly.

### 10 - Safe Division Function
Defines a function, `SafeDiv`, that divides two numbers but returns `0` if the divisor is `0`. This is essential for applications where dividing by zero could result in errors, ensuring safe, error-free calculations.

### 11 - View for Students Needing Meetings
Creates a view, `need_meeting`, listing students with a score under 80 and either no recent meeting or no meeting in the last month. This view simplifies tracking students who may require academic support, making it easier to manage meeting schedules.

---

These scripts offer hands-on practice with MySQL features essential for building robust, scalable, and optimized database applications.

## Author

Developed by Younes SABER [https://github.com/seeyou7]
