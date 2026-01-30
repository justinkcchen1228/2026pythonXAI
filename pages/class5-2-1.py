import openai # pip install openai
from dotenv import load_dotenv
import os

load_dotenv # 載入 .env檔案內容

# 設定 API 金鑰
openai.api_key = os.getenv("OPEN_API_KEY")