import boto3

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Prompt the user to enter the user_uuid
user_uuid = input("Enter the user_uuid: ")

# Query the table to retrieve the items with the matching user_uuid
response = dynamodb.scan(
    TableName=table_name,
    FilterExpression='#uu = :user_uuid',
    ExpressionAttributeNames={'#uu': 'user_uuid'},
    ExpressionAttributeValues={':user_uuid': {'S': user_uuid}},
    ProjectionExpression='message'
)

# Retrieve the items associated with the user_uuid
items = response['Items']

if len(items) == 0:
    print("No records with the specified user_uuid were found.")
else:
    print(f"Number of records retrieved: {len(items)}")

    # Create a set to track duplicate messages
    message_set = set()
    duplicates = {}

    for item in items:
        message = item.get('message', {}).get('S')
        if message:
            if message in message_set:
                if message not in duplicates:
                    duplicates[message] = 2
                else:
                    duplicates[message] += 1
            else:
                message_set.add(message)

    if duplicates:
        print("\nDuplicate records found:")
        for message, count in duplicates.items():
            print(f"Message: {message}")
            print(f"Count: {count}")
            print("------------------------------")
    else:
        print("\nNo duplicate records found.")
