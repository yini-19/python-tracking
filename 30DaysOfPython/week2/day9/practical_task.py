from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def check_health():
    health_status = {
        "status": "OK"
    }
    return health_status

@app.get("/about")
def print_about():
    about_info = {
        "name": "Task API", 
        "description": "An API for managing tasks."
    }
    return about_info