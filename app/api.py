from fastapi import FastAPI 
from routers import metrics, aws

app = FastAPI(      
    title="Internal DevOps Utilities API",        
    description="This is a Internal API utilities App for monitoring metrics, AWS usage, Log Analysis, etc.",  
    version="1.0.0", 
    docs_url="/docs",
    redoc_url="/redocs"
    
) 

@app.get("/") # define a route that handles HTTP GET requests at the root URL path
def hello_world(): 
    """
    Returns a simple "Hello, World!" message.      # This is a basic endpoint to verify that the API is working correctly.
    """
    return {"message": "Hello, World! This is DevOps utilities API "} 
    
app.include_router(metrics.router) 
app.include_router(aws.router, prefix="/aws")
