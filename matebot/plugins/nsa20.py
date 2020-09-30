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

import logging
from discord.ext.commands import Bot
from discord import utils

async def change_role(ctx):
  await ctx.message.author.edit(roles = [utils.get(ctx.message.guild.roles,
    name = str(ctx.command).capitalize())])

def add_commands(bot: Bot):
  ## Altera cargo de acordo com comando
  @bot.command()
  async def dev(ctx):
    ctx.command = 'desenvolvedor'
    await change_role(ctx)
  @bot.command()
  async def design(ctx):
    await change_role(ctx)
  @bot.command()
  async def negocios(ctx):
    await change_role(ctx)
  @bot.command()
  async def cientista(ctx):
    await change_role(ctx)
