resource "aws_vpc" "spree" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "Spree"
  }

  provider = aws.virginia
}

resource "aws_subnet" "public_1" {
  vpc_id            = aws_vpc.spree.id
  cidr_block        = "10.0.0.0/24"
  availability_zone = "us-east-1a"
  tags = {
    Name = "Public Subnet 1"
  }

  provider = aws.virginia
}

resource "aws_subnet" "private_1" {
  vpc_id            = aws_vpc.spree.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "Private Subnet 1"
  }

  provider = aws.virginia
}

resource "aws_subnet" "public_2" {
  vpc_id            = aws_vpc.spree.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "us-east-1b"
  tags = {
    Name = "Public Subnet 2"
  }

  provider = aws.virginia
}

resource "aws_subnet" "private_2" {
  vpc_id            = aws_vpc.spree.id
  cidr_block        = "10.0.3.0/24"
  availability_zone = "us-east-1b"

  tags = {
    Name = "Private Subnet 2"
  }

  provider = aws.virginia
}
