import boto3
from collections import defaultdict
from termcolor import colored

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
    ProjectionExpression='pk, sk'
)

# Retrieve the items associated with the user_uuid and message
items = response['Items']

if len(items) == 0:
    print(colored("No records with the specified user_uuid and message were found.", 'green'))
else:
    print(colored(f"Number of records retrieved: {colored(len(items), 'yellow')}", 'blue'))

    # Create a dictionary to track duplicate records
    duplicates = defaultdict(list)

    for item in items:
        pk = item.get('pk', {}).get('S')
        sk = item.get('sk', {}).get('S')
        if pk and sk:
            duplicates[pk].append(sk)

    # Determine the number of duplicate records to delete
    total_duplicates = 0
    for pk, sk_list in duplicates.items():
        if len(sk_list) > 2:
            total_duplicates += len(sk_list) - 2

    print(colored(f"Number of duplicate records found: {colored(total_duplicates, 'yellow')}", 'blue'))

    # Prompt the user to confirm deletion
    proceed = input(colored("Do you want to proceed with deleting duplicate records? (yes/no): ", 'blue'))

    if proceed.lower() == 'yes':
        deleted_count = 0

        for pk, sk_list in duplicates.items():
            if len(sk_list) > 2:
                # Delete extra duplicate records
                records_to_delete = sk_list[:-2]

                # Delete the records in batches
                while len(records_to_delete) > 0:
                    batch = [{'DeleteRequest': {'Key': {'pk': {'S': pk}, 'sk': {'S': sk}}}} for sk in records_to_delete[:25]]
                    response = dynamodb.batch_write_item(RequestItems={table_name: batch})
                    deleted_count += len(response.get('UnprocessedItems', {}).get(table_name, []))
                    records_to_delete = records_to_delete[25:]

        print(colored(f"Number of duplicate records deleted: {colored(deleted_count, 'yellow')}", 'blue'))
    else:
        print(colored("Deletion process aborted.", 'blue'))

    # Query the table to retrieve the remaining items with the matching user_uuid and message
    response = dynamodb.scan(
        TableName=table_name,
        FilterExpression='#uu = :user_uuid AND #msg = :message',
        ExpressionAttributeNames={'#uu': 'user_uuid', '#msg': 'message'},
        ExpressionAttributeValues={':user_uuid': {'S': user_uuid}, ':message': {'S': message}},
        ProjectionExpression='pk, message'
    )

    # Retrieve the remaining items associated with the user_uuid and message
    remaining_items = response['Items']
    print(colored(f"\nNumber of remaining records: {colored(len(remaining_items), 'yellow')}", 'blue'))
    print(colored("Value of 'message' attribute in remaining records:", 'blue'))
    for item in remaining_items:
        pk = item.get('pk', {}).get('S')
        message = item.get('message', {}).get('S')
        print(f"PK: {pk}\nMessage: {message}\n{'-' * 30}")
