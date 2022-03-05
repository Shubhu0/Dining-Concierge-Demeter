import json
import boto3
def lambda_handler(event, context):
    message = event['messages'][0]['unstructured']['text']
    client = boto3.client('lex-runtime')
    
    response = client.post_text(
        botAlias='BotAlias',
        botName='MyBot',
        userId='root',
        inputText=message)
    res = {
        'headers': {
            'Access-Control-Allow-Headers' : 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "messages" : [{
            "type" : "unstructured",
            "unstructured" : {
                "text" : response['message']
            }
        }]
    }
    return res
