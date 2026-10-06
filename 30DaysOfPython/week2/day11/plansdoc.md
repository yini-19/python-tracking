**Exercise 1**
* searched_word should return all similar results
* searched_word is narrowing t a group. it could match more than one task at atime
* searched_word is query based. it is going to narrow down a collection
* parameter = keyword
* keyword is a string
* /tasks
* /tasks?keyword=searched_word
* this is a GET method
* should return a list of tasks having similar words to the searched_word
* GET /tasks?keyword=searched_word returns a list of words that are similar to searched_word

**Exercise 2**
* the application will crash or slow down the response significantly
* instead of asking for all tasks, the caller can ask for just a chunk of the the tasks
* limit - integer
* skip - integer
* skip = 20, limit = 10 tasks
* GET /tasks?keyword=searched_word&skip=20&limit=10
* default limit = no limit, default skip = 0
