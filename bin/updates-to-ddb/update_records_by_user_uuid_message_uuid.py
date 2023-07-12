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

# Define the user_handle
user_handle = 'Ultra-Man'

# Wait for all three values to be entered
while not (old_user_uuid and new_user_uuid and message_uuid):
    print("Please enter all three values.")

# Retrieve the items associated with the old_user_uuid
response = dynamodb.scan(
    TableName=table_name,
    FilterExpression='#ou = :old_user_uuid AND #nu = :new_user_uuid AND #mu = :message_uuid AND #uh = :user_handle',
    ExpressionAttributeNames={
        '#ou': 'user_uuid',
        '#nu': 'new_user_uuid',
        '#mu': 'message_uuid',
        '#uh': 'user_handle'
    },
    ExpressionAttributeValues={
        ':old_user_uuid': {'S': old_user_uuid},
        ':new_user_uuid': {'S': new_user_uuid},
        ':message_uuid': {'S': message_uuid},
        ':user_handle': {'S': user_handle}
    },
    ProjectionExpression='user_display_name, message, message_group_uuid, pk, message_uuid, user_uuid, sk, user_handle'
)

# Retrieve the items associated with the old_user_uuid
items = response['Items']

if len(items) == 0:
    print("No records with the specified old_user_uuid, new_user_uuid, message_uuid, and user_handle were found.")
else:
    print("Records associated with the old_user_uuid:")
    print("----------------------------------")
    for item in items:
        print("Record:")
        for attr_name, attr_value in item.items():
            if attr_value:
                attr_value = attr_value.get(list(attr_value.keys())[0])
                print(f"{attr_name}: {attr_value}")
        print("----------------------------------")

    # Update the items to be associated with the new_user_uuid
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

    # Retrieve the items associated with the new_user_uuid
    response = dynamodb.scan(
        TableName=table_name,
        FilterExpression='#nu = :new_user_uuid AND #mu = :message_uuid AND #uh = :user_handle',
        ExpressionAttributeNames={
            '#nu': 'user_uuid',
            '#mu': 'message_uuid',
            '#uh': 'user_handle'
        },
        ExpressionAttributeValues={
            ':new_user_uuid': {'S': new_user_uuid},
            ':message_uuid': {'S': message_uuid},
            ':user_handle': {'S': user_handle}
        },
        ProjectionExpression='user_display_name, message, message_group_uuid, pk, message_uuid, user_uuid, sk, user_handle'
    )

    # Retrieve the updated items associated with the new_user_uuid
    updated_items = response['Items']

    if len(updated_items) > 0:
        print("\nRecords associated with the new_user_uuid:")
        print("----------------------------------")
        for item in updated_items:
            print("Record:")
            for attr_name, attr_value in item.items():
                if attr_value:
                    attr_value = attr_value.get(list(attr_value.keys())[0])
                    print(f"{attr_name}: {attr_value}")
            print("----------------------------------")
    else:
        print("No records were updated.")
