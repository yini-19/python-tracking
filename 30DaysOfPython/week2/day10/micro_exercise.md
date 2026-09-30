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
