-- DB切り替え
\c "hoge"

--テーブルを作成

CREATE TABLE "users" (
  "id"         SERIAL NOT NULL PRIMARY KEY,
  "name"       VARCHAR(255) NOT NULL,
  "age"        INTEGER NOT NULL
);

-- --テーブルにデータを挿入
INSERT INTO "users" ("name", "age") 
VALUES ('doer', 12);

INSERT INTO "users" ("name", "age") 
VALUES ('doshisha', 30);
