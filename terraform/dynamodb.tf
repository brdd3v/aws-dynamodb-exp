locals {
  billing_mode   = "PROVISIONED"
  read_capacity  = 10
  write_capacity = 10
}

resource "aws_dynamodb_table" "ProductCatalog" {
  name           = "ProductCatalog"
  billing_mode   = local.billing_mode
  read_capacity  = local.read_capacity
  write_capacity = local.write_capacity
  hash_key       = "Id"

  attribute {
    name = "Id"
    type = "N"
  }
}

resource "aws_dynamodb_table" "Forum" {
  name           = "Forum"
  billing_mode   = local.billing_mode
  read_capacity  = local.read_capacity
  write_capacity = local.write_capacity
  hash_key       = "Name"

  attribute {
    name = "Name"
    type = "S"
  }
}

resource "aws_dynamodb_table" "Thread" {
  name           = "Thread"
  billing_mode   = local.billing_mode
  read_capacity  = local.read_capacity
  write_capacity = local.write_capacity
  hash_key       = "ForumName"
  range_key      = "Subject"

  attribute {
    name = "ForumName"
    type = "S"
  }

  attribute {
    name = "Subject"
    type = "S"
  }
}

resource "aws_dynamodb_table" "Reply" {
  name           = "Reply"
  billing_mode   = local.billing_mode
  read_capacity  = local.read_capacity
  write_capacity = local.write_capacity
  hash_key       = "Id"
  range_key      = "ReplyDateTime"

  attribute {
    name = "Id"
    type = "S"
  }

  attribute {
    name = "ReplyDateTime"
    type = "S"
  }

  attribute {
    name = "PostedBy"
    type = "S"
  }

  attribute {
    name = "Message"
    type = "S"
  }

  global_secondary_index {
    name            = "PostedBy-Message-Index"
    hash_key        = "PostedBy"
    range_key       = "Message"
    read_capacity   = local.read_capacity
    write_capacity  = local.write_capacity
    projection_type = "ALL"
  }
}
