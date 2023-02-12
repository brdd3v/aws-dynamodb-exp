#!/usr/bin/env python

from constructs import Construct
from cdktf_cdktf_provider_aws.provider import AwsProvider, AwsProviderDefaultTags
from cdktf_cdktf_provider_aws.dynamodb_table import DynamodbTable, DynamodbTableGlobalSecondaryIndex
from cdktf import App, TerraformStack


billing_mode = "PROVISIONED"
read_capacity = 10
write_capacity = 10


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AwsProvider(self, "AWS",
                    access_key="mock_access_key",
                    secret_key="mock_secret_key",
                    region="us-east-1",
                    skip_credentials_validation=True,
                    skip_metadata_api_check="True",
                    skip_requesting_account_id=True,
                    endpoints=[
                        {"dynamodb": "http://localhost:4566"}
                    ],
                    default_tags=[
                        AwsProviderDefaultTags(tags={"Env": "Dev",
                                                     "Owner": "CDKTF"}
                                               )
                    ],
                    )

        product_catalog = DynamodbTable(self, "tbl_productCatalog",
                                        name="ProductCatalog",
                                        billing_mode=billing_mode,
                                        read_capacity=read_capacity,
                                        write_capacity=write_capacity,
                                        hash_key="Id",
                                        attribute=[
                                            {"name": "Id", "type": "N"}
                                        ],
                                        )

        forum = DynamodbTable(self, "tbl_forum",
                              name="Forum",
                              billing_mode=billing_mode,
                              read_capacity=read_capacity,
                              write_capacity=write_capacity,
                              hash_key="Name",
                              attribute=[
                                  {"name": "Name", "type": "S"}
                              ],
                              )

        thread = DynamodbTable(self, "tbl_thread",
                               name="Thread",
                               billing_mode=billing_mode,
                               read_capacity=read_capacity,
                               write_capacity=write_capacity,
                               hash_key="ForumName",
                               range_key="Subject",
                               attribute=[
                                   {"name": "ForumName", "type": "S"},
                                   {"name": "Subject", "type": "S"}
                               ],
                               )

        reply = DynamodbTable(self, "tbl_reply",
                              name="Reply",
                              billing_mode=billing_mode,
                              read_capacity=read_capacity,
                              write_capacity=write_capacity,
                              hash_key="Id",
                              range_key="ReplyDateTime",
                              attribute=[
                                  {"name": "Id", "type": "S"},
                                  {"name": "ReplyDateTime", "type": "S"},
                                  {"name": "PostedBy", "type": "S"},
                                  {"name": "Message", "type": "S"}
                              ],
                              global_secondary_index=[
                                  DynamodbTableGlobalSecondaryIndex(
                                      name="PostedBy-Message-Index",
                                      hash_key="PostedBy",
                                      range_key="Message",
                                      read_capacity=read_capacity,
                                      write_capacity=write_capacity,
                                      projection_type="ALL"
                                  )
                              ],
                              )


app = App()
MyStack(app, "cdktf")

app.synth()
