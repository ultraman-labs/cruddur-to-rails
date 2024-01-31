import boto3

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Retrieve the messages for Tony Quintanilla
response = dynamodb.query(
    TableName=table_name,
    IndexName='user_uuid-index',
    KeyConditionExpression='#uu = :user_uuid',
    FilterExpression='#udn = :user_display_name',
    ExpressionAttributeNames={
        '#uu': 'user_uuid',
        '#udn': 'user_display_name',
        '#msg': 'message'
    },
    ExpressionAttributeValues={
        ':user_uuid': {'S': 'f34ded61-7951-45f9-851b-0a151f853f06'},
        ':user_display_name': {'S': 'Tony Quintanilla'}
    },
    ProjectionExpression='#msg'
)

# Extract the messages
items = response['Items']
if items:
    messages = [item['message']['S'] for item in items]

    # Display the retrieved messages
    print("Messages for Tony Quintanilla:")
    for message in messages:
        print(message)
else:
    print("No messages found for Tony Quintanilla.")
