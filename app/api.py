from fastapi import FastAPI  # Importing fastAPI class
from routers import metrics, aws

app = FastAPI(       # creating object of FastAPI class
    title="Internal DevOps Utilities API",         # means what is the title of our API application
    description="This is a Internal API utilities App for monitoring metrics, AWS usage, Log Analysis, etc.",  # description of our API application
    version="1.0.0", 
    docs_url="/docs",
    redoc_url="/redocs"
    
) 


@app.get("/")  # defining a GET endpoint at the path "/"
def hello_world():  # defining a function that will be called when the endpoint is accessed
    """
    Returns a simple "Hello, World!" message.      # This is a basic endpoint to verify that the API is working correctly.
    """
    return {"message": "Hello, World! This is DevOps utilities API "} # This line returns a JSON response with a key "message" and the value "Hello, World!" when the endpoint is accessed.

app.include_router(metrics.router) #  By including this router, we can access the metrics endpoints defined in the metrics.py file.
app.include_router(aws.router, prefix="/aws")