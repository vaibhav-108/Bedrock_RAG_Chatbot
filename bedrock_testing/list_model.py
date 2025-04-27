import boto3

# Initialize client (ensure AWS credentials are configured)
bedrock = boto3.client(
    service_name="bedrock",
    region_name="us-east-1"  # Change to your region
)

# List available models
response = bedrock.list_foundation_models()

# Print results
print("Available Foundation Models:")
for model in response["modelSummaries"]:
    print(f"- {model['modelId']} (Provider: {model['providerName']})")