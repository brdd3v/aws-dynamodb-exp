#!/bin/bash

for table_name in ProductCatalog Forum Thread Reply
do
    aws dynamodb delete-table \
        --table-name $table_name \
        --endpoint="http://localhost:4566" \
        --region="us-east-1" > /dev/null

    echo "Table '$table_name' deleted"
done

