import discord, asyncio, os
from config import Deno

bot = Deno(command_prefix='d.', help_command=None, activity=discord.Game('Ajuda? d.help'))

loop = asyncio.get_event_loop()
t_bot = loop.create_task(bot.run(os.environ['B_TOKEN']))
#t_web = loop.create_task(web.app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)), loop=loop))
gathered = asyncio.gather(t_bot)
try:
  loop.run_until_complete(gathered)
except KeyboardInterrupt:
    loop.close()

