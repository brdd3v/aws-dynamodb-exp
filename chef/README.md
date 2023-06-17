## [Chef](https://www.chef.io/)

More information about the aws Cookbook can be found [here](https://supermarket.chef.io/cookbooks/aws).


To create tables:
```
chef-client -z --runlist "recipe[dynamo::default]"
```

or

```
chef-client -z -o dynamo
```
