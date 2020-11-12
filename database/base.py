from motor import motor_asyncio
from .model import User
from datetime import datetime
import os

class Database:
    def __init__(self, *, deno):
        self.deno = deno
        self.connection = motor_asyncio.AsyncIOMotorClient(os.environ['D_URL'])
        self.db = db = self.connection[os.environ['D_NAME']]
        self.user = db.users

    async def get_user(self, ctx):
        data = await self.user.find_one({"_id": ctx.id})
        if data != None:
           return User(data, self.user)
        else:
          return await self.reg_user(ctx)

    async def reg_user(self, ctx):
        data = {
                "_id": ctx.id,
                "premium":{
                           "status":False, 
                           "time":str(datetime.now()),
                           "level":0
                          },
                "monitor":{
                           "nike":{
                                   "status":False,
                                   "link":[]
                                   }
                           }
                }
        await self.user.insert_one(data)
        return User(data, self.user)  
