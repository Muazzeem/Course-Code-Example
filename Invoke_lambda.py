import boto3
import json

lambda_client = boto3.client('lambda')
payload = {
    "data": "Test"
}
invoke_response = lambda_client.invoke(
    FunctionName="function-name",
    InvocationType="RequestResponse",
    Payload=json.dumps(payload)
)
print(invoke_response)
print(invoke_response["Payload"].readlines())
