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
