def lambda_handler(event, context):
    print("Event: {}".format(event))

    response = {
        'statusCode': 200,
        'body': 'Hello, World!'
    }

    return response
