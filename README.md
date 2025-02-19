# Amazon DynamoDB のワーク

* このワークは、指定された AWS アカウントと IAM ユーザー/パスワードを使用して実施して下さい。
* ワークの環境は、許可されている期限内でのみ利用可能ですのでご了承ください。
---

## ワークの目的

* Amazon DynamoDB について、下記の操作をハンズオンで体験します。
    - AWS SDK for Python (boto3) を使用した Python のコードから Amazon DynamoDB のテーブルを操作する

![](images/sdk.png)

---

### 手順

#### 準備

1. インストラクターのガイドに基づき、開発環境を用意し、アクセスします。

1. 開発環境のターミナルで下記のコマンドを実行します。
    - git clone コマンドで GitHub リポジトリから AWS SDK for Python (boto3) のサンプルを取得します。
    - git コマンドは今回使用する開発環境に組み込まれています。


    ```
    git clone https://github.com/tetsuo-nobe/dynamodb_work.git
    ```

1. AWS SDK for Python (boto3) のサンプルが存在するフォルダに移動します。サンプルは必ずこのフォルダから実行します。

    ```
    cd dynamodb_work
    ```  

1. 使用する DynamoDB のテーブル名をユニークにするため、テーブル名の設定を変更します。
    - **注意：この手順は使用する環境により不要な場合があります。インストラクターのガイドに基づき必要な場合のみ実施してください。**

    - **myconfig.py** を開きます。
    - `table_name = 'score'` の行で、scoreの後に 2 桁の自分の番号を追記して下さい。
        - 例: `table_name = 'score28'`
    - Ctrl + s キーでファイルを保存します

#### テーブルの作成

1. 下図のようなテーブルを作成します。


![](images/table.png)


1. **create_table.py** を開きます。

1. インストラクターの説明を聴きながらコードの内容を概要レベルで確認します。

1. 開発環境のターミナルで、次のコマンドを実行します。

    ```
    python3  create_table.py
    ```  

1. テーブル作成の完了のメッセージ出力を確認します。
    - AWS マネジメントコンソールでも確認してみましょう。

#### 項目の作成

1. 作成したテーブルに項目を作成します。


1. **put_item.py** を開きます。

1. インストラクターの説明を聴きながらコードの内容を概要レベルで確認します。

1. 開発環境のターミナルで、次のコマンドを実行します。

    ```
    python3  put_item.py
    ```  

1. 項目作成の完了のメッセージ出力を確認します。
    - AWS マネジメントコンソールでも確認してみましょう。
    - 
#### 項目の取得

1. テーブルからキーを指定して項目を取得します。


1. **get_item.py** を開きます。

1. インストラクターの説明を聴きながらコードの内容を概要レベルで確認します。

1. 開発環境のターミナルで、次のコマンドを実行します。

    ```
    python3  get_item.py
    ```  

1. 出力内容を確認します。

#### 項目の取得

1. テーブルからプライマリキーを指定して項目を取得します。
    - このサンプルの場合、パーティションキーとソートキーを指定します。
    - 項目取得時のパターンについて確認しましょう。

1. **get_item.py** を開きます。

1. インストラクターの説明を聴きながらコードの内容を概要レベルで確認します。

1. 開発環境のターミナルで、次のコマンドを実行します。

    ```
    python3  get_item.py
    ```  

1. 出力内容を確認します。

#### テーブルへの Query 発行

1. Query を発行して該当する項目を取得します。
    - get_item との違いを確認しましょう。
    - Query で指定できる条件について確認しましょう。

1. **query.py** を開きます。

1. インストラクターの説明を聴きながらコードの内容を概要レベルで確認します。

1. 開発環境のターミナルで、次のコマンドを実行します。

    ```
    python3  query.py
    ```  

1. 出力内容を確認します。

#### テーブルへのグローバルセカンダリインデックスの追加

1. 下図のようなグローバルセカンダリインデックスを作成します。


![](images/gsi.png)


1. **add_gsi.py** を開きます。

1. インストラクターの説明を聴きながらコードの内容を概要レベルで確認します。

1. 開発環境のターミナルで、次のコマンドを実行します。

    ```
    python3  add_gsi.py
    ```  

1. 出力内容を確認します。 


#### グローバルセカンダリインデックスへの Query 発行

1. Query を発行して該当する項目を取得します。
    - テーブルに対して Query を発行する場合との違いを確認しましょう。

1. **query_gsi.py** を開きます。

1. インストラクターの説明を聴きながらコードの内容を概要レベルで確認します。

1. 開発環境のターミナルで、次のコマンドを実行します。

    ```
    python3  query_gsi.py
    ```  

1. 出力内容を確認します。

#### 項目の更新

1. テーブルからプライマリキーを指定して項目を更新します。
    - このサンプルの場合、パーティションキーとソートキーを指定します。

1. **update_item.py** を開きます。

1. インストラクターの説明を聴きながらコードの内容を概要レベルで確認します。

1. 開発環境のターミナルで、次のコマンドを実行します。

    ```
    python3  update_item.py
    ```  

1. 出力内容を確認します。

#### 項目の削除

1. テーブルからプライマリキーを指定して項目を削除します。
    - このサンプルの場合、パーティションキーとソートキーを指定します。

1. **delete_item.py** を開きます。

1. インストラクターの説明を聴きながらコードの内容を概要レベルで確認します。

1. 開発環境のターミナルで、次のコマンドを実行します。

    ```
    python3  delete_item.py
    ```  

1. 出力内容を確認します。

#### テーブルの削除

1. サンプルで使用したテーブルを削除します

1. **delete_table.py** を開きます。

1. インストラクターの説明を聴きながらコードの内容を概要レベルで確認します。

1. 開発環境のターミナルで、次のコマンドを実行します。

    ```
    python3  delete_table.py
    ```  

1. 出力内容を確認します。

---

#### ワークは以上です。お疲れさまでした！