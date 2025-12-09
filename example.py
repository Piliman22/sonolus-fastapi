from sonolus_fastapi import Sonolus
from sonolus_fastapi.pack import freepackpath

app = Sonolus(
    address='https://example.com', # サーバーアドレスを指定してください Specify your server address
    port=8000, # サーバーポートを指定してください Specify your server port
    enable_cors=True, # CORSを有効にするかどうか Whether to enable CORS
)

app.load(freepackpath) # Sonolus packのパスを指定してください Specify the path to the Sonolus pack

if __name__ == "__main__":
    app.run() # サーバーを起動します Start the server