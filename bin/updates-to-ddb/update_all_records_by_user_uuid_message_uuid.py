import boto3
from termcolor import colored
import time

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Prompt user for old_user_uuid, new_user_uuid, and message_uuid
old_user_uuid = input("Enter the old user_uuid: ")
new_user_uuid = input("Enter the new user_uuid: ")
message_uuid = input("Enter the message_uuid: ")

# Define the user_handle
user_handle = 'Ultra-Man'

# Query the table to retrieve all items with the matching user_handle and message_uuid
response = dynamodb.scan(
    TableName=table_name,
    FilterExpression='#uh = :user_handle AND #mu = :message_uuid',
    ExpressionAttributeNames={'#uh': 'user_handle', '#mu': 'message_uuid'},
    ExpressionAttributeValues={':user_handle': {'S': user_handle}, ':message_uuid': {'S': message_uuid}},
    ProjectionExpression='pk, user_display_name, message, message_group_uuid, message_uuid, user_uuid, user_handle'
)

# Update the items with the new_user_uuid and count the number of records updated
items = response['Items']
num_records = len(items)
updated_count = 0
blink = True
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

    # Retrieve the updated record
    response = dynamodb.get_item(
        TableName=table_name,
        Key={
            'pk': {'S': pk},
            'sk': {'S': 'PROFILE'}
        },
        ProjectionExpression='pk, user_display_name, message, message_group_uuid, message_uuid, user_uuid, user_handle'
    )
    updated_item = response.get('Item')

    # Display the updated record
    if updated_item:
        print("\nUpdated Record:")
        for attr_name, attr_value in updated_item.items():
            if attr_value:
                attr_value = attr_value.get(list(attr_value.keys())[0])
                print(f"{attr_name}: {attr_value}")

    # Wait for a short duration before moving to the next update
    time.sleep(0.5)

# Print the final number of records updated
if updated_count == 0:
    print("No records were updated.")
else:
    message = colored("Number of records updated: ", 'yellow') + colored(str(updated_count), 'green')
    print(message)
