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
    def __init__(self, scope: App, id: str,zip_file_name: str, region: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        account_id = cdk.Stack.of(self).account
        data_folder_name=zip_file_name.replace('.zip','')
        agent_name = f"agent_{data_folder_name.lower()}"
        suffix = f"{region}-{account_id}-{agent_name.lower()}"
        lambda_role_name = f'{agent_name}-lambda-role-{suffix}'
        agent_role_name = f'AmazonBedrockExecutionRoleForAgents_{suffix}'
        lambda_name = f'{agent_name}-{suffix}'
        foundation_model = BedrockFoundationModel('anthropic.claude-3-sonnet-20240229-v1:0', supports_agents=True)
        prep_data(data_folder_name)
        glue_database_name = f"{data_folder_name.lower()}"

        #Start here (Step 0)

#CDK app definition here (Step 4)