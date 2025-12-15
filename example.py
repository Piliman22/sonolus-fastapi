from sonolus_fastapi import Sonolus
from sonolus_fastapi.pack import freepackpath

sonolus = Sonolus(
    address='https://example.com', # サーバーアドレスを指定してください Specify your server address
    port=8000, # サーバーポートを指定してください Specify your server port
    enable_cors=True, # CORSを有効にするかどうか Whether to enable CORS
)

@sonolus.app.get("/hoge") # ルートエンドポイントを追加 Add root endpoint
def huga():
    return {"message": "huga"}

sonolus.load(freepackpath) # Sonolus packのパスを指定してください Specify the path to the Sonolus pack

if __name__ == "__main__":
    sonolus.run() # サーバーを起動します Start the server