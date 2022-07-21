import json
from concurrent.futures import ThreadPoolExecutor

import boto3


def call_lambda(n):
    client = boto3.client('lambda')
    payloadBytesArr = {"test": n}
    x = client.invoke(
        FunctionName="test-function",
        InvocationType="RequestResponse",
        Payload=json.dumps(payloadBytesArr)
    )
    print(x["Payload"].readlines())


def main():
    with ThreadPoolExecutor(50) as executor:
        for number in range(100):
            executor.map(call_lambda, [number])


if __name__ == '__main__':
    main()
