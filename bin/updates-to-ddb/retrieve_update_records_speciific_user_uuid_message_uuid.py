import boto3
from termcolor import colored

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Prompt user for old_user_uuid, new_user_uuid, and message_uuid
old_user_uuid = input("Enter the old user_uuid: ")
new_user_uuid = input("Enter the new user_uuid: ")
message_uuid = input("Enter the message_uuid: ")

# Wait for all three values to be entered
while not (old_user_uuid and new_user_uuid and message_uuid):
    print("Please enter all three values.")

# Define the user_handle
user_handle = 'Ultra-Man'

# Retrieve the item associated with the old_user_uuid and message_uuid
response = dynamodb.scan(
    TableName=table_name,
    FilterExpression='#ou = :old_user_uuid AND #mu = :message_uuid AND #uh = :user_handle',
    ExpressionAttributeNames={
        '#ou': 'user_uuid',
        '#mu': 'message_uuid',
        '#uh': 'user_handle'
    },
    ExpressionAttributeValues={
        ':old_user_uuid': {'S': old_user_uuid},
        ':message_uuid': {'S': message_uuid},
        ':user_handle': {'S': user_handle}
    },
    ProjectionExpression='user_display_name, message, message_group_uuid, pk, message_uuid, user_uuid, sk, user_handle',
    Limit=1
)

# Retrieve the item associated with the old_user_uuid and message_uuid
items = response['Items']

if len(items) == 0:
    print("No record with the specified old_user_uuid, message_uuid, and user_handle was found.")
else:
    print(colored("Record associated with the old_user_uuid and message_uuid:", 'green'))
    print("----------------------------------")
    item = items[0]
    for attr_name in ['user_display_name', 'message', 'message_group_uuid', 'pk', 'message_uuid', 'user_uuid', 'sk', 'user_handle']:
        attr_value = item.get(attr_name)
        if attr_value:
            attr_value = attr_value.get(list(attr_value.keys())[0])
            print(f"{attr_name}: {attr_value}")
    print("----------------------------------")

    # Insert a new record associated with the new_user_uuid and attribute values from the old_user_uuid
    new_record = item.copy()
    new_record['user_uuid'] = {'S': new_user_uuid}

    response = dynamodb.put_item(
        TableName=table_name,
        Item=new_record
    )

    print(colored("\nNew record associated with the new_user_uuid:", 'green'))
    print("----------------------------------")

    for attr_name in ['user_display_name', 'message', 'message_group_uuid', 'pk', 'message_uuid', 'user_uuid', 'sk', 'user_handle']:
        attr_value = new_record.get(attr_name)
        if attr_value:
            attr_value = attr_value.get(list(attr_value.keys())[0])
            print(f"{attr_name}: {attr_value}")
    print("----------------------------------")
