# linearAlgebraContent

## みんなで頑張ろうぜ！！！

## 環境構築について

環境構築は現状Dockerでやるのがおすすめです。

Macユーザーの場合Docker For Macをインストールしてください。（DesktopのやつでOK）

dockerが使える状態になったらsetup_for_docker_env.shを開きます。

※このファイルは現状実行するためというよりもコマンドを見るためにあるような感じです。

以下コマンドを実行します。

```
docker-compose up --no-recreate
```

別タブで以下コマンドを実行すればコンテナ内で作業できます。

```
docker exec -it linear-algebra-content /bin/bash
```

無事にコンテナ内に入ったら以下コマンドを実行してローカルサーバを起動します。

```
uvicorn main:app --reload
```
