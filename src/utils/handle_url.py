import os
from dotenv import load_dotenv
load_dotenv()
import ozon3 as ooo

TOKEN = os.environ.get('TOKEN')

api = ooo.Ozon3(TOKEN)