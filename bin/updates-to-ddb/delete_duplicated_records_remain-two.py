import boto3

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Prompt the user to enter the user_uuid and message
user_uuid = input("Enter the user_uuid: ")
message = input("Enter the message: ")

# Query the table to retrieve the items with the matching user_uuid and message
response = dynamodb.scan(
    TableName=table_name,
    FilterExpression='#uu = :user_uuid AND #msg = :message',
    ExpressionAttributeNames={'#uu': 'user_uuid', '#msg': 'message'},
    ExpressionAttributeValues={':user_uuid': {'S': user_uuid}, ':message': {'S': message}},
    ProjectionExpression='pk, sk, message'
)

# Retrieve the items associated with the user_uuid and message
items = response['Items']

if len(items) == 0:
    print("No records with the specified user_uuid and message were found.")
else:
    print(f"Number of records retrieved: {len(items)}")

    # Create a dictionary to track duplicate messages
    duplicates = {}

    for item in items:
        sk = item.get('sk', {}).get('S')
        if sk:
            if sk not in duplicates:
                duplicates[sk] = {
                    'count': 1,
                    'pk': item.get('pk', {}).get('S'),
                    'message': item.get('message', {}).get('S')
                }
            else:
                duplicates[sk]['count'] += 1

    if duplicates:
        print("\nDuplicate records found:")
        remaining_duplicates = 2
        deleted_count = 0
        for sk, data in duplicates.items():
            count = data['count']
            if count > remaining_duplicates:
                deleted_count += 1
                # Delete the extra duplicate records
                response = dynamodb.delete_item(
                    TableName=table_name,
                    Key={
                        'pk': {'S': data['pk']},
                        'sk': {'S': sk}
                    }
                )

        print(f"Number of duplicate records deleted: {deleted_count}")

    else:
        print("\nNo duplicate records found.")

    # Query the table to retrieve the items with the matching user_uuid and message
    response = dynamodb.scan(
        TableName=table_name,
        FilterExpression='#uu = :user_uuid AND #msg = :message',
        ExpressionAttributeNames={'#uu': 'user_uuid', '#msg': 'message'},
        ExpressionAttributeValues={':user_uuid': {'S': user_uuid}, ':message': {'S': message}},
        ProjectionExpression='pk, message'
    )

    # Retrieve the items associated with the user_uuid and message
    remaining_items = response['Items']
    print(f"\nNumber of remaining records: {len(remaining_items)}")
    print("Value of 'message' attribute in remaining records:")
    for item in remaining_items:
        pk = item.get('pk', {}).get('S')
        message = item.get('message', {}).get('S')
        print(f"PK: {pk}\nMessage: {message}\n{'-' * 30}")
