import boto3
from termcolor import colored
import time

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Prompt user for old_user_uuid, new_user_uuid, message_uuid, and number of records to update
old_user_uuid = input("Enter the old user_uuid: ")
new_user_uuid = input("Enter the new user_uuid: ")
message_uuid = input("Enter the message_uuid: ")
num_records = int(input("Enter the number of records to update: "))

# Define the user_handle
user_handle = 'Ultra-Man'

# Query the table to retrieve the specified number of items with the matching user_handle and message_uuid
response = dynamodb.scan(
    TableName=table_name,
    FilterExpression='#uh = :user_handle AND #mu = :message_uuid',
    ExpressionAttributeNames={'#uh': 'user_handle', '#mu': 'message_uuid'},
    ExpressionAttributeValues={':user_handle': {'S': user_handle}, ':message_uuid': {'S': message_uuid}},
    ProjectionExpression='pk',
    Limit=num_records
)

# Update the items with the new_user_uuid and count the number of records updated
items = response['Items']
updated_count = 0
blink = True
while items and updated_count < num_records:
    for item in items:
        pk = item['pk']['S']
        response = dynamodb.update_item(
            TableName=table_name,
            Key={
                'pk': {'S': pk},
                'sk': {'S': 'PROFILE'}
            },
            UpdateExpression='SET user_uuid = :new_uuid',
            ExpressionAttributeValues={':new_uuid': {'S': new_user_uuid}}
        )
        updated_count += 1

    # Clear the console output
    print("\033[H\033[J")

    # Display blinking "PROCESSING" message
    if blink:
        print(colored("PROCESSING", 'yellow', attrs=['blink']))
    else:
        print("PROCESSING")

    blink = not blink

    # Wait for a short duration to simulate blinking effect
    time.sleep(0.5)

    # Query the table again to check if there are more items
    response = dynamodb.scan(
        TableName=table_name,
        FilterExpression='#uh = :user_handle AND #mu = :message_uuid',
        ExpressionAttributeNames={'#uh': 'user_handle', '#mu': 'message_uuid'},
        ExpressionAttributeValues={':user_handle': {'S': user_handle}, ':message_uuid': {'S': message_uuid}},
        ProjectionExpression='pk',
        Limit=num_records - updated_count
    )
    items = response['Items']

# Print the final number of records updated
if updated_count == 0:
    print("No records were updated.")
else:
    message = colored("Number of records updated: ", 'yellow') + colored(str(updated_count), 'green')
    print(message)
