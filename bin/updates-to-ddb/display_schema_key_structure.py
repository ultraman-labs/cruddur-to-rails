import boto3

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Retrieve table description
response = dynamodb.describe_table(TableName=table_name)

# Extract table schema
table_description = response['Table']
attribute_definitions = table_description['AttributeDefinitions']
key_schema = table_description['KeySchema']

# Display table schema
print("Attribute Definitions:")
for attribute in attribute_definitions:
    print(attribute)

print("\nKey Schema:")
for key in key_schema:
    print(key)