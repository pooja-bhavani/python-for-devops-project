from app.api import app  # Importing the app from the app folder and api.py file
import uvicorn  # Importing uvicorn to run the FastAPI application

if __name__ == "__main__":
    # this uvicorn will create ASGI. ASGI stands for Asynchronous Server Gateway Interface, which is a specification for building asynchronous web servers in Python.
    uvicorn.run(
        "app.api:app", # means to run the app kept inside the app folder and api.py file
        host="0.0.0.0", # if i want the internal team to use this app. we expose it's ip address to
        port=8000, # i want to run this app on port 8000 note don't use 3306 because it's used by mysql database or the big app ports 
        reload=True # this will automatically reload the server when we make changes to the code, which is very useful during development.

    )
