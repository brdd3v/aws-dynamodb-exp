from constructs import Construct
from aws_cdk import (
    Stack,
    Tags,
    RemovalPolicy,
    aws_dynamodb as dynamodb,
)


billing_mode = dynamodb.BillingMode.PROVISIONED
read_capacity = 10
write_capacity = 10


class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        product_catalog = dynamodb.Table(self, "tbl_productCatalog",
                                         table_name="ProductCatalog",
                                         partition_key=dynamodb.Attribute(name="Id",
                                                                          type=dynamodb.AttributeType.NUMBER),
                                         billing_mode=billing_mode,
                                         read_capacity=read_capacity,
                                         write_capacity=write_capacity,
                                         removal_policy=RemovalPolicy.DESTROY,
                                         )
        # Tags.of(product_catalog).add("Env", "Dev")
        # Tags.of(product_catalog).add("Owner", "AWSCDK")

        forum = dynamodb.Table(self, "tbl_forum",
                               table_name="Forum",
                               partition_key=dynamodb.Attribute(name="Name", type=dynamodb.AttributeType.STRING),
                               billing_mode=billing_mode,
                               read_capacity=read_capacity,
                               write_capacity=write_capacity,
                               removal_policy=RemovalPolicy.DESTROY,
                               )
        # Tags.of(forum).add("Env", "Dev")
        # Tags.of(forum).add("Owner", "AWSCDK")

        thread = dynamodb.Table(self, "tbl_thread",
                                table_name="Thread",
                                partition_key=dynamodb.Attribute(name="ForumName", type=dynamodb.AttributeType.STRING),
                                sort_key=dynamodb.Attribute(name="Subject", type=dynamodb.AttributeType.STRING),
                                billing_mode=billing_mode,
                                read_capacity=read_capacity,
                                write_capacity=write_capacity,
                                removal_policy=RemovalPolicy.DESTROY,
                                )
        # Tags.of(thread).add("Env", "Dev")
        # Tags.of(thread).add("Owner", "AWSCDK")

        reply = dynamodb.Table(self, "tbl_reply",
                               table_name="Reply",
                               partition_key=dynamodb.Attribute(name="Id", type=dynamodb.AttributeType.STRING),
                               sort_key=dynamodb.Attribute(name="ReplyDateTime", type=dynamodb.AttributeType.STRING),
                               billing_mode=billing_mode,
                               read_capacity=read_capacity,
                               write_capacity=write_capacity,
                               removal_policy=RemovalPolicy.DESTROY,
                               )
        reply.add_global_secondary_index(
            index_name="PostedBy-Message-Index",
            partition_key=dynamodb.Attribute(name="PostedBy", type=dynamodb.AttributeType.STRING),
            sort_key=dynamodb.Attribute(name="Message", type=dynamodb.AttributeType.STRING),
            projection_type=dynamodb.ProjectionType.ALL,
            read_capacity=read_capacity,
            write_capacity=write_capacity,
        )
        # Tags.of(reply).add("Env", "Dev")
        # Tags.of(reply).add("Owner", "AWSCDK")

