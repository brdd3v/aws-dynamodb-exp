## Creating tables in DynamoDB using ...

Example tables and sample data can be found [here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SampleData.html) (This sample data is also saved in the [data](/data/) folder).

Testing was carried out on the AWS account, the [local version](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html) of DynamoDB, and [LocalStack](https://localstack.cloud/) <sup>1</sup>.



|                | AWS Account        | LocalStack         | DynamoDB Local     |
| -------------- | ------------------ | ------------------ | ------------------ |
| Bash (AWS CLI) | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Boto3          | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Terraform      | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| CDKTF          | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Pulumi         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Ansible        | :heavy_check_mark: | :heavy_check_mark: | :x: <sup>2</sup>   |
| Serverless     | :heavy_check_mark: | :wavy_dash: <sup>3</sup> | :wavy_dash: <sup>4</sup> |
| CloudFormation | :heavy_check_mark: | :wavy_dash: <sup>3</sup> | :x:          |
| SAM            | :heavy_check_mark: | :wavy_dash: <sup>3</sup> | :x:          |
| CDK            | :heavy_check_mark: | :wavy_dash: <sup>3</sup> | :x:          |
| Chef           | :wavy_dash: <sup>5</sup> | :x:                | :x:          |



#### Footnotes

1. Files in this repository are configured to work with LocalStack by default.
2. The current version of DynamoDB Local does not support tagging.
3. The current community version of LocalStack does not completely support all the features of [CloudFormation](https://docs.localstack.cloud/user-guide/aws/cloudformation/).
4. Plugin for working with DynamoDB Local supports migration (creation of tables), but, apparently, not removal.
5. There are restrictions (the possibility of deleting tables or adding tags is not found).

