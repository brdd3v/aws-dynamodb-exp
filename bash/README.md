## Bash (using [AWS CLI](https://aws.amazon.com/cli/))

More information about the commands can be found [here](https://docs.aws.amazon.com/cli/latest/reference/dynamodb/index.html) and usage examples [here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tools.CLI.html).


To create tables:
```
./dynamodb.sh
```


To delete tables:
```
./dynamodb_del.sh
```

For the convenience of working with LocalStack (In order not to specify the endpoint-url each time), you can use [awslocal](https://docs.localstack.cloud/user-guide/integrations/aws-cli/).
