from discord.ext import commands
import discord

class User(commands.Cog):
    def __init__(self, deno):
        self.deno = deno

    @commands.command(name='test')
    async def _test(self, ctx, *, member: discord.Member=None):
        if member is None:
           member = ctx.author

        db = await self.deno.db.get_user(member)
        data = db.data

        embed = discord.Embed(colour=0xFFC0CB)
        embed.set_author(name="Minha conta", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Usuário", value=f"Nome : ``{member}``\nId : ``{member.id}``", inline=False)
        embed.add_field(name="Premium", value=f"Status : ``{await self.deno.convert.check(data['premium']['status'])}``\nLevel : ``{data['premium']['level']}``\nExpira em : ``{await self.deno.convert.time(data['premium']['time'])}``", inline=False)
        embed.add_field(name="Monitor", value=f"{await self.deno.convert.link(data, 'nike')}", inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"{ctx.me.name} © 2020" , icon_url=ctx.me.avatar_url)
        await ctx.send(embed=embed)

def setup(deno):
    deno.add_cog(User(deno))        
