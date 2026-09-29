### Exercise 1
**The /health endpoint**
Caller: its a monitoring tool
Path: GET /health - should return
Response: {"status": "OK"}

**The /about endpoint**
Caller: for any developer that wants to know what my api is about
Path: GET /about
Response: {"name": "Task API", "description": "An API for managing tasks."}

### Exercise 2
1. Browser builds a GET request to /health, with      headers, no body.
2. Uvicorn receives the raw request off the network and hands it to FastAPI.
3. FastAPI matches the request's method and path against your decorator.
4. Your function runs with no input, and returns {"status": "OK"}.
5. FastAPI converts that dictionary to JSON, attaches status 200, and adds headers.
6. Uvicorn sends the response back, and the browser displays the JSON.