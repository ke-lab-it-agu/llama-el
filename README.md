# Llama 2-based Entity Linking for Wikidata

## バージョン

- Python 3.12.2
- replicate 0.23.1
- python-dotenv 1.0.1
- SPARQLWrapper 2.0.0
- torch 2.2.1
- transformers 4.38.2
- sentencepiece 0.2.0
- accelerate 0.27.2
- protobuf 4.25.3
- pandas 2.2.1
- openpyxl 3.1.2

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

このプロジェクトには、テキストからエンティティ名と Wikipedia URL を生成するプロセス、Wikipedia URL を Wikidata ID に変換するプロセス、そして評価するプロセスが含まれています。

### エンティティ名と Wikipedia URL を生成

```bash
python main.py -t url -d <dataset> -m <model> -l <language>
```

- `<dataset>`: `lcquad2`, `simpleqs`, `webqsp`
- `<model>`: `llama-2-7b`, `llama-2-13b`, `llama-2-70b`, `Swallow-2-13b`
- `<language>`: `english`, `japanese`
- e.g. `python main.py -t url -d webqsp -m llama-2-70b -l english`

### Wikipedia URL を Wikidata ID に変換

```bash
python main.py -t id -d <dataset> -m <model> -l <language>
```

- e.g. `python main.py -t id -d webqsp -m llama-2-70b -l english`

### 評価

```bash
python main.py -t eval -d <dataset> -m <model> -l <language>
```

- e.g. `python main.py -t eval -d webqsp -m llama-2-70b -l english`

## エラー対応

`-t url`を実行した際に`json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)`というエラーメッセージが表示された場合は、以下の手順で対応してください。

1. `add_id_to_json.py`スクリプトを実行して、JSON ファイルに ID を追加します。
2. `wikipedia_el.py`の 57 行目にある引数を`data[id:]`として修正します。ここで、`id`は最後に成功した ID の番号です。
3. 修正後、`-t url`をもう一度実行してください。

これにより、エラーが発生した場所から処理を再開できます。
