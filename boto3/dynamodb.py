#!/usr/bin/env python

import boto3

db_client = boto3.client('dynamodb',
                         endpoint_url='http://localhost:4566',
                         region_name="us-east-1")

params = {
    'BillingMode': 'PROVISIONED',
    'ProvisionedThroughput': {'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10},
    'Tags': [{'Key': 'Env', 'Value': 'Dev'},
             {'Key': 'Owner', 'Value': 'AWSPythonSDK'}]
}


def main():

    db_client.create_table(
        TableName='ProductCatalog',
        AttributeDefinitions=[{'AttributeName': 'Id', 'AttributeType': 'N'}],
        KeySchema=[{'AttributeName': 'Id', 'KeyType': 'HASH'}],
        **params
    )
    print("Table 'ProductCatalog' created")

    db_client.create_table(
        TableName='Forum',
        AttributeDefinitions=[{'AttributeName': 'Name', 'AttributeType': 'S'}],
        KeySchema=[{'AttributeName': 'Name', 'KeyType': 'HASH'}],
        **params
    )
    print("Table 'Forum' created")

    db_client.create_table(
        TableName='Thread',
        AttributeDefinitions=[
            {'AttributeName': 'ForumName', 'AttributeType': 'S'},
            {'AttributeName': 'Subject', 'AttributeType': 'S'},
        ],
        KeySchema=[
            {'AttributeName': 'ForumName', 'KeyType': 'HASH'},
            {'AttributeName': 'Subject', 'KeyType': 'RANGE'}
        ],
        **params
    )
    print("Table 'Thread' created")

    db_client.create_table(
        TableName='Reply',
        AttributeDefinitions=[
            {'AttributeName': 'Id', 'AttributeType': 'S'},
            {'AttributeName': 'ReplyDateTime', 'AttributeType': 'S'},
            {'AttributeName': 'PostedBy', 'AttributeType': 'S'},
            {'AttributeName': 'Message', 'AttributeType': 'S'},
        ],
        KeySchema=[
            {'AttributeName': 'Id', 'KeyType': 'HASH'},
            {'AttributeName': 'ReplyDateTime', 'KeyType': 'RANGE'}
        ],
        GlobalSecondaryIndexes=[
            {'IndexName': 'PostedBy-Message-Index',
             'KeySchema': [
                 {'AttributeName': 'PostedBy', 'KeyType': 'HASH'},
                 {'AttributeName': 'Message', 'KeyType': 'RANGE'},
            ],
            'Projection': {'ProjectionType': 'ALL'},
            'ProvisionedThroughput': params['ProvisionedThroughput']}
        ],
        **params
    )
    print("Table 'Reply' created")


if __name__ == "__main__":
    main()
