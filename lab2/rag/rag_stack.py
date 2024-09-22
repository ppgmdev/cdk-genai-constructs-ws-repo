from aws_cdk import (
    Duration,
    Stack,
    CfnOutput,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_apigateway as apigateway,
)

from cdklabs.generative_ai_cdk_constructs import (
    bedrock
)

from constructs import Construct

class RAGStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        region = Stack.of(self).region

        ##### Step 1: Configure S3 Buckets and upload files to S3


        ##### Step 2: Configure Bedrock S3 data Source and Knowledge base



        ##### Step 3: Create a Lambda function and API gateway to query the Knowledge base


