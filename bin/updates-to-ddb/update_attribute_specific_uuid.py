import boto3

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Define the user_handle and new_user_uuid
user_handle = 'Ultra-Man'
old_user_uuid = '7fba6d6d-ca3a-4557-b9fd-7b9844b15289'
new_user_uuid = 'f34ded61-7951-45f9-851b-0a151f853f06'

# Query the table to retrieve the item with the matching user_handle
response = dynamodb.scan(
    TableName=table_name,
    FilterExpression='#uh = :user_handle',
    ExpressionAttributeNames={'#uh': 'user_handle'},
    ExpressionAttributeValues={':user_handle': {'S': user_handle}},
    ProjectionExpression='pk'
)

# Update the item with the new_user_uuid and count the number of records updated
items = response['Items']
updated_count = 0
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

if updated_count == 0:
    print("No records were updated.")
else:
    print(f"Number of records updated: {updated_count}")
