#!/usr/bin/env python

import boto3


def main():
    db_client = boto3.client('dynamodb',
                         endpoint_url='http://localhost:4566',
                         region_name="us-east-1")

    for table_name in ["Forum", "ProductCatalog", "Reply", "Thread"]:
        db_client.delete_table(TableName=table_name)
        print(f"Table '{table_name}' deleted")


if __name__ == "__main__":
    main()
