import boto3
import botocore.config
import json
import os
from datetime import datetime

# Load environment variables
REGION = os.getenv("AWS_REGION", "us-east-1")
S3_BUCKET = os.getenv("S3_BUCKET", "awsbedrockblogvishnu")

def blog_generate_using_bedrock(blogtopic: str) -> str:
    """Generates a blog using Amazon Bedrock and logs the full response for debugging."""
    prompt = f"Write a 200-word blog on the topic: {blogtopic}"

    body = {
        "inputText": prompt,  
        "textGenerationConfig": {
            "maxTokenCount": 512,
            "temperature": 0.5,
            "topP": 0.9
        }
    }

    try:
        bedrock = boto3.client(
            "bedrock-runtime",
            region_name=REGION,
            config=botocore.config.Config(read_timeout=300, retries={'max_attempts': 3})
        )

        response = bedrock.invoke_model(
            body=json.dumps(body),
            modelId="amazon.titan-text-lite-v1",
            contentType="application/json"
        )

        response_content = response.get('body').read()
        print("Bedrock Response:", response_content)  

        response_data = json.loads(response_content)
        blog_details = response_data.get('results', [{}])[0].get('outputText', '')

        print("Extracted Blog:", blog_details) 

        return blog_details

    except Exception as e:
        print(f"Error generating the blog: {e}")
        return ""



def save_blog_details_s3(s3_key: str, s3_bucket: str, generate_blog: str):
    """Saves the generated blog to an S3 bucket."""
    s3 = boto3.client('s3')

    try:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=generate_blog.encode('utf-8'))
        print(f"Blog saved to S3: {s3_key}")
    except Exception as e:
        print(f"Error saving to S3: {e}")

def lambda_handler(event, context):
    """AWS Lambda function handler."""
    try:
        print("Received Event:", json.dumps(event, indent=2))

        # Validate event body
        if not event.get('body'):
            return {'statusCode': 400, 'body': json.dumps({'error': 'Missing body in event'})}
        
        try:
            event_data = json.loads(event['body'])
        except json.JSONDecodeError:
            return {'statusCode': 400, 'body': json.dumps({'error': 'Invalid JSON input in body'})}

        blogtopic = event_data.get('blog_topic', 'Default Topic')

        # Generate blog
        generate_blog = blog_generate_using_bedrock(blogtopic)

        if generate_blog:
            current_time = datetime.now().strftime('%Y-%m-%d/%H%M%S')
            s3_key = f"blogs/{current_time}.txt"
            save_blog_details_s3(s3_key, S3_BUCKET, generate_blog)

            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Blog Generation completed', 'blog': generate_blog})
            }
        else:
            return {'statusCode': 500, 'body': json.dumps({'error': 'Blog generation failed'})}

    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': f"Server error: {str(e)}"})}
