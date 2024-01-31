import boto3

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Perform scan operation to retrieve all items
response = dynamodb.scan(TableName=table_name)

# Extract items
items = response['Items']

# Create a set to store unique attribute names
attribute_names = set()

# Collect all attribute names
for item in items:
    attribute_names.update(item.keys())

# Display all attribute names
print("Attribute Names:")
for attribute_name in attribute_names:
    print(attribute_name)
