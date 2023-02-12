## [Serverless](https://www.serverless.com/)

More information about the Serverless Dynamodb Local Plugin can be found [here](https://www.serverless.com/plugins/serverless-dynamodb-local).


More information about the Serverless plugin for LocalStack can be found [here](https://www.serverless.com/plugins/serverless-localstack).


To create and delete tables (AWS Account):
```
serverless deploy --stage prod
serverless remove --stage prod
```


To create and delete tables (LocalStack):
```
serverless deploy --stage local
serverless remove --stage local
```


To create tables (DynamoDB Local):
```
serverless dynamodb migrate
```
