import boto3
from datetime import datetime, timezone, timedelta

def get_bucket_info():

    s3_client = boto3.client("s3") # Create an S3 client using boto3 to interact with the AWS S3 service. This creates an S3 API client
    buckets = s3_client.list_buckets()["Buckets"] #Fetch all buckets
    current_time = datetime.now(timezone.utc)
    print(current_time)


    new_buckets = [] # Create an empty list to store the names of the buckets
    old_buckets = []

    for bucket in buckets:  # Iterate through the list of buckets and extract the name of each bucket, then append it to the new_buckets list
        bucket_name = bucket["Name"] # Extract the name of the bucket from the bucket dictionary
        creation_date = bucket["CreationDate"] 
        date_90_days_ago = current_time - timedelta(days=90) 
        
        if creation_date > date_90_days_ago:
            new_buckets.append(bucket_name)
        else:
            old_buckets.append(bucket_name)

    return {
        "total_buckets": len(buckets),
        "new_buckets": len(new_buckets),
        "old_buckets": len(old_buckets),
        "new_buckets_names": new_buckets,
        "old_buckets_names": old_buckets
    }    

   



