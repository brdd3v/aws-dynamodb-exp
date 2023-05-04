from troposphere import Template, Tags
from troposphere.dynamodb import (
    Table,
    AttributeDefinition,
    KeySchema,
    ProvisionedThroughput,
    GlobalSecondaryIndex,
    Projection
)


tags = Tags(Env="Dev", Owner="AWSCF")

provisioned_throughput = ProvisionedThroughput(
    ReadCapacityUnits=10, WriteCapacityUnits=10
)


t = Template()

t.set_version("2010-09-09")

t.add_resource(
    Table(
        "ProductCatalog",
        TableName="ProductCatalog",
        AttributeDefinitions=[
            AttributeDefinition(AttributeName="Id", AttributeType="N")
        ],
        KeySchema=[
            KeySchema(AttributeName="Id", KeyType="HASH")
        ],
        ProvisionedThroughput=provisioned_throughput,
        Tags=tags
    )
)

t.add_resource(
    Table(
        "Forum",
        TableName="Forum",
        AttributeDefinitions=[
            AttributeDefinition(AttributeName="Name", AttributeType="S")
        ],
        KeySchema=[
            KeySchema(AttributeName="Name", KeyType="HASH")
        ],
        ProvisionedThroughput=provisioned_throughput,
        Tags=tags
    )
)

t.add_resource(
    Table(
        "Thread",
        TableName="Thread",
        AttributeDefinitions=[
            AttributeDefinition(AttributeName="ForumName", AttributeType="S"),
            AttributeDefinition(AttributeName="Subject", AttributeType="S")
        ],
        KeySchema=[
            KeySchema(AttributeName="ForumName", KeyType="HASH"),
            KeySchema(AttributeName="Subject", KeyType="RANGE")
        ],
        ProvisionedThroughput=provisioned_throughput,
        Tags=tags
    )
)

t.add_resource(
    Table(
        "Reply",
        TableName="Reply",
        AttributeDefinitions=[
            AttributeDefinition(AttributeName="Id", AttributeType="S"),
            AttributeDefinition(AttributeName="ReplyDateTime", AttributeType="S"),
            AttributeDefinition(AttributeName="PostedBy", AttributeType="S"),
            AttributeDefinition(AttributeName="Message", AttributeType="S")
        ],
        KeySchema=[
            KeySchema(AttributeName="Id", KeyType="HASH"),
            KeySchema(AttributeName="ReplyDateTime", KeyType="RANGE")
        ],
        ProvisionedThroughput=provisioned_throughput,
        GlobalSecondaryIndexes=[
            GlobalSecondaryIndex(
                IndexName="PostedBy-Message-Index",
                KeySchema=[
                    KeySchema(AttributeName="PostedBy", KeyType="HASH"),
                    KeySchema(AttributeName="Message", KeyType="RANGE")
                ],
                Projection=Projection(ProjectionType="ALL"),
                ProvisionedThroughput=provisioned_throughput
            )
        ],
        Tags=tags
    )
)

with open("dynamodb_.yaml", "w") as f:
    f.write(t.to_yaml())
