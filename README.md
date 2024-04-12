aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 764118177562.dkr.ecr.eu-central-1.amazonaws.com
docker build --platform linux/arm64 -t dompitest:test1 .
aws ecr create-repository --repository-name hello-world --region eu-central-1 --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
docker tag dompitest:test1 764118177562.dkr.ecr.eu-central-1.amazonaws.com/hello-world:latest
docker push 764118177562.dkr.ecr.eu-central-1.amazonaws.com/hello-world:latest


on:
  push:
    branches:
      - master
jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: Install zip tool
        uses: montudor/action-zip@v1
      - name: Create zip file
        run: cd lambda_functions && zip -r lambda.zip .
      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: eu-central-1
      - name: Update Lambda Function
        run: |
          aws lambda update-function-code \
          --function-name arn:aws:lambda:eu-central-1:764118177562:function:sendSlackMessageWhenNewImageIsUploaded \
          --zip-file fileb://lambda_functions/lambda.zip
      
