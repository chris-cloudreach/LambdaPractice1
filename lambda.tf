# This is the actual lambda function
resource "aws_lambda_function" "test_lambda" {
  s3_key      = "BotoScript.zip"
  function_name = "BotoScript"
  s3_bucket     = "my-first-lambdabucket-194694014750"
  role          = aws_iam_role.lambda_role.arn
  handler       = "BotoScript.handler"
  runtime       = "python3.8"
}