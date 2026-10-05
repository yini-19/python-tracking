from fastapi import FastAPI

app = FastAPI()

next_id = 1

tasks = {}

@app.get("/tasks")
def all_tasks():
  return list(tasks.values())

@app.get("/tasks/{_id}")
def one_task(task_id):
  return tasks[task_id]

@app.post("/tasks")
def new_task(Title: str, Description: str):
  global next_id
  Done = False
  identifier = next_id
  tasks[identifier] = {"task_id": next_id, "title": Title, "Details": Description, "done": Done}
  next_id += 1
  return tasks[identifier]

@app.put("/tasks/{task_id}")
def edit_task(task_id: int, Title: str, Description: str):
  
  tasks[task_id] ={"task_id": task_id, "title": Title, "Details": Description, "done": tasks[task_id]["done"]}
  return tasks[task_id]

@app.delete("/tasks/{task_id}")
def delete_task(task_id):
  del tasks[task_id]
  return None

