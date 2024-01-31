import boto3
import json

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Perform scan operation to retrieve all items
response = dynamodb.scan(TableName=table_name)

# Extract items
items = response['Items']

# Display item details
print("Table Items:")
for item in items:
    formatted_item = {}
    for attribute, value in item.items():
        formatted_item[attribute] = list(value.values())[0]
    print(json.dumps(formatted_item, indent=4))
    print()
