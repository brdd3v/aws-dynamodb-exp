## [Crossplane](https://www.crossplane.io/)

More information about the resource can be found [here](https://doc.crds.dev/github.com/crossplane/provider-aws/dynamodb.aws.crossplane.io/Table/v1alpha1@v0.41.1).



### Install

Install the Crossplane Helm chart:
```
helm repo add crossplane-stable https://charts.crossplane.io/stable
helm repo update
helm install crossplane crossplane-stable/crossplane --namespace crossplane-system --create-namespace
```

Install the AWS provider:
```
kubectl apply -f provider.yaml
```

Create a K8s secret with AWS credentials:
```
kubectl create secret generic aws-secret -n crossplane-system --from-file=creds=./aws-credentials-sample.txt
```

Create a ProviderConfig:
```
kubectl apply -f provider-config.yaml
```

More information about ProviderConfig can be found [here](https://doc.crds.dev/github.com/crossplane/provider-aws/aws.crossplane.io/ProviderConfig/v1beta1@v0.41.1).


### Usage

To create tables:
```
kubectl apply -f dynamodb.yaml
```


To delete tables:
```
kubectl delete -f dynamodb.yaml
```

### Notes

For testing in LocalStack, [Helm chart](https://github.com/localstack/helm-charts) is needed.

You can also consider [this source](https://alvsanand.github.io/apify-your-infra-with-crossplane/) as an example of using LocalStack and Crossplane.
