import boto3
import json
#List the KMS Keys by ID

kms_client = boto3.client('kms', region_name='us-west-1')


#Describe the keys

for key in response['Keys']:
    try:
	    key_info = kms_client.describe_key(KeyId=key['KeyArn'])
		key_id = key_info['KeyMetadata']['KeyId']
		key_arn = key_info['KeyMetadata']['Arn']
		key_state = key_info['KeyMetadata']['KeyState']
		key_description = key_info['KeyMetadata']['Description']
		print('Key id:' + key_id)
		print('Key Arn:' + key_arn)
		print('Key State:' + key_state)
		print('Key Description:' + key_description)
		print('-------------------------------------------')
	except ClientError as e:
	    logging.error(e)
		