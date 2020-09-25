import json

def lambda_handler(event, context):
    operand_1 = event['queryStringParameters']['firstoperand']
    operand_2 = event['queryStringParameters']['secondoperand']
    operation = event['queryStringParameters']['operator']
    
    if(operation.lower() == 'plus'):
    	output_result = int(operand_1) + int(operand_2)
    	operation = "Addition"
    elif(operation.lower() == 'minus'):
    	output_result = int(operand_1) - int(operand_2)
    	operation = "Subtraction"
    elif(operation.lower() == 'divide'):
    	output_result = int(operand_1) / int(operand_2)
    	operation = "Division"
    elif(operation.lower() == 'multiply'):
    	output_result = int(operand_1) * int(operand_2)
    	operation = "Multiplication"
    else:
    	output_result = "Incorrect operation requested"
    	
    output_response = {}
    
    output_response['Result'] = output_result
    output_response['OperationPerformed'] = operation
    
    response_object = {}
    response_object['statusCode'] = 200
    response_object['headers'] = {}
    response_object['headers']['Content-Type'] = 'application/json'
    response_object['body'] = json.dumps(output_response)
    
    return response_object

