import boto3
from termcolor import colored

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Prompt the user to enter the user_uuid and message_uuid
user_uuid = input("Enter the user_uuid: ")
message_uuid = input("Enter the message_uuid: ")

# Query the table to retrieve the items with the matching user_uuid and message_uuid
response = dynamodb.scan(
    TableName=table_name,
    FilterExpression='#uu = :user_uuid AND #mu = :message_uuid',
    ExpressionAttributeNames={'#uu': 'user_uuid', '#mu': 'message_uuid'},
    ExpressionAttributeValues={':user_uuid': {'S': user_uuid}, ':message_uuid': {'S': message_uuid}},
    ProjectionExpression='pk, user_display_name, message, message_group_uuid, message_uuid, user_uuid, user_handle'
)

# Retrieve the items
items = response['Items']

if len(items) == 0:
    print("No records with the specified user_uuid and message_uuid were found.")
else:
    num_records = len(items)
    num_items = sum(len(item) for item in items)
    print("----------------------------------")
    for item in items:
        print("Record:")
        for attr_name, attr_value in item.items():
            if attr_value:
                attr_value = attr_value.get(list(attr_value.keys())[0])
                print(f"{attr_name}: {attr_value}")
        print("----------------------------------")
    print(colored(f"\nNumber of records retrieved: {num_records}", 'green'))
    print(colored(f"Number of items retrieved: {num_items}", 'green'))
