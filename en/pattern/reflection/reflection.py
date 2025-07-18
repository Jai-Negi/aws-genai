import boto3

def get_bedrock_response(prompt, model_id):
    session = boto3.Session()
    bedrock = session.client(service_name='bedrock-runtime')

    response = bedrock.converse(
        modelId=model_id,
        messages=[{"role": "user", "content": [{"text": prompt}]}],
        inferenceConfig={"maxTokens": 2000,  "temperature": 0.0}
    )

    return response['output']['message']['content'][0]['text']

def solve_math_problem(problem):
    prompt = f"Please solve the following math problem:\nProblem: {problem}"
    return get_bedrock_response(prompt, "anthropic.claude-3-5-haiku-20241022-v1:0")

def validate_solution(problem, solution):
    prompt = f"Please review the following math problem and its solution:\nProblem: {problem}\nSolution: {solution}"
    return get_bedrock_response(prompt, "anthropic.claude-3-5-sonnet-20240620-v1:0")

math_problem = "Solve the equation 2x + 5 = 13"

solution = solve_math_problem(math_problem)
print(f"AI Solution: {solution}\n\n")

validation = validate_solution(math_problem, solution)
print(f"Validation Result: {validation}")

