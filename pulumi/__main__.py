import pulumi_aws as aws

billing_mode="PROVISIONED"
read_capacity=10
write_capacity=10


product_catalog = aws.dynamodb.Table(
    resource_name="tbl_productCatalog",
    name="ProductCatalog",
    attributes=[{
        "name": "Id",
        "type": "N",
    }],
    billing_mode=billing_mode,
    hash_key="Id",
    read_capacity=read_capacity,
    write_capacity=write_capacity
)


forum = aws.dynamodb.Table(
    resource_name="tbl_forum",
    name="Forum",
    attributes=[{
        "name": "Name",
        "type": "S",
    }],
    billing_mode=billing_mode,
    hash_key="Name",
    read_capacity=read_capacity,
    write_capacity=write_capacity
)


thread = aws.dynamodb.Table(
    resource_name="tbl_thread",
    name="Thread",
    attributes=[
        {
            "name": "ForumName",
            "type": "S",
        },
        {
            "name": "Subject",
            "type": "S",
        },
    ],
    billing_mode=billing_mode,
    hash_key="ForumName",
    range_key="Subject",
    read_capacity=read_capacity,
    write_capacity=write_capacity
)


reply = aws.dynamodb.Table(
    resource_name="tbl_reply",
    name="Reply",
    attributes=[
        {
            "name": "Id",
            "type": "S",
        },
        {
            "name": "ReplyDateTime",
            "type": "S",
        },
        {
            "name": "PostedBy",
            "type": "S",
        },
        {
            "name": "Message",
            "type": "S",
        },
    ],
    billing_mode=billing_mode,
    global_secondary_indexes=[{
        "name": "PostedBy-Message-Index",
        "hash_key": "PostedBy",
        "range_key": "Message",
        "projectionType": "ALL",
        "read_capacity": read_capacity,
        "write_capacity": write_capacity,
    }],
    hash_key="Id",
    range_key="ReplyDateTime",
    read_capacity=read_capacity,
    write_capacity=write_capacity
)
