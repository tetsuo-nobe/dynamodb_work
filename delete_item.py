'''
  delete_item による項目の削除
  プライマリキーの値を指定して該当する項目を削除する
'''
import boto3
import botocore
from  myconfig import table_name


# delete_item を実行する関数
def delete_score_item(p_userId,p_gameId):
    
    ddbClient = boto3.client('dynamodb')
    # delete_item 発行
    ddbClient.delete_item(
        TableName = table_name,
        Key       = {
                     'userId': {'N': str(p_userId)},
                     'gameId': {'S': p_gameId},
        }
    )

# ここから実行開始
if __name__ == '__main__':
    try:
        delete_score_item(3,"NTD-001")
        print('Deleted.')
    except botocore.exceptions.ClientError as err:
        print(err.response['Error']['Message'])
    except botocore.exceptions.ParamValidationError as error:
        print(error)  
