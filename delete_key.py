import boto3


kms_client = boto3.client('kms', region_name='us-west-1')
response = kms_client.schedule_key_deletion(
    KeyId='e35424cf-bbd6-4ef5-8567-1eee9f981c8d',
    PendingWindowInDays=7
)
print(response)


			
