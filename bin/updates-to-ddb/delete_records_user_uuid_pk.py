import boto3
from termcolor import colored

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Prompt the user to enter the user_uuid and pk
user_uuid = input("Enter the user_uuid: ")
pk = input("Enter the pk: ")

# Query the table to retrieve the items with the matching user_uuid and pk
response = dynamodb.scan(
    TableName=table_name,
    FilterExpression='#uu = :user_uuid AND #pk = :pk',
    ExpressionAttributeNames={'#uu': 'user_uuid', '#pk': 'pk'},
    ExpressionAttributeValues={':user_uuid': {'S': user_uuid}, ':pk': {'S': pk}},
    ProjectionExpression='message, sk, user_uuid, user_handle, pk, user_display_name, message_uuid'
)

# Retrieve the items associated with the user_uuid and pk
items = response['Items']

if len(items) == 0:
    print("No records with the specified user_uuid and pk were found.")
else:
    num_records = len(items)
    num_items = sum(len(item) for item in items)
    print(f"Number of records retrieved: {num_records}")
    print(f"Number of items retrieved: {num_items}")

    delete_confirmation = input("Do you want to delete the retrieved records? (yes/no): ")

    if delete_confirmation.lower() == 'yes':
        count_deleted_records = 0
        for item in items:
            response = dynamodb.delete_item(
                TableName=table_name,
                Key={
                    'pk': item['pk'],
                    'sk': item['sk']
                }
            )
            count_deleted_records += 1

        print(f"Number of records deleted: {count_deleted_records}")
    else:
        print("Deletion canceled by user.")
