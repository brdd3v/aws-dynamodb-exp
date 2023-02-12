aws_dynamodb_table 'ProductCatalog' do
  action :create
  attribute_definitions [
    { attribute_name: 'Id', attribute_type: 'N' }
  ]
  key_schema [
    { attribute_name: 'Id', key_type: 'HASH' }
  ]
  provisioned_throughput ({
    read_capacity_units: 10,
    write_capacity_units: 10
  })
  stream_specification ({
    stream_enabled: false
  })
end

aws_dynamodb_table 'Forum' do
  action :create
  attribute_definitions [
    { attribute_name: 'Name', attribute_type: 'S' }
  ]
  key_schema [
    { attribute_name: 'Name', key_type: 'HASH' }
  ]
  provisioned_throughput ({
    read_capacity_units: 10,
    write_capacity_units: 10
  })
  stream_specification ({
    stream_enabled: false
  })
end

aws_dynamodb_table 'Thread' do
  action :create
  attribute_definitions [
    { attribute_name: 'ForumName', attribute_type: 'S' },
    { attribute_name: 'Subject', attribute_type: 'S' }
  ]
  key_schema [
    { attribute_name: 'ForumName', key_type: 'HASH' },
    { attribute_name: 'Subject', key_type: 'RANGE' }
  ]
  provisioned_throughput ({
    read_capacity_units: 10,
    write_capacity_units: 10
  })
  stream_specification ({
    stream_enabled: false
  })
end

aws_dynamodb_table 'Reply' do
  action :create
  attribute_definitions [
    { attribute_name: 'Id', attribute_type: 'S' },
    { attribute_name: 'ReplyDateTime', attribute_type: 'S' },
    { attribute_name: 'PostedBy', attribute_type: 'S' },
    { attribute_name: 'Message', attribute_type: 'S' }
  ]
  key_schema [
    { attribute_name: 'Id', key_type: 'HASH' },
    { attribute_name: 'ReplyDateTime', key_type: 'RANGE' }
  ]
  global_secondary_indexes [
    {
      index_name: 'PostedBy-Message-Index',
      key_schema: [
        {attribute_name: 'PostedBy', key_type: 'HASH'},
        {attribute_name: 'Message', key_type: 'RANGE'}
      ],
      projection: {
        projection_type: 'ALL'
      },
      provisioned_throughput: {
        read_capacity_units: 10,
        write_capacity_units: 10
      }
    }
  ]
  provisioned_throughput ({
    read_capacity_units: 10,
    write_capacity_units: 10
  })
  stream_specification ({
    stream_enabled: false
  })
end
