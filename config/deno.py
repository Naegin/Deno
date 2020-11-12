from .data import Config
from discord.ext import commands
from database import Database
from .convert import User
from os import listdir

class Deno(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loaded = False
        self.config = Config()
        self.convert = User()
        self.db = Database(deno=self)

    async def modules(self):
        plugins = [p[:-3] for p in listdir("plugins") if p.endswith(".py")]
        total_plugins = len(plugins)
        for i, plugin in enumerate(plugins, 1):
          try:
             self.load_extension(f"plugins.{plugin}")
          except Exception as e:
              print(f"[Plugin] : Erro ao carregar o plugin {plugin}.\n{e.__class__.__name__}: {e}")
          else:
            print(f"[Plugin] : O plugin {plugin} carregado com sucesso. ({i}/{total_plugins})")
        self.loaded = True


    async def on_ready(self):
       if not self.loaded:
          await self.modules()
          print(f"[Session] : O bot {self.user.name} está online.") 


    async def on_message(self, message):
       ctx = await self.get_context(message)
       
       if not ctx.guild: return
       
       if ctx.author.bot or not ctx.channel.permissions_for(message.guild.me).send_messages : return
       
       if not ctx.valid : return

       ctx.user = await self.db.get_user(ctx.author)
       
       await self.invoke(ctx)
