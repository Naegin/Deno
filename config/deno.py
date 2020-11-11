from .data import Config
from discord.ext import commands
from .database import Database

class Deno(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loaded = False
        self.config = Config()
        self.db = Database(letty=self)


    async def on_ready(self):
       #if not self.loaded:
          print(f"[Session] : O bot {self.user.name} está online.") 