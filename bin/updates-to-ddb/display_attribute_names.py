import boto3

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Perform scan operation to retrieve all items
response = dynamodb.scan(TableName=table_name)

# Extract items
items = response['Items']

# Display all attribute names
print("Attribute Names:")
for item in items:
    for attribute_name in item.keys():
        print(attribute_name)
    print()
