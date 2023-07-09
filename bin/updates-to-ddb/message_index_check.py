import boto3

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Check if 'message-index' exists in the table
response = dynamodb.describe_table(
    TableName=table_name
)

# Get the list of global secondary indexes
global_secondary_indexes = response['Table'].get('GlobalSecondaryIndexes', [])

# Check if 'message-index' is among the global secondary indexes
index_exists = any(index['IndexName'] == 'message-index' for index in global_secondary_indexes)

# Print the result
if index_exists:
    print("'message-index' exists in the table.")
else:
    print("'message-index' does not exist in the table.")
