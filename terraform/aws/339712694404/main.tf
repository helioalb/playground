resource "aws_vpc" "spree" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name: "Spree"
  }
}
