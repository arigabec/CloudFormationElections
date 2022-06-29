import json
import boto3
from time import gmtime, strftime

dynamodb = boto3.resource('dynamodb')
dynamodb_client = boto3.client('dynamodb')
table = dynamodb.Table('elections-project-2022')
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

def function_votes(event, context):
    body = json.loads(event["body"])
    username = body["username"]
    ci = body["ci"]
    votes = body["votes"]
    center = body["center"]
    city = body["city"]
    image = body["image"]
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
        'body': json.dumps('Registrando votos del centro ' + center)
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
            'body': json.dumps('Bienvenido ' + username)
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps('No existe el elemento')
        }
    
    