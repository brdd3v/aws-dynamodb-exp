## [AWS SAM](https://aws.amazon.com/serverless/sam/) (Serverless Application Model)

More information about the structure of the template can be found [here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-dynamodb.html).


For the convenience of working with LocalStack, the [samlocal](https://docs.localstack.cloud/user-guide/integrations/aws-sam/) script was used.


To create tables:
```
samlocal deploy --config-file="./samconfig.toml" --template-file="./dynamodb.yaml"
```


To delete tables:
```
samlocal delete --no-prompts --config-file="./samconfig.toml"
```
