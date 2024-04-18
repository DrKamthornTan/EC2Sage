import boto3
import requests
import time

# Specify the ARN of the SageMaker Notebook instance
notebook_instance_arn = 'arn:aws:sagemaker:ap-southeast-2:888905897052:notebook-instance/mergeMM'

# Create a SageMaker client
sagemaker_client = boto3.client('sagemaker')

# Start the notebook instance
response = sagemaker_client.start_notebook_instance(NotebookInstanceName=notebook_instance_arn)

# Check the status of the notebook instance
status = response['NotebookInstanceStatus']
print(f"Notebook instance status: {status}")

# Wait until the notebook instance is in the 'InService' state
while status != 'InService':
    response = sagemaker_client.describe_notebook_instance(NotebookInstanceName=notebook_instance_arn)
    status = response['NotebookInstanceStatus']
    print(f"Notebook instance status: {status}")
    
    if status != 'InService':
        # Wait for a few seconds before checking the status again
        time.sleep(5)

# Notebook instance is now in the 'InService' state, you can proceed to call your program

# ... Call your program or execute desired code on the SageMaker Notebook instance ...

# Stop the notebook instance once you're done
sagemaker_client.stop_notebook_instance(NotebookInstanceName=notebook_instance_arn)
print("Notebook instance stopped.")