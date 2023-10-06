# MachineLearning-app

Flaskの機械学習APIのリポジトリです
run_server.pyを実行後，以下のコマンドを入力してください．

```bash
curl http://0.0.0.0:5000/predict -X POST -H 'Content-Type:application/json' -d '{"feature":[1, 1, 1, 1]}'
```
```bash
{"Content-Type":"application/json","prediction":[2],"success":true}
```
これが出力結果
