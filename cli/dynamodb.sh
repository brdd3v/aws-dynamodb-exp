#!/bin/bash

RCU=10
WCU=10


aws dynamodb create-table \
    --table-name ProductCatalog \
    --attribute-definitions AttributeName=Id,AttributeType=N \
    --key-schema AttributeName=Id,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=$RCU,WriteCapacityUnits=$WCU \
    --tags Key=Env,Value=Dev Key=Owner,Value=Bash \
    --endpoint="http://localhost:4566" \
    --region="us-east-1" > /dev/null

echo "Table 'ProductCatalog' created"


aws dynamodb create-table \
    --table-name Forum \
    --attribute-definitions AttributeName=Name,AttributeType=S \
    --key-schema AttributeName=Name,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=$RCU,WriteCapacityUnits=$WCU \
    --tags Key=Env,Value=Dev Key=Owner,Value=Bash \
    --endpoint="http://localhost:4566" \
    --region="us-east-1" > /dev/null

echo "Table 'Forum' created"


aws dynamodb create-table \
    --table-name Thread \
    --attribute-definitions AttributeName=ForumName,AttributeType=S AttributeName=Subject,AttributeType=S \
    --key-schema AttributeName=ForumName,KeyType=HASH AttributeName=Subject,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=$RCU,WriteCapacityUnits=$WCU \
    --tags Key=Env,Value=Dev Key=Owner,Value=Bash \
    --endpoint="http://localhost:4566" \
    --region="us-east-1" > /dev/null

echo "Table 'Thread' created"


aws dynamodb create-table \
    --table-name Reply \
    --attribute-definitions AttributeName=Id,AttributeType=S AttributeName=ReplyDateTime,AttributeType=S AttributeName=PostedBy,AttributeType=S AttributeName=Message,AttributeType=S \
    --key-schema AttributeName=Id,KeyType=HASH AttributeName=ReplyDateTime,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=$RCU,WriteCapacityUnits=$WCU \
    --tags Key=Env,Value=Dev Key=Owner,Value=Bash \
    --global-secondary-indexes \
        "[
            {
                \"IndexName\": \"PostedBy-Message-Index\",
                \"KeySchema\": [
                    {\"AttributeName\":\"PostedBy\",\"KeyType\":\"HASH\"},
                    {\"AttributeName\":\"Message\",\"KeyType\":\"RANGE\"}
                ],
                \"Projection\": {
                    \"ProjectionType\":\"ALL\"
                },
                \"ProvisionedThroughput\": {
                    \"ReadCapacityUnits\": $RCU,
                    \"WriteCapacityUnits\": $WCU
                }
            }
        ]" \
    --endpoint="http://localhost:4566" \
    --region="us-east-1" > /dev/null

echo "Table 'Reply' created"

