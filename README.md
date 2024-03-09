# Llama 2-based Entity Linking for Wikidata

## 要件

- Python 3.12.2
- replicate 0.23.1
- python-dotenv 1.0.1
- SPARQLWrapper 2.0.0
- torch 2.2.1
- transformers 4.38.2
- sentencepiece 0.2.0
- accelerate 0.27.2
- protobuf 4.25.3

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

   ```text
   REPLICATE_API_TOKEN=YOUR_API_TOKEN_HERE
   ```

2. このファイルを`.env`という名前で保存し、プロジェクトのルートディレクトリに配置します。

API トークンは Replicate の[ウェブサイト](https://replicate.com/signin?next=%2Faccount%2Fapi-tokens)から取得できます。

## 実行方法

このプロジェクトには、テキストからエンティティ名と Wikipedia URL を生成するプロセス、Wikipedia URL を Wikidata ID に変換するプロセス、そして評価するプロセスが含まれています。それぞれのプロセスは以下のコマンドで実行できます。

- エンティティ名と Wikipedia URL を生成: `python main.py --task url --model [モデル名] --dataset [データセット名] --language [言語名]`
- Wikipedia URL を Wikidata ID に変換: `python main.py --task id --model [モデル名] --dataset [データセット名] --language [言語名]`
- 評価を実行: `python main.py --task eval --model [モデル名] --dataset [データセット名] --language [言語名]`

利用可能なデータセット名は`lcquad2`, `simpleqs`, `webqsp`です。モデル名は`llama-2-70b`, `llama-2-13b`, `llama-2-7b`, `Swallow-7b`から選択できます。対象言語は`english`または`japanese`です。

例: エンティティ名と Wikipedia URL を生成する場合、Llama 2-70B モデルを使用して 英語の LC-QuAD2.0 データセットを指定するには、以下のように実行します。

```bash
python main.py --task url --model llama-2-70b --dataset lcquad2 --language english
```

`--task`の代わりに`-t`、`--dataset`の代わりに`-d`、`--model`の代わりに`-m`、`--language`の代わりに`-l`を使用することもできます。

## エラー対応

`-t url`を実行した際に`json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)`というエラーメッセージが表示された場合は、以下の手順で対応してください。

1. `add_id_to_json.py`スクリプトを実行して、JSON ファイルに ID を追加します。
2. `wikipedia_el.py`の 57 行目にある引数を`data[id:]`として修正します。ここで、`id`は最後に成功した ID の番号です。
3. 修正後、`-t url`をもう一度実行してください。

これにより、エラーが発生した場所から処理を再開できます。
