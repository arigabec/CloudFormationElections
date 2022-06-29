import json
import boto3
from time import gmtime, strftime

dynamodb = boto3.resource('dynamodb')
dynamodb_client = boto3.client('dynamodb')
table = dynamodb.Table('elections-project-2022')
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

def function_votes(event, context):
    username = event['username']
    ci = event['ci']
    votes = event['votes']
    center = event['center']
    city = event['city']
    image = event['image']
    response = table.put_item(
        Item={
            'username': username,
            'ci': ci,
            'numberOfvotes': votes,
            'center': center,
            'city': city,
            'image': image,
            'LatestGreetingTime':now
            })
    return {
        'statusCode': 200,
        'body': json.dumps('Registrando votos del centro ' + center),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    
def function_users(event, context):
    username = event["queryStringParameters"]["username"]
    ci = event["queryStringParameters"]["ci"]
    response = dynamodb_client.get_item(
        TableName='elections-project-2022',
        Key={
            'username':{'S':username},
            'ci':{'S':ci}
        })
    if 'Item' in response:
        return {
            'statusCode': 200,
            'body': json.dumps('Bienvenido ' + username),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps('No existe el elemento')
        }
    
    