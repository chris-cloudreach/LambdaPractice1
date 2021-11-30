terraform {
  backend "s3"{
      bucket = "my-first-lambdabucket-194694014750"
      key = "sprint2/week4/lambda-function/terraform.tfstate"
      dynamodb_table = "terraform-lock"
  }
}