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

resource "aws_internet_gateway" "ig" {
  vpc_id = aws_vpc.spree.id

  tags = {
    Name = "Spree Internet Gateway"
  }

  provider = aws.virginia
}

resource "aws_route_table" "second_rt" {
  vpc_id = aws_vpc.spree.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.ig.id
  }

  tags = {
    Name = "Second Route Table"
  }

  provider = aws.virginia
}

resource "aws_route_table_association" "public_1" {
  subnet_id      = aws_subnet.public_1.id
  route_table_id = aws_route_table.second_rt.id
}

resource "aws_route_table_association" "public_2" {
  subnet_id      = aws_subnet.public_2.id
  route_table_id = aws_route_table.second_rt.id
}

resource "aws_security_group" "bastion" {
  name        = "bastion-sg"
  description = "Bastion traffic"
  vpc_id      = aws_vpc.spree.id

  tags = {
    Name = "bastion-sg"
  }

  provider = aws.virginia
}

resource "aws_vpc_security_group_ingress_rule" "bastion_ssh" {
  security_group_id = aws_security_group.bastion.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 22
  ip_protocol       = "tcp"
  to_port           = 22
  description       = "SSH"

  tags = {
    Name = "SSH"
  }

  provider = aws.virginia
}

resource "aws_vpc_security_group_egress_rule" "allow_all_traffic_ipv4" {
  security_group_id = aws_security_group.bastion.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1" # semantically equivalent to all ports
  description       = "All traffic"

  tags = {
    Name = "All traffic"
  }

  provider = aws.virginia
}

resource "aws_instance" "bastion" {
  ami                         = "ami-080e1f13689e07408"
  instance_type               = "t2.micro"
  associate_public_ip_address = true
  availability_zone           = "us-east-1a"
  subnet_id                   = aws_subnet.public_1.id
  vpc_security_group_ids      = [aws_security_group.bastion.id]
  key_name                    = "maintenance"
  tags = {
    Name = "Bastion"
  }

  provider = aws.virginia
}

resource "aws_security_group" "postgres" {
  name        = "postgres-sg"
  description = "Postgres traffic"
  vpc_id      = aws_vpc.spree.id

  tags = {
    Name = "postgres-sg"
  }

  provider = aws.virginia
}

resource "aws_vpc_security_group_ingress_rule" "postgres_ingress_from_bastion" {
  security_group_id            = aws_security_group.postgres.id
  ip_protocol                  = "tcp"
  from_port                    = 5432
  to_port                      = 5432
  referenced_security_group_id = aws_security_group.bastion.id

  tags = {
    Name = "postgresql"
  }

  provider = aws.virginia
}
