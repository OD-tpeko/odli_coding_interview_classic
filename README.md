# Hello and Welcome!

We're thrilled to have you take on this software engineering test as part of our team evaluation process. This test is designed to gauge your software engineering skills in working with databases, git, testing and satisfying real world requirements. 

## Your Task

You will find a Python project waiting for your expertise. Your mission is to implement the following steps:

1. Read To-Do entries from a database.
2. Apply a *due date* to the To-Do entry.
   - Follow the given business requirements.
3. Save it back to the database.

### Business Requirement

You are provided the following business requirements:

- A To-Do entry must have a *due date*
- An *open* To-Do entry may change its *due date*
- A *done* To-Do entry must not change its *due date*

Modifications that would violate these business requirements will explicitly throw an exception.  
Modifications that leaves the entry effectively unchanged will not throw an exception.

## What's Provided

You'll have the following at your disposal:

1. A pre-configured device with the necessary tools and environment ready:
    * Python 3.12
    * VS Code
2. A pre-configured project structure with a template file named `read_modify_write_todos.py`.
3. A pre-defined data model and test cases.
4. A simple database schema filled with sample data, usable with SQLite3.

## Instructions

1. Run the provided `setup.sh` script.
2. Open the provided `src/read_modify_write_todos.py` file.
3. You'll find three functions with placeholders: 
   - `read_todo_entry(connection, id)`
   - `apply_due_on(todo, due_date)`
   - `write_todo_entry(connection, todo)`.
4. Your task is to complete these functions to achieve the business requirement mentioned above.  
   Don't worry about writing perfect code – functionality is key for now.
5. Run the provided testcases (pytest) to validate your implementation.
6. Commit your implementation in Git.

## Additional Information

- The database schema can be viewed in `sql/schema.sql`, the sample data in `sql/seed.sql`.
- You have 1 hour to complete the task.
- You are allowed to use the internet to get the information you need, but the usage of LLMs is prohibited.
- Remember, we're more interested in seeing your problem-solving skills in action than perfect code.

Feel free to reach out if you have any questions during the test. Good luck, and let's see your coding prowess shine!