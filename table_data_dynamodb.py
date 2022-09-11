import os
import csv
import boto3

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
                        "id": row['id'],
                        "name": row['name'],
                        "createdAt": row['createdAt'],
                        "updatedAt": row['updatedAt'],
                        "_lastChangedAt": row['_lastChangedAt'],
                        "_version": row['_version'],
                        "user_specific": row['user_specific'],
                        "description": row['description'] ,
                }
            )
main()
