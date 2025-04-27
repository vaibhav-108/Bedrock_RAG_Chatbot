import os
import json
import sys
import boto3
from botocore.exceptions import ClientError

bedrock=boto3.client(service_name="bedrock-runtime",
                     region_name="us-east-1")


prompt="""

        you are a polity expert now tell me how i can win the election?
"""

# payload={
    
#     "prompt": "[INST]"+prompt+"[/INST]",
#     # "messages": [{"role": "user", "content": prompt}],
#     "max_gen_len": 512,
#     "temperature": 0.3,
#     "top_p":0.9
# }

formatted_prompt = f"""
<｜begin▁of▁sentence｜><｜User｜>{prompt}<｜Assistant｜><think>\n
"""

body = json.dumps({
    "prompt": formatted_prompt,
    "max_tokens": 512,
    "temperature": 0.5,
    "top_p": 0.9,
})

# body=json.dumps(payload)

model_id= "us.deepseek.r1-v1:0"
# # model_id="meta.llama3-2-1b-instruct-v1:0"
# model_id="meta.llama3-1-8b-instruct-v1:0"

try:
    response=bedrock.invoke_model(
        body=body,
        modelId=model_id,
        accept="application/json",
        contentType="application/json"
    )

    response_body=json.loads(response["body"].read())
    response_text=response_body["choices"]
    
      # Print choices.
    for index, choice in enumerate(response_text):
        print(f"Choice {index + 1}\n----------")
        print(f"Text:\n{choice['text']}\n")
        print(f"Stop reason: {choice['stop_reason']}\n")
    
except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)