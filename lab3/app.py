from aws_cdk import App, Stack, RemovalPolicy
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_glue as glue
from aws_cdk import aws_iam as iam
from aws_cdk.aws_s3_deployment import BucketDeployment, Source
import aws_cdk as cdk
from aws_cdk.aws_lambda import Runtime
from aws_cdk.aws_lambda_python_alpha import PythonFunction
from cdklabs.generative_ai_cdk_constructs import (
    bedrock)
from cdklabs.generative_ai_cdk_constructs.bedrock import (
    Agent, ApiSchema, BedrockFoundationModel,AgentActionGroup
)
from aws_cdk import aws_events as events
from aws_cdk import aws_cloudformation as cfn
from aws_cdk import aws_events_targets as events_targets
from aws_cdk import Duration
from cdklabs.generative_ai_cdk_constructs.bedrock import ActionGroupExecutor
from constructs import Construct
from agent_instruction_generator import analyze_csv_files,generate_instruction,invoke_claude_3_with_text
from Prep_Data import prep_data

class MyStack(Stack):
    #Start here

#CDK app definition here (Step 4)