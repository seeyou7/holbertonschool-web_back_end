# Personal Data

## Description

This project focuses on handling and protecting Personally Identifiable Information (PII) in data systems. You will learn how to filter and obfuscate sensitive information in logs, securely handle passwords, and connect to databases using environment variables.

## Learning Objectives

By the end of this project, you should be able to:

- Identify examples of Personally Identifiable Information (PII).
- Implement a log filter to obfuscate PII fields.
- Encrypt passwords and verify their validity.
- Authenticate to a database using environment variables.

## Resources

- [What Is PII, non-PII, and Personal Data?](https://www.osano.com/articles/what-is-pii)
- [Logging Documentation](https://docs.python.org/3/library/logging.html)
- [bcrypt Package](https://pypi.org/project/bcrypt/)
- [Logging to Files, Setting Levels, and Formatting](https://docs.python.org/3/howto/logging.html#logging-to-a-file)

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using Python 3.9.
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code should use the `pycodestyle` style (version 2.5).
- All files must be executable.
- The length of your files will be tested using `wc`.
- All modules should have documentation.
- All classes and functions should have documentation with descriptive sentences.
- All functions should be type annotated.

## Project Tasks

### Task 0: Regex-ing

**Objective**: Write a function `filter_datum` that returns the log message obfuscated.

- **Arguments**:
  - `fields`: List of strings representing fields to obfuscate.
  - `redaction`: String representing what the field will be obfuscated with.
  - `message`: String representing the log line.
  - `separator`: String representing the field separator in the log line.
- **Requirements**:
  - Use a regular expression to replace occurrences of certain field values.
  - The function should be less than 5 lines long.
  - Use `re.sub` for substitution with a single regex.

**Example**:

```python
fields = ["password", "date_of_birth"]
messages = [
    "name=John;email=john@example.com;password=secret;date_of_birth=01/01/1990;",
    "name=Jane;email=jane@example.com;password=12345;date_of_birth=02/02/1992;"
]

for message in messages:
    print(filter_datum(fields, '***', message, ';'))


#Task 1: Log Formatter
Objective: Update the RedactingFormatter class to filter values in incoming log records.

#Requirements:
Accept a list of strings fields as a constructor argument.
Implement the format method to use filter_datum.
The format method should be less than 5 lines long.
Example:

#Task 2: Create Logger
Objective: Implement a get_logger function that returns a logging.Logger object configured for user data.

Requirements:
The logger should be named "user_data" and log up to logging.INFO level.
It should not propagate messages to other loggers.
Add a StreamHandler with RedactingFormatter as the formatter.
Create a tuple PII_FIELDS containing the fields considered PII.
Task 3: Connect to Secure Database
Objective: Implement a get_db function to connect securely to a database using environment variables.

Environment Variables:
PERSONAL_DATA_DB_USERNAME (default: "root")
PERSONAL_DATA_DB_PASSWORD (default: "")
PERSONAL_DATA_DB_HOST (default: "localhost")
PERSONAL_DATA_DB_NAME (no default, must be set)
Requirements:
Use the os module to access environment variables.
Use mysql-connector-python to connect to the database.
Task 4: Read and Filter Data
Objective: Implement a main function that retrieves all rows in the users table and displays each row in a filtered format.

Filtered Fields:
-name
-email
-phone
-ssn
-password
-Requirements:
Use get_db to obtain a database connection.
Format each log line using the RedactingFormatter.


#Task 5: Encrypting Passwords
Objective: Implement a hash_password function that hashes a password using bcrypt.

Requirements:
The function should expect a string password and return a salted, hashed password (bytes).
Use bcrypt.hashpw for hashing.


#Task 6: Check Valid Password
Objective: Implement an is_valid function to verify if a password matches a hashed password.

Arguments:
hashed_password: Bytes representing the hashed password.
password: String representing the plaintext password.
#Requirements:
Use bcrypt.checkpw to validate the password.

##Author

Younes SABER