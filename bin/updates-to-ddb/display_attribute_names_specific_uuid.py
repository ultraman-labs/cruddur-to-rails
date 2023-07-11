import boto3

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Retrieve item for the specified user_uuid
response = dynamodb.query(
    TableName=table_name,
    IndexName='user_uuid-index',
    KeyConditionExpression='user_uuid = :uuid',
    ExpressionAttributeValues={
        ':uuid': {'S': '7fba6d6d-ca3a-4557-b9fd-7b9844b15289'}
    },
    ProjectionExpression='user_display_name, message, message_group_uuid, pk, message_uuid, user_uuid, sk, user_handle'
)

# Extract the retrieved attributes
items = response['Items']

# Display the retrieved attributes
for item in items:
    print('Retrieved Attributes:')
    for attribute, value in item.items():
        attribute_name = attribute
        attribute_value = value.get(list(value.keys())[0], '')
        print(f'{attribute_name}: {attribute_value}')
    print('---')

print('All attributes were retrieved successfully.')
