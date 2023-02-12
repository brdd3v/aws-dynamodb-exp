#!/usr/bin/env python

import boto3
import sys
import os
import json


def main():
    db_client = boto3.client('dynamodb',
                             endpoint_url='http://localhost:4566',
                             region_name="us-east-1")

    json_files = [f.path for f in os.scandir(sys.path[0]) if f.name.endswith('.json')]
    for json_file in json_files:
        with open(json_file, "r") as f:
            content = json.loads(f.read())
            resp = db_client.batch_write_item(RequestItems=content)
            print(f"Successfully loaded data into the table '{list(content.keys())[0]}'")


if __name__ == "__main__":
    main()
