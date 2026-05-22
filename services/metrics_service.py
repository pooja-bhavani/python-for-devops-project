import psutil

def get_system_metrics():

    """
       This API gets system metrics such as CPU usage, memory usage, and disk usage. 
       It also checks if the CPU usage exceeds a defined threshold and returns the system status accordingly.
    """

    cpu_percent = psutil.cpu_percent(interval=1)  # Get CPU usage percentage
    memory_percent = psutil.virtual_memory().percent  # Get memory usage percentage
    disk_percent = psutil.disk_usage('/').percent  # Get disk usage percentage

    cpu_threshold = 10 # Define a threshold for CPU usage

    status = "High CPU" if cpu_percent > cpu_threshold else "Healthy" # Determine system status based on CPU usage

    return {
        "cpu_percent": cpu_percent, # Return the CPU usage percentage
        "memory_percent": memory_percent, # Return the memory usage percentage
        "disk_percent": disk_percent, # Return the disk usage percentage
        "cpu_threshold": cpu_threshold, # Return the CPU usage threshold
        "system_status": status # Return the system status

    }





