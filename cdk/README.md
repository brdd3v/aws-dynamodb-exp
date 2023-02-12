## [AWS CDK](https://aws.amazon.com/cdk/) (Cloud Development Kit)

More information about the module can be found [here](https://docs.aws.amazon.com/cdk/api/v1/docs/aws-dynamodb-readme.html).


For the convenience of working with LocalStack, the [cdklocal](https://docs.localstack.cloud/user-guide/integrations/aws-cdk/) script was used.


To bootstrap:
```
cdklocal bootstrap
```


To create tables:
```
cdklocal deploy
```


To delete tables:
```
cdklocal destroy --force
```
