import boto3
from termcolor import colored
from datetime import datetime

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Prompt the user to enter the message_uuid
message_uuid = input("Enter the message_uuid: ")

# Query the table to retrieve the items with the matching message_uuid
response = dynamodb.scan(
    TableName=table_name,
    FilterExpression='#mu = :message_uuid',
    ExpressionAttributeNames={'#mu': 'message_uuid'},
    ExpressionAttributeValues={':message_uuid': {'S': message_uuid}},
    ProjectionExpression='pk, user_display_name, message, message_group_uuid, message_uuid, user_uuid, user_handle'
)

# Retrieve the items associated with the message_uuid
items = response['Items']

if len(items) == 0:
    print("No records with the specified message_uuid were found.")
else:
    num_records = len(items)
    num_items = sum(len(item) for item in items)
    print(colored("\nCurrent record associated with the message_uuid:", 'green'))
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

    # Retrieve the values associated with the current user_uuid
    current_user_uuid = items[0]['user_uuid']['S']
    user_handle = items[0]['user_handle']['S']
    user_display_name = items[0]['user_display_name']['S']
    message = items[0]['message']['S']
    pk = items[0]['pk']['S']

    # Prompt the user to enter the new_user_uuid
    new_user_uuid = input("Enter the new user_uuid: ")

  # Generate unique sort key value
    sort_key = datetime.now().isoformat()

    # Create a new record associated with the new_user_uuid and the attribute values from the current record
    new_record = {
        'user_handle': {'S': user_handle},
        'user_display_name': {'S': user_display_name},
        'user_uuid': {'S': new_user_uuid},
        'message': {'S': message},
        'pk': {'S': pk},
        'message_uuid': {'S': message_uuid},
        'sk': {'S': sort_key}  # Include the sort key attribute
    }

    # Insert the new record into the table
    response = dynamodb.put_item(
        TableName=table_name,
        Item=new_record
    )

    print(colored("\nNew record associated with the new_user_uuid:", 'green'))
    print("----------------------------------")
    for attr_name, attr_value in new_record.items():
        if attr_value:
            attr_value = attr_value.get(list(attr_value.keys())[0])
            print(f"{attr_name}: {attr_value}")
    print("----------------------------------")
