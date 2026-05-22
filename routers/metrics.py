from fastapi import APIRouter, HTTPException  # Importing APIRouter and HTTPException from FastAPI

from services.metrics_service import get_system_metrics

router = APIRouter() 

@router.get("/metrics", status_code=200) # Define a GET endpoint at the path "/metrics"
def get_metrics(): 

    try:
        metrics = get_system_metrics() 
        return metrics
    except:
        raise HTTPException(
            status_code=500, 
            detail="Internal Server Error" 
        )

