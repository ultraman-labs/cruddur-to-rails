import boto3
from termcolor import colored
from datetime import datetime

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Prompt the user to enter the user_uuid, pk, and new_user_uuid
print(colored(f"\n--------------------------------------------------------", 'red'))
user_uuid = input("Enter the current user_uuid: ")
pk = input("Enter the pk: ")
new_user_uuid = input("Enter the new user_uuid: ")

# Query the table to retrieve the items with the matching user_uuid and pk
response = dynamodb.scan(
    TableName=table_name,
    FilterExpression='#uu = :user_uuid AND #pk = :pk',
    ExpressionAttributeNames={'#uu': 'user_uuid', '#pk': 'pk'},
    ExpressionAttributeValues={':user_uuid': {'S': user_uuid}, ':pk': {'S': pk}},
    ProjectionExpression='user_display_name, message, message_group_uuid, pk, message_uuid, user_uuid, sk, user_handle'
)

# Retrieve the items associated with the user_uuid and pk
items = response['Items']

if len(items) == 0:
    print("No records with the specified user_uuid and pk were found.")
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
    print(colored(f"\nNumber of records retrieved: {num_records}", 'yellow'))
    print(colored(f"Number of items retrieved: {num_items}", 'yellow'))

    # Insert new records associated with the new_user_uuid and attribute values from the old records
    count_new_records = 0
    for item in items:
        new_record = item.copy()
        new_record['user_uuid'] = {'S': new_user_uuid}

        # Generate unique sort key value
        sort_key = datetime.now().isoformat()

        # Include the sort key attribute
        new_record['sk'] = {'S': sort_key}

        response = dynamodb.put_item(
            TableName=table_name,
            Item=new_record
        )
        count_new_records += 1

    print(colored(f"\nNumber of new records created: {count_new_records}", 'green'))
    print(colored("\nNew records associated with the new_user_uuid:", 'green'))
    print("----------------------------------")

    for item in items:
        for attr_name, attr_value in item.items():
            if attr_value:
                attr_value = attr_value.get(list(attr_value.keys())[0])
                print(f"{attr_name}: {attr_value}")
        print("----------------------------------")
