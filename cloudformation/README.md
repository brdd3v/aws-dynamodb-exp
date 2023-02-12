## [AWS CloudFormation](https://aws.amazon.com/cloudformation/) (using AWS CLI)

More information about the structure of the template can be found [here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html), and about commands for working with CloudFormation [here](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/index.html).


To create tables:
```
aws cloudformation deploy --stack-name="dynamodb-exp" --template-file="./dynamodb.yaml" --region="us-east-1" --endpoint-url="http://localhost:4566"
```


To delete tables:
```
aws cloudformation delete-stack --stack-name="dynamodb-exp" --region="us-east-1" --endpoint-url="http://localhost:4566"
```


For the convenience of working with LocalStack (In order not to specify the endpoint-url each time), you can use [awslocal](https://docs.localstack.cloud/user-guide/integrations/aws-cli/).
