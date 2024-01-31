import boto3

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Retrieve the current user_uuid for Tony Quintanilla
response_tony = dynamodb.get_item(
    TableName=table_name,
    Key={
        'pk': {'S': 'USER#Tony Quintanilla'},
        'sk': {'S': 'PROFILE'}
    },
    ProjectionExpression='user_uuid'
)

# Retrieve the current user_uuid for Cassidy Tuck
response_cassidy = dynamodb.get_item(
    TableName=table_name,
    Key={
        'pk': {'S': 'USER#Cassidy Tuck'},
        'sk': {'S': 'PROFILE'}
    },
    ProjectionExpression='user_uuid'
)

# Extract the user_uuid values
user_uuid_tony = response_tony['Item']['user_uuid']['S']
user_uuid_cassidy = response_cassidy['Item']['user_uuid']['S']

# Display the current user_uuid values
print(f"Current user_uuid for Tony Quintanilla: {user_uuid_tony}")
print(f"Current user_uuid for Cassidy Tuck: {user_uuid_cassidy}")
