# vim:fileencoding=utf-8
#  Plugin nsa20 para matebot: NASA Space Apps Challenge
#  Copyleft (C) 2020 Iuri Guilherme, 2020 Fábrica do Futuro
#  
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

from discord.ext.commands import Bot

def add_commands(bot: Bot):
  @bot.command()
  async def desenvolvimento(ctx):
    await ctx.send(u"digite !desenvolvimento se você for desenvolvedor de sistemas;")

  @bot.command()
  async def design(ctx):
    await ctx.send(u"digite !design se você é designer ou web designer;")

  @bot.command()
  async def negocios(ctx):
    await ctx.send(u"digite  !negocios se você for da área comercial, empreendedor, gestor, etc;")

  @bot.command()
  async def mkt(ctx):
    await ctx.send(u"digite !mkt se você é da área de marketing ou publicidade;")

  @bot.command()
  async def cientista_de_dados(ctx):
    await ctx.send(u"digite !cientista_de_dados se for o seu caso;")

  @bot.command()
  async def outros(ctx):
    await ctx.send(u"digite !outros se sua área de atuação não se encaixa em nenhum dos perfis acima :wink: ")

  @bot.event
  async def on_member_join(member):
    logging.info(u"{} entrou no servidor".format(member))
