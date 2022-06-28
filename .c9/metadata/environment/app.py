{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":65,"position":65,"stack":[[{"start":{"row":0,"column":0},"end":{"row":19,"column":5},"action":"insert","lines":["import json","import boto3","s3 = boto3.client('s3')","def create_bucket(event, context): # ?name=<BucketName>","    bucketName = event[\"queryStringParameters\"][\"name\"]","    s3.create_bucket(Bucket=bucketName)","    return {","        'statusCode': 200,","        'body': json.dumps(\"hello from lambda\")","    }","","def list_buckets(event, context):","    buckets = s3.list_buckets()","    bucket_list=[]","    for bucket in buckets[\"Buckets\"]:","        bucket_list.append(bucket[\"Name\"])","    return {","        'statusCode': 200,","        'body': json.dumps(bucket_list)","    }"],"id":1}],[{"start":{"row":3,"column":0},"end":{"row":10,"column":0},"action":"remove","lines":["def create_bucket(event, context): # ?name=<BucketName>","    bucketName = event[\"queryStringParameters\"][\"name\"]","    s3.create_bucket(Bucket=bucketName)","    return {","        'statusCode': 200,","        'body': json.dumps(\"hello from lambda\")","    }",""],"id":2},{"start":{"row":2,"column":23},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":2,"column":23},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":4,"column":33},"end":{"row":8,"column":42},"action":"remove","lines":["","    buckets = s3.list_buckets()","    bucket_list=[]","    for bucket in buckets[\"Buckets\"]:","        bucket_list.append(bucket[\"Name\"])"],"id":4}],[{"start":{"row":7,"column":27},"end":{"row":7,"column":38},"action":"remove","lines":["bucket_list"],"id":5},{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"insert","lines":["e"]},{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":["v"]},{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"insert","lines":["e"]},{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"insert","lines":["n"]},{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":0},"end":{"row":8,"column":5},"action":"remove","lines":["import json","import boto3","s3 = boto3.client('s3')","","def list_buckets(event, context):","    return {","        'statusCode': 200,","        'body': json.dumps(event)","    }"],"id":6},{"start":{"row":0,"column":0},"end":{"row":32,"column":5},"action":"insert","lines":["import json","import boto3","dynamodb = boto3.resource('dynamodb')","def adopt(event, context):","    body = json.loads(event[\"body\"])","    pet = body[\"pet\"] # pet_A","    owner = body[\"owner\"] # owner_01","    year = body[\"year\"] # 2020","    employee = body[\"employee\"] # employee_A","    table = dynamodb.Table('petStore')","    ","    table.put_item(","       Item={","            'pk': owner,","            'sk': pet,","            'employee': employee,","            'year': year","        }","    )","    ","    table.put_item(","       Item={","            'pk': f'{employee}#{owner}#{year}',","            'sk': pet,","            'employee': employee,","            'year': year","        }","    )","    ","    return {","        'statusCode': 200,","        'body': json.dumps(\"data saved\")","    }"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":9},"action":"remove","lines":["adopt"],"id":7},{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":["s"]},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["a"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["v"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["e"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["-"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["u"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["s"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["e"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["r"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":13},"action":"remove","lines":["save-user"],"id":8},{"start":{"row":3,"column":4},"end":{"row":3,"column":13},"action":"insert","lines":["save_user"]}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":7},"action":"remove","lines":["pet"],"id":9},{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["u"]},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["s"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["e"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["r"]}],[{"start":{"row":5,"column":17},"end":{"row":5,"column":20},"action":"remove","lines":["pet"],"id":10},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["u"]},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["s"]},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["e"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["r"]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":9},"action":"remove","lines":["owner"],"id":11},{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["c"]},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["i"]}],[{"start":{"row":6,"column":15},"end":{"row":6,"column":20},"action":"remove","lines":["owner"],"id":12},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["c"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["i"]}],[{"start":{"row":6,"column":30},"end":{"row":8,"column":44},"action":"remove","lines":["","    year = body[\"year\"] # 2020","    employee = body[\"employee\"] # employee_A"],"id":13}],[{"start":{"row":6,"column":21},"end":{"row":6,"column":30},"action":"remove","lines":[" owner_01"],"id":14},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"remove","lines":["#"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"remove","lines":[" "]},{"start":{"row":5,"column":23},"end":{"row":5,"column":31},"action":"remove","lines":[" # pet_A"]}],[{"start":{"row":7,"column":28},"end":{"row":7,"column":36},"action":"remove","lines":["petStore"],"id":15},{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":["e"]},{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"insert","lines":["l"]},{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"insert","lines":["e"]},{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"insert","lines":["c"]},{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"insert","lines":["t"]},{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"insert","lines":["i"]}],[{"start":{"row":7,"column":28},"end":{"row":7,"column":34},"action":"remove","lines":["electi"],"id":16},{"start":{"row":7,"column":28},"end":{"row":7,"column":41},"action":"insert","lines":["elections2022"]}],[{"start":{"row":11,"column":18},"end":{"row":11,"column":23},"action":"remove","lines":["owner"],"id":17},{"start":{"row":11,"column":18},"end":{"row":11,"column":19},"action":"insert","lines":["u"]},{"start":{"row":11,"column":19},"end":{"row":11,"column":20},"action":"insert","lines":["s"]},{"start":{"row":11,"column":20},"end":{"row":11,"column":21},"action":"insert","lines":["e"]},{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"insert","lines":["r"]}],[{"start":{"row":12,"column":18},"end":{"row":12,"column":21},"action":"remove","lines":["pet"],"id":18},{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"insert","lines":["c"]},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["i"]}],[{"start":{"row":12,"column":20},"end":{"row":14,"column":24},"action":"remove","lines":[",","            'employee': employee,","            'year': year"],"id":19}],[{"start":{"row":15,"column":0},"end":{"row":23,"column":5},"action":"remove","lines":["    ","    table.put_item(","       Item={","            'pk': f'{employee}#{owner}#{year}',","            'sk': pet,","            'employee': employee,","            'year': year","        }","    )"],"id":20},{"start":{"row":14,"column":5},"end":{"row":15,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":3,"column":9},"end":{"row":3,"column":13},"action":"remove","lines":["user"],"id":21},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["v"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["o"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["t"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["e"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":9},"end":{"row":3,"column":14},"action":"remove","lines":["votes"],"id":22},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["u"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["s"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["e"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["r"]}],[{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["-"],"id":23}],[{"start":{"row":19,"column":5},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]},{"start":{"row":20,"column":4},"end":{"row":21,"column":0},"action":"insert","lines":["",""]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":21,"column":4},"end":{"row":47,"column":5},"action":"insert","lines":["import json","import boto3","from time import gmtime, strftime","","dynamodb = boto3.resource('dynamodb')","table = dynamodb.Table('Proyect')","now = strftime(\"%a, %d %b %Y %H:%M:%S +0000\", gmtime())","","def lambda_handler(event, context):","    username = event['username']","    ci = event['ci']","    votes = event['votes']","    center = event['center']","    city = event['city']","    response = table.put_item(","        Item={","            'username': username,","            'ci': ci,","            'numberOfvotes': votes,","            'center': center,","            'city': city,","            'LatestGreetingTime':now","            })","    return {","        'statusCode': 200,","        'body': json.dumps('Registrando votos del centro ' + center)","    }"],"id":25}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "],"id":26},{"start":{"row":20,"column":4},"end":{"row":21,"column":0},"action":"remove","lines":["",""]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":20,"column":0},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":27}],[{"start":{"row":29,"column":4},"end":{"row":29,"column":18},"action":"remove","lines":["lambda_handler"],"id":28},{"start":{"row":29,"column":4},"end":{"row":29,"column":13},"action":"insert","lines":["save_user"]}],[{"start":{"row":0,"column":0},"end":{"row":19,"column":5},"action":"remove","lines":["import json","import boto3","dynamodb = boto3.resource('dynamodb')","def save_user(event, context):","    body = json.loads(event[\"body\"])","    user = body[\"user\"]","    ci = body[\"ci\"]","    table = dynamodb.Table('elections-2022')","    ","    table.put_item(","       Item={","            'pk': user,","            'sk': ci","        }","    )","    ","    return {","        'statusCode': 200,","        'body': json.dumps(\"data saved\")","    }"],"id":29}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"remove","lines":["",""],"id":30},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":5,"column":24},"end":{"row":5,"column":31},"action":"remove","lines":["Proyect"],"id":31},{"start":{"row":5,"column":24},"end":{"row":5,"column":40},"action":"insert","lines":["elections-2022-2"]}],[{"start":{"row":0,"column":0},"end":{"row":26,"column":5},"action":"remove","lines":["import json","import boto3","from time import gmtime, strftime","","dynamodb = boto3.resource('dynamodb')","table = dynamodb.Table('elections-2022-2')","now = strftime(\"%a, %d %b %Y %H:%M:%S +0000\", gmtime())","","def save_user(event, context):","    username = event['username']","    ci = event['ci']","    votes = event['votes']","    center = event['center']","    city = event['city']","    response = table.put_item(","        Item={","            'username': username,","            'ci': ci,","            'numberOfvotes': votes,","            'center': center,","            'city': city,","            'LatestGreetingTime':now","            })","    return {","        'statusCode': 200,","        'body': json.dumps('Registrando votos del centro ' + center)","    }"],"id":32},{"start":{"row":0,"column":0},"end":{"row":28,"column":5},"action":"insert","lines":["import json","import boto3","from time import gmtime, strftime","","dynamodb = boto3.resource('dynamodb')","table = dynamodb.Table('Proyect')","now = strftime(\"%a, %d %b %Y %H:%M:%S +0000\", gmtime())","","def lambda_handler(event, context):","    username = event['username']","    ci = event['ci']","    votes = event['votes']","    center = event['center']","    city = event['city']","    image = event['image']","    response = table.put_item(","        Item={","            'username': username,","            'ci': ci,","            'numberOfvotes': votes,","            'center': center,","            'city': city,","            'image': image,","            'LatestGreetingTime':now","            })","    return {","        'statusCode': 200,","        'body': json.dumps('Registrando votos del centro ' + center)","    }"]}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":18},"action":"remove","lines":["lambda_handler"],"id":33},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["f"]},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["u"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["n"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["c"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["t"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["i"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["o"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["n"]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["-"]}],[{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["v"],"id":34},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["o"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["t"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["e"]},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["s"]}],[{"start":{"row":28,"column":5},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":35},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]},{"start":{"row":29,"column":4},"end":{"row":30,"column":0},"action":"insert","lines":["",""]},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]},{"start":{"row":30,"column":4},"end":{"row":31,"column":0},"action":"insert","lines":["",""]},{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"insert","lines":["    "]},{"start":{"row":31,"column":4},"end":{"row":32,"column":0},"action":"insert","lines":["",""]},{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":30,"column":4},"end":{"row":48,"column":9},"action":"insert","lines":["def lambda_handler(event, context):","    username = event[\"queryStringParameters\"][\"username\"]","    ci = event[\"queryStringParameters\"][\"ci\"]","    response = dynamodb_client.get_item(","        TableName='Proyect',","        Key={","            'username':{'S':username},","            'ci':{'S':ci}","        })","    if 'Item' in response:","        return {","            'statusCode': 200,","            'body': json.dumps('Bienvenido ' + username)","        }","    else:","        return {","            'statusCode': 200,","            'body': json.dumps('No existe el elemento')","        }"],"id":36}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"remove","lines":["    "],"id":37},{"start":{"row":29,"column":4},"end":{"row":30,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":29,"column":4},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":38},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"remove","lines":["    "],"id":39}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":18},"action":"remove","lines":["lambda_handler"],"id":40},{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"insert","lines":["f"]},{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"insert","lines":["u"]},{"start":{"row":30,"column":6},"end":{"row":30,"column":7},"action":"insert","lines":["n"]},{"start":{"row":30,"column":7},"end":{"row":30,"column":8},"action":"insert","lines":["c"]},{"start":{"row":30,"column":8},"end":{"row":30,"column":9},"action":"insert","lines":["t"]},{"start":{"row":30,"column":9},"end":{"row":30,"column":10},"action":"insert","lines":["i"]},{"start":{"row":30,"column":10},"end":{"row":30,"column":11},"action":"insert","lines":["o"]},{"start":{"row":30,"column":11},"end":{"row":30,"column":12},"action":"insert","lines":["n"]},{"start":{"row":30,"column":12},"end":{"row":30,"column":13},"action":"insert","lines":["-"]}],[{"start":{"row":30,"column":12},"end":{"row":30,"column":13},"action":"remove","lines":["-"],"id":41}],[{"start":{"row":30,"column":12},"end":{"row":30,"column":13},"action":"insert","lines":["_"],"id":42},{"start":{"row":30,"column":13},"end":{"row":30,"column":14},"action":"insert","lines":["u"]},{"start":{"row":30,"column":14},"end":{"row":30,"column":15},"action":"insert","lines":["s"]},{"start":{"row":30,"column":15},"end":{"row":30,"column":16},"action":"insert","lines":["e"]},{"start":{"row":30,"column":16},"end":{"row":30,"column":17},"action":"insert","lines":["r"]},{"start":{"row":30,"column":17},"end":{"row":30,"column":18},"action":"insert","lines":["s"]}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"remove","lines":["-"],"id":43}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["_"],"id":44}],[{"start":{"row":5,"column":30},"end":{"row":5,"column":31},"action":"remove","lines":["t"],"id":45},{"start":{"row":5,"column":29},"end":{"row":5,"column":30},"action":"remove","lines":["c"]},{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"remove","lines":["e"]},{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"remove","lines":["y"]},{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"remove","lines":["o"]},{"start":{"row":5,"column":25},"end":{"row":5,"column":26},"action":"remove","lines":["r"]},{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"remove","lines":["P"]}],[{"start":{"row":5,"column":24},"end":{"row":5,"column":46},"action":"insert","lines":["elections-project-2022"],"id":46}],[{"start":{"row":34,"column":19},"end":{"row":34,"column":26},"action":"remove","lines":["Proyect"],"id":47},{"start":{"row":34,"column":19},"end":{"row":34,"column":41},"action":"insert","lines":["elections-project-2022"]}],[{"start":{"row":27,"column":68},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":48},{"start":{"row":28,"column":0},"end":{"row":28,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":28,"column":8},"end":{"row":31,"column":3},"action":"insert","lines":["'headers': {","      'Content-Type': 'application/json',","      'Access-Control-Allow-Origin': '*'","  }"],"id":49}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "],"id":50},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "],"id":51},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":29,"column":13},"end":{"row":29,"column":14},"action":"remove","lines":[" "],"id":52},{"start":{"row":29,"column":12},"end":{"row":29,"column":13},"action":"remove","lines":[" "]}],[{"start":{"row":30,"column":12},"end":{"row":30,"column":13},"action":"remove","lines":[" "],"id":53},{"start":{"row":30,"column":12},"end":{"row":30,"column":13},"action":"remove","lines":[" "]}],[{"start":{"row":31,"column":9},"end":{"row":31,"column":10},"action":"remove","lines":[" "],"id":54},{"start":{"row":31,"column":8},"end":{"row":31,"column":9},"action":"remove","lines":[" "]}],[{"start":{"row":46,"column":56},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":55},{"start":{"row":47,"column":0},"end":{"row":47,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":47,"column":12},"end":{"row":50,"column":9},"action":"insert","lines":["'headers': {","            'Content-Type': 'application/json',","            'Access-Control-Allow-Origin': '*'","        }"],"id":56}],[{"start":{"row":48,"column":12},"end":{"row":48,"column":16},"action":"insert","lines":["    "],"id":57}],[{"start":{"row":49,"column":12},"end":{"row":49,"column":16},"action":"insert","lines":["    "],"id":58}],[{"start":{"row":50,"column":8},"end":{"row":50,"column":12},"action":"insert","lines":["    "],"id":59}],[{"start":{"row":55,"column":55},"end":{"row":56,"column":0},"action":"insert","lines":["",""],"id":60},{"start":{"row":56,"column":0},"end":{"row":56,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":56,"column":12},"end":{"row":59,"column":9},"action":"insert","lines":["'headers': {","            'Content-Type': 'application/json',","            'Access-Control-Allow-Origin': '*'","        }"],"id":61}],[{"start":{"row":59,"column":8},"end":{"row":59,"column":12},"action":"insert","lines":["    "],"id":62}],[{"start":{"row":58,"column":12},"end":{"row":58,"column":16},"action":"insert","lines":["    "],"id":63}],[{"start":{"row":57,"column":16},"end":{"row":57,"column":20},"action":"insert","lines":["    "],"id":64}],[{"start":{"row":57,"column":16},"end":{"row":57,"column":20},"action":"remove","lines":["    "],"id":65}],[{"start":{"row":57,"column":12},"end":{"row":57,"column":16},"action":"insert","lines":["    "],"id":66}]]},"ace":{"folds":[],"scrolltop":572.5,"scrollleft":0,"selection":{"start":{"row":57,"column":16},"end":{"row":57,"column":16},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":37,"state":"start","mode":"ace/mode/python"}},"timestamp":1656425725318,"hash":"1395c1600378f2c52ec1e1a78df3e6ecf8cbf8be"}