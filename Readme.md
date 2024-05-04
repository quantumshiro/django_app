# django_app

djangoによるTODOサイト

## 事前準備

windows11+wsl2+Ubuntu22+DockerCompose+vscodeでの環境を構築してること。

## 環境構築手順

### 本リポジトリをクローンする

```bash
git clone https://github.com/sacky3105/django_app.git
cd django_app
```

後にファイル編集などをして、git通知が煩わしいときまたはプルリクしない場合は
作成したフォルダで以下のコマンドを入れる。

```bash
 rm -rf .git
```

### コンテナ稼働する

```bash
cd app
docker-compose build
docker-compose up -d
```

### 各種サイト確認する

http://localhost:8000/folders/1/tasks

## コンテナ起動する方法

`docker-compose.yml`が存在するフォルダーで以下のコマンドを実行する。

```bash
docker-compose up -d
```

## コンテナ停止する方法

`docker-compose.yml`が存在するフォルダーで以下のコマンドを実行する。

```bash
docker-compose stop
```

## コンテナ削除する方法

`docker-compose.yml`が存在するフォルダーで以下のコマンドを実行する。

```bash
docker-compose down
```

## 起動中のコンテナに入る

### webコンテナ

```bash
docker-compose exec web /bin/bash
```

### dbコンテナ

```bash
docker-compose exec db /bin/bash
```
