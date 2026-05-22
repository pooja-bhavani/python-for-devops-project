from fastapi import APIRouter, HTTPException  # Importing APIRouter and HTTPException from FastAPI

from services.metrics_service import get_system_metrics

router = APIRouter() # Create an APIRouter instance to define routes for the metrics endpoints

@router.get("/metrics", status_code=200) # Define a GET endpoint at the path "/metrics"
def get_metrics(): # Define a function that will be called when the endpoint is accessed

    try:
        metrics = get_system_metrics() # Call the get_system_metrics function to retrieve system metrics
        return metrics
    except:
        raise HTTPException(
            status_code=500, # If there is an error while retrieving the metrics, raise an HTTPException with a status code of 500 (Internal Server Error)
            detail="Internal Server Error" # Provide a detail message for the exception
        )

