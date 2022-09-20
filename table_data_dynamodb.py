import os
import csv
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb', 
        region_name='us-east-2',
        aws_access_key_id= os.environ.get('ACCESS_ID'),
        aws_secret_access_key= os.environ.get('ACCESS_KEY') )

tableName = 'Playlist'
filename = 'playlist.csv' 

def main():
    csvfile = open(filename)
    write_to_dynamo(csv.DictReader(csvfile))
    return print("Done")

def write_to_dynamo(rows):
    table = dynamodb.Table(tableName)
    with table.batch_writer() as batch:
        for row in rows:
            batch.put_item(
                Item={
                    "id": "Admin_" + row["name"] + "_" + str(datetime.now()),
                    "name": row["name"],
                    "created_by": row["created_by"],
                    "description": "Milo Playlist",
                    "user_specific": row["user_specific"]
                }
            )
main()
