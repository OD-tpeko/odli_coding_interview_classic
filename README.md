# Hello and Welcome!

We're thrilled to have you take on this software engineering test as part of our team evaluation process. This test is designed to gauge your software engineering skills in working with databases, git, testing and satisfying real world requirements. 

## Your Task

You will find a Python project waiting for your expertise. Your mission is to implement the following steps:

1. Read To-Do entries from a database.
2. Apply one of two modifications to the To-Do entry.
   - Change *done* status of the entry.
   - Modify *due date* of the entry.
3. Save it back to the database.

### Business Requirement

You are provided the following business requirements:

- A To-Do entry may always be marked as *done*.
- A To-Do entry may always be marked as *not done*.
- A To-Do entry may change its *due date*.
- A *done* To-Do entry may not change its *due date*.

Modifications that would violate these business requirements will silently be ignored.

## What's Provided

You'll have the following at your disposal:

1. A pre-configured device with the necessary tools and environment ready:
    * Python 3.12
    * VS Code
2. A pre-configured project structure with a template file named `read_modify_write_todos.py`.
3. A pre-defined data model and usable commands.
4. A simple database schema, usable with SQLite3.

## Instructions

1. Run the provided `setup.sh` script.
2. Make and checkout a new git branch, which you will be working on.
3. Open the provided `src/read_modify_write_todos.py` file.
4. You'll find three functions with placeholders: 
   - `read_todo_entry(connection, id)`
   - `apply_on_todo_entry(todo, command)`
   - `write_todo_entry(connection, todo)`.
5. Your task is to complete these functions to achieve the business requirement mentioned above.  
   Don't worry about writing perfect code – functionality is key for now.
6. Run the provided testcases to validate your implementation.
7. Commit your implementation to your checked out branch.
8. Merge your checked out branch into the `master` branch.

## Additional Information

- The database schema can be viewed in `sql/schema.sql`.
- You have 1 hour to complete the task.
- You are allowed to use the internet to get the information you need.
- Remember, we're more interested in seeing your problem-solving skills in action than perfect code.

Feel free to reach out if you have any questions during the test. Good luck, and let's see your coding prowess shine!