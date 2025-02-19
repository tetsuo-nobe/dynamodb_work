'''
  query を使用した項目の取得
  userId(パーティションキー)の値を指定して該当する項目を取得する
'''
import boto3
import botocore
from  myconfig import table_name
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from boto3.dynamodb.types import TypeDeserializer

# クエリーを実行する関数 1:パーティションキーのみ指定
def query_by_partitionKey(p_userId):
    
    ddbClient = boto3.client('dynamodb')
    # クエリー発行 
    response = ddbClient.query(
        TableName=table_name,
        KeyConditionExpression='userId = :userId',
        ExpressionAttributeValues={
            ':userId': {"N": str(p_userId)}
        },
        ProjectionExpression="gameId, score"
    )
    return response["Items"]

# クエリーを実行する関数 2:パーティションキーを指定、ソートキーに前方一致指定
def query_by_code(p_userId,p_code):
    
    ddbClient = boto3.client('dynamodb')
    # クエリー発行 
    response = ddbClient.query(
        TableName=table_name,
        KeyConditionExpression='userId = :userId and begins_with(gameId,:code)',
        ExpressionAttributeValues={
            ':userId': {"N": str(p_userId)},
            ':code': {"S": p_code},
        },
        ProjectionExpression="gameId, score"
    )
    return response["Items"]


## 項目の表示用のユーティリティ関数
def printScores(scores):
    if isinstance(scores, list):
        for score in scores:
            print(
                json.dumps(
                    {key: TypeDeserializer().deserialize(value) for key, value in score.items()},
                    cls=DecimalEncoder
                )
            )

# 項目を JSON に変換するためのヘルパークラス
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        if isinstance(o, set):  # <---resolving sets as lists
            return list(o)
        return super(DecimalEncoder, self).default(o)

# ここから実行開始
if __name__ == '__main__':
    try:
        # userId = 3 の項目を取得
        print("query: userId = 3")
        items = query_by_partitionKey(3)
        printScores(items)
        
        # userId = 3 and gameId が "NTD" で始まるの項目を取得
        print("query: userId = 3 and begins_with(gameId,'NTD')")
        items = query_by_code(3, "NTD")
        printScores(items)
    except botocore.exceptions.ClientError as err:
        print(err.response['Error']['Message'])
    except botocore.exceptions.ParamValidationError as error:
        print(error)  