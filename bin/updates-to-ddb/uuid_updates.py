import boto3

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Prepare BatchWriteItem Request
request_items = []

# Define updates for specific user_display_name values
updates = {
    'Tony Quintanilla': 'f34ded61-7951-45f9-851b-0a151f853f06',
    'Cassidy Tuck': '53b535ba-864b-447b-a1bc-026a4ddd1f0e'
}

# Update Items
for user_display_name, new_user_uuid in updates.items():
    update_request = {
        'PutRequest': {
            'Item': {
                'user_display_name': {'S': user_display_name},
                'user_uuid': {'S': new_user_uuid}
            }
        }
    }
    request_items.append(update_request)

# Execute BatchWriteItem Request
response = dynamodb.batch_write_item(RequestItems={table_name: request_items})

# Handle Errors
if response.get('UnprocessedItems'):
    print('Some items were not updated successfully:', response['UnprocessedItems'])
else:
    print('All items were updated successfully.')
