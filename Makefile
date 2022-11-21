# help ターゲットをデフォルトのターゲットにする
.DEFAULT_GOAL := help

# env
ENV_LOCAL_FILE := docker-compose.env
ENV_LOCAL = $(shell cat $(ENV_LOCAL_FILE))

# docker
DOCKER_COMPOSE:=docker-compose.yml
DOCKER_EXEC:=docker exec -it

DB_CONTAINER_NAME:=flask_user-crud_db
SERVER_CONTAINER_NAME:=flask_user-crud_server

# dir
SRC_DIR:=./src

# volume
DATA_DIR:=./db/data

# rm
RM:=rm -rf

.PHONY: up
up: ## docker環境を立ち上げる
	$(ENV_LOCAL) docker-compose -f $(DOCKER_COMPOSE) up

.PHONY: down
down: ## dockerイメージを削除し、docker環境を閉じる
	docker-compose -f $(DOCKER_COMPOSE) down \
	--rmi all --volumes --remove-orphans

.PHONY: fclean
fclean:down del-volumes ## マウントしたデータを削除、またdockerイメージも削除する

.PHONY: re
re:fclean up ## 完全に初期化した状態でdocker環境を立ち上げる

.PHONY: del-volumes
del-volumes:del-data

.PHONY: del-data
del-data:
	$(RM) $(DATA_DIR)

.PHONY: attach-db
attach-db: ## dockerのdbコンテナにアクセスする
	$(DOCKER_EXEC) $(DB_CONTAINER_NAME) bash

.PHONY: attach-server
attach-server: ## dockerのserverコンテナにアクセスする
	$(DOCKER_EXEC) $(SERVER_CONTAINER_NAME) sh

.PHONY: help
help: ## コマンドの一覧を標示する
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'