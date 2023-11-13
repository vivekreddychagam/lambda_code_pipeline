import boto3
import json

def perform_tasks():
    # Your logic for performing tasks goes here
    print("Performing tasks...")

def put_job_success(job_id):
    codepipeline = boto3.client('codepipeline')
    codepipeline.put_job_success_result(jobId=job_id)

def put_job_failure(job_id, error_message):
    codepipeline = boto3.client('codepipeline')
    codepipeline.put_job_failure_result(
        jobId=job_id,
        failureDetails={'message': error_message, 'type': 'JobFailed'}
    )

def lambda_handler(event, context):
    try:
        # Extract the jobId from the event
        job_id = event['CodePipeline.job']['id']

        # Your logic for handling the CodePipeline event goes here
        perform_tasks()

        # Example: Determine success/failure based on some condition
        success_condition = True

        if success_condition:
            put_job_success(job_id)
        else:
            put_job_failure(job_id, "Custom error message for failure")

    except Exception as e:
        # Handle any unexpected exceptions
        print(f"Error: {str(e)}")
        put_job_failure(job_id, str(e))

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function executed successfully!')
    }
