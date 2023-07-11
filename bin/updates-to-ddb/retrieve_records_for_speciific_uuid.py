import boto3
from termcolor import colored

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Define the user_uuid
user_uuid = 'f34ded61-7951-45f9-851b-0a151f853f06'

# Query the table to retrieve the items with the matching user_uuid
response = dynamodb.scan(
    TableName=table_name,
    FilterExpression='#uu = :user_uuid',
    ExpressionAttributeNames={'#uu': 'user_uuid'},
    ExpressionAttributeValues={':user_uuid': {'S': user_uuid}},
    ProjectionExpression='pk, user_display_name, message, message_group_uuid, message_uuid, user_uuid, user_handle'
)

# Retrieve the items
items = response['Items']

if len(items) == 0:
    print("No records with the specified user_uuid were found.")
else:
    num_records = len(items)
    print(colored(f"Number of records retrieved: {num_records}", 'green'))
    print("----------------------------------")
    for item in items:
        print("Record:")
        for attr_name, attr_value in item.items():
            if attr_value:
                attr_value = attr_value.get(list(attr_value.keys())[0])
                print(f"{attr_name}: {attr_value}")
        print("----------------------------------")
