import boto3
import json
import sys

def get_bedrock_response(prompt, model_id, tool_config):
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')

    response = bedrock.converse(
        modelId=model_id,
        messages=[{"role": "user", "content": [{"text": prompt}]}],
        toolConfig=tool_config,
        inferenceConfig={"maxTokens": 2000,  "temperature": 0.0}
    )

    return response['output']['message']['content'][0]['text']

tool_config = {
    "tools": [
        {
            "toolSpec": {
                "name": "get_stock_price",
                "description": "Gets the current stock price for the given ticker.",
                "inputSchema": {
                    "json": {
                        "type": "object",
                        "properties": {
                            "ticker": {
                                "type": "string",
                                "description": "Stock ticker symbol"
                            }
                        },
                        "required": [
                            "ticker"
                        ]
                    }
                }
            }
        }
    ]
}

tool_config["tools"].append({
    "toolSpec": {
        "name": "get_company_info",
        "description": "Gets company information (company name, industry, market cap, etc.) for the given ticker.",
        "inputSchema": {
            "json": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "Company ticker symbol"
                    }
                },
                "required": [
                    "ticker"
                ]
            }
        }
    }
})

def plan_company_analysis(ticker):
    prompt = f"You are an AI company analyst. Your goal is to perform a comprehensive analysis of {ticker}. Please outline your plan to achieve this goal."
    return get_bedrock_response(prompt, "anthropic.claude-3-5-sonnet-20240620-v1:0", tool_config)

ticker = sys.argv[1]
analysis_plan = plan_company_analysis(ticker)
print(analysis_plan)

