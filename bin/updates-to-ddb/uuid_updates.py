import boto3

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Define updates for specific user_display_name values
updates = {
    'Tony Quintanilla': 'f34ded61-7951-45f9-851b-0a151f853f06',
    'Cassidy Tuck': '53b535ba-864b-447b-a1bc-026a4ddd1f0e'
}

# Update Items
for user_display_name, new_user_uuid in updates.items():
    update_expression = 'SET user_uuid = :new_uuid'
    expression_attribute_values = {':new_uuid': {'S': new_user_uuid}}
    
    response = dynamodb.update_item(
        TableName=table_name,
        Key={
            'pk': {'S': f'USER#{user_display_name}'},
            'sk': {'S': 'PROFILE'}
        },
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values
    )
    print(f"Item updated for user_display_name: {user_display_name}")

print('All items were updated successfully.')
