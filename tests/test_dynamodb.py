import boto3
import sys
import json
import pytest
from deepdiff import DeepDiff


table_properties_exclude_paths = [
    "root['CreationDateTime']",
    "root['TableSizeBytes']",
    "root['TableArn']",
    "root['TableId']",
    "root['ProvisionedThroughput']['LastIncreaseDateTime']",
    "root['ProvisionedThroughput']['LastDecreaseDateTime']",
    "root['ProvisionedThroughput']['NumberOfDecreasesToday']",
    "root['ItemCount']",
    "root['Replicas']",
    "root['DeletionProtectionEnabled']",
    "root['GlobalSecondaryIndexes'][0]['IndexStatus']",
    "root['GlobalSecondaryIndexes'][0]['IndexSizeBytes']",
    "root['GlobalSecondaryIndexes'][0]['ItemCount']",
    "root['GlobalSecondaryIndexes'][0]['IndexArn']",
    "root['GlobalSecondaryIndexes'][0]['ProvisionedThroughput']['NumberOfDecreasesToday']"
]

def get_tables_struct():
    with open(f"{sys.path[0]}/tbl_struct.json", "r") as json_file:
        json_data = json.loads(json_file.read())["Tables"]
        return json_data


@pytest.fixture(params=get_tables_struct())
def get_table_struct(request):
    return request.param


@pytest.fixture()
def db_client():
    db = boto3.client("dynamodb",
                      endpoint_url="http://localhost:4566",
                      region_name="us-east-1")
    yield db
    db.close()


def test_table_properties(get_table_struct, db_client):
    resp = db_client.describe_table(TableName=get_table_struct["TableName"])
    diff = DeepDiff(resp["Table"],
                    get_table_struct,
                    exclude_paths=table_properties_exclude_paths,
                    ignore_order=True)
    assert not diff


def test_table_properties_has_tags(get_table_struct, db_client):
    resp_descr = db_client.describe_table(TableName=get_table_struct["TableName"])
    resp_tags = db_client.list_tags_of_resource(ResourceArn=resp_descr["Table"]["TableArn"])
    assert [tag["Key"] in ["Env", "Owner"] for tag in resp_tags["Tags"]] == [True, True]


def test_table_properties_item_count(get_table_struct, db_client):
    resp = db_client.describe_table(TableName=get_table_struct["TableName"])
    if not resp["Table"]["ItemCount"]:
        pytest.skip(f"Table '{get_table_struct['TableName']}' doesn't contain data")
    assert resp["Table"]["ItemCount"] == get_table_struct["ItemCount"]
