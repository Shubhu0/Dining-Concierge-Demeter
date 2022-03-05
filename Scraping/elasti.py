import boto3
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth


def put_into_elasticsearch():
    host = "search-elastic-jjc6x2mv3pknnjhgcl5d4zuv24.us-east-1.es.amazonaws.com"
    region = "us-east-1"
    service = "es"
    credentials = boto3.Session().get_credentials()
    awsauth = AWS4Auth('AKIAWUV5FAPNQ2GNZUT7', 'iKgN3NZVu4JNa2m/x+Oq6Ws0QN0pzWG0l8IP2pcT', 'us-east-1', service)

    es = Elasticsearch(
        hosts=[{'host': host, 'port': 443}],
        http_auth=('root', 'Shubh_1998'),
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1',aws_access_key_id= 'AKIAWUV5FAPNQ2GNZUT7',aws_secret_access_key= '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')
    table = dynamodb.Table("yelp-restaurants")
    response = None
    while True:
        if response is None:
            response = table.scan()
        else:
        
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        counter = 0
        for business in response['Items']:
            if not response:
          
                response = table.scan()
            restaurantID = business["Business ID"]
            doc = {
                "Business ID": restaurantID,
                "cuisine": business["cuisine"]
            }
            es.index(
                index="restaurants",
                doc_type="Restaurant",
                id=restaurantID,
                body=doc,
            )
            check = es.get(index="restaurants", doc_type="Restaurant", id=restaurantID)
            if check["found"]:
                print("Index %s succeeded" % restaurantID)
            counter = counter + 1

put_into_elasticsearch()
