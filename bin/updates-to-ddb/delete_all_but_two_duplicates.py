import boto3
from collections import defaultdict
from termcolor import colored

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define table name
table_name = 'cruddur-messages'

# Prompt the user to enter the user_uuid
user_uuid = input("Enter the user_uuid: ")

# Query the table to retrieve all items with the matching user_uuid
response = dynamodb.scan(
    TableName=table_name,
    FilterExpression='#uu = :user_uuid',
    ExpressionAttributeNames={'#uu': 'user_uuid'},
    ExpressionAttributeValues={':user_uuid': {'S': user_uuid}},
    ProjectionExpression='pk, sk, message'
)

# Retrieve the items associated with the user_uuid
items = response['Items']

if len(items) == 0:
    print(colored("No records with the specified user_uuid were found.", 'green'))
else:
    print(colored(f"Number of records retrieved: {colored(len(items), 'yellow')}", 'blue'))

    # Create a dictionary to track duplicate records
    duplicates = defaultdict(list)

    for item in items:
        pk = item.get('pk', {}).get('S')
        sk = item.get('sk', {}).get('S')
        message = item.get('message', {}).get('S')
        if pk and sk and message:
            duplicates[message].append((pk, sk))

    # Determine the number of duplicate records
    total_duplicates = sum(len(sk_list) - 2 for sk_list in duplicates.values() if len(sk_list) > 2)

    print(colored(f"Number of duplicate records found: {colored(total_duplicates, 'yellow')}", 'blue'))

    # Prompt the user to confirm deletion
    proceed = input(colored("Do you want to proceed with deleting duplicate records? (yes/no): ", 'blue'))

    if proceed.lower() == 'yes':
        deleted_count = 0

        for sk_list in duplicates.values():
            if len(sk_list) > 2:
                # Sort the records based on sk value
                sk_list.sort(key=lambda x: x[1])

                # Delete extra duplicate records
                records_to_delete = sk_list[:-2]

                for pk, sk in records_to_delete:
                    response = dynamodb.delete_item(
                        TableName=table_name,
                        Key={
                            'pk': {'S': pk},
                            'sk': {'S': sk}
                        }
                    )
                    deleted_count += 1

        print(colored(f"Number of duplicate records deleted: {colored(deleted_count, 'yellow')}", 'blue'))
    else:
        print(colored("Deletion process aborted.", 'blue'))

    # Query the table to retrieve the remaining items with the matching user_uuid
    response = dynamodb.scan(
        TableName=table_name,
        FilterExpression='#uu = :user_uuid',
        ExpressionAttributeNames={'#uu': 'user_uuid'},
        ExpressionAttributeValues={':user_uuid': {'S': user_uuid}},
        ProjectionExpression='pk, message'
    )

    # Retrieve the remaining items associated with the user_uuid
    remaining_items = response['Items']
    print(colored(f"\nNumber of remaining records: {colored(len(remaining_items), 'yellow')}", 'blue'))
    print(colored("Value of 'message' attribute in remaining records:", 'blue'))
    for item in remaining_items:
        pk = item.get('pk', {}).get('S')
        message = item.get('message', {}).get('S')
        print(f"PK: {pk}\nMessage: {message}\n{'-' * 30}")
