from fastapi import APIRouter, HTTPException  # Importing APIRouter and HTTPException from FastAPI

from services.aws_service import get_bucket_info


router = APIRouter() # Create an APIRouter instance to define routes for the metrics endpoints

@router.get("/s3", status_code=200) # Define a GET endpoint at the path "/metrics"
def get_buckets(): # Define a function that will be called when the endpoint is accessed. basically giving a name to api

    try:
        buckets_info = get_bucket_info() # Call the get_bucket_info function to retrieve bucket information
        return buckets_info
    except:
        raise HTTPException(
            status_code=500, # If there is an error while retrieving the metrics, raise an HTTPException with a status code of 500 (Internal Server Error)
            detail="Internal Server Error" # Provide a detail message for the exception
        )
