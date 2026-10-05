### Exercise 1
**Contact app**
* Each "User" will contain ID, name, email, phone no
* There should be a "see everyone" option as well as "see a contact", "add contact", "update contact", "delete contact"
------------------------
|Role| Method | Path
-------------------------------
  | "see everyone"     | GET method    | `/users`           |
  -----------------
  | "see a contact"    | GET method    | `/users/{user_id}` |
  ----------------
  | "add contact"      | POST method   | `/users`           |
  --------------
  | "update contact"   | PUT method    | `/users/{user_id}` |
  --------------
  | "remove contact"   | DELETE method | `/users/{user_id}` |
  -----------------------------------------

### Exercise 2

* Each task should have an 'task_id' field, a 'Title' field, a 'description' field, and a 'done' field
* Five actions that users actions that users can take:
-------------------
Action  |  Method  |  Path
-------------------
  1. "see all tasks" |  GET  | `/tasks`  |  a list of all the tasks
  2. "see one particular task"  |  GET  |  `/tasks/{task_id}`  | a particular task object
  3. "create a task"  |  POST  |  `/tasks`  |  the task object just created and a created status 
  4. "edit a task"  |  PUT  |  `/tasks/{task_id}`  |  the task object just updated and a success meesage
  5. "delete task"  |  DELETE  |  `/tasks/{task_id}`  |  a success message for delete
