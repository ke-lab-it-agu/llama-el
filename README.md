# Llama 2-based Entity Linking for Wikidata

## 要件

- Python 3.11.8
- replicate 0.23.1
- python-dotenv 1.0.1
- SPARQLWrapper 2.0.0

## インストール

```bash
git clone https://github.com/ke-lab-it-agu/llama-el.git
cd llama_el
python -m venv venv
# Windowsの場合
venv\Scripts\activate
# Unix, Linux, macOSの場合
source venv/bin/activate
pip install -r requirements.txt
```

## .env ファイルの作成

1. テキストエディタを開き、以下の内容をファイルに貼り付けます（`YOUR_API_TOKEN_HERE`は実際の Replicate API トークンに置き換えてください）:

   ```
   REPLICATE_API_TOKEN=YOUR_API_TOKEN_HERE
   ```

2. このファイルを`.env`という名前で保存し、プロジェクトのルートディレクトリに配置します。

API トークンは Replicate のウェブサイトから取得できます。セキュリティの観点から、`.env`ファイルは公開リポジトリにはアップロードしないでください。

## 実行方法

このプロジェクトには、テキストからエンティティ名と Wikipedia URL を生成するプロセス、Wikipedia URL を Wikidata ID に変換するプロセス、そして評価するプロセスが含まれています。それぞれのプロセスは以下のコマンドで実行できます。

- エンティティ名と Wikipedia URL を生成: `python main.py --task url --model [モデル名] --dataset [データセット名]`
- Wikipedia URL を Wikidata ID に変換: `python main.py --task id --model [モデル名] --dataset [データセット名]`
- 評価を実行: `python main.py --task eval --model [モデル名] --dataset [データセット名]`

利用可能なデータセット名は`lcquad2`, `simpleqs`, `webqsp`です。モデル名は`llama-2-70b`, `llama-2-13b`, `llama-2-7b`から選択できます。

例: エンティティ名と Wikipedia URL を生成する場合、Llama 2-70b モデルを使用して LC-QuAD2.0 データセットを指定するには、以下のように実行します。

```bash
python main.py --task url --model llama-2-70b --dataset lcquad2
```

`--task`の代わりに`-t`、`--dataset`の代わりに`-d`、`--model`の代わりに`-m`を使用することもできます。
