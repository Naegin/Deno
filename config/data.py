from json import load
from collections import namedtuple
from dotenv import load_dotenv

__all__ = ("Config")

def get(file, type="normal"):
    try:
      with open(file, encoding="utf8") as data:
          if type == "obj":
             return load(data, object_hook=lambda d: namedtuple("X", d.keys())(*d.values()))
          elif type == "normal":
             return load(data)
    except Exception as e:
        print(e)

class Config:
    def __init__(self):
      self.config = get("./json/config/config.json", type="obj")

load_dotenv("./json/config/.env")