from dateutil.relativedelta import relativedelta
from datetime import datetime
import discord, arrow

__all__ = ("User")

class User:
    def __init__(self):
      self.test = '233'
    
    async def level(self, level):
       if level == 1 : return '5'
       
       elif level == 2 : return '10'
       
       elif level == 3 : return '20'
       
       else : return '0'
    
    async def check(self, data):
       if data is True : return "Ativado"
       
       else : return "Desativado"
    
    async def time(self, time):
       now = arrow.get(datetime.now())
       db = arrow.get(str(time))

       remain = (db - now).days
       if remain > 0:
          remain = f'{remain} dias'
       else:
         remain = 'Expirado'

       return f"{remain}"
    
    async def link(self, data, type):
       status = await self.check(data['monitor'][type.lower()]['status'])
       level = await self.level(data['premium']['level'])
       
       return f"{type.title()} : ``{len(data['monitor'][type.lower()]['link'])}/{level}`` ``[{status}]``"
