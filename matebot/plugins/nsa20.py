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

import emojis, logging

from discord.ext.commands import Bot
from discord import utils

## TODO: garantir que os cargos existem (testar a existência e criar se necessá\
## rio)
cargos = ['Desenvolvedor', 'Designer', 'Negócios', 'Cientista']

async def change_role_callback(ctx):
  await ctx.message.author.add_roles(utils.get(ctx.message.guild.roles,
    name = str(ctx.command).capitalize()))
  for cargo in cargos:
    if str(ctx.command).capitalize() != cargo:
      await ctx.message.author.remove_roles(utils.get(ctx.message.guild.roles,
        name = cargo))
  logging.info(u"{0} mudou o cargo para {1}".format(ctx.author,
    str(ctx.command).capitalize()))

def add_commands(bot: Bot):
  ## Altera cargo de acordo com comando
  @bot.command()
  async def dev(ctx):
    ctx.command = 'desenvolvedor'
    await change_role_callback(ctx)
  @bot.command()
  async def designer(ctx):
    await change_role_callback(ctx)
  @bot.command()
  async def negocios(ctx):
    ctx.command = 'negócios'
    await change_role_callback(ctx)
  @bot.command()
  async def cientista(ctx):
    await change_role_callback(ctx)

  @bot.event
  async def on_raw_reaction_add(payload):
   message_id = payload.message_id
   ## Mensagem de boas vindas
   if message_id in [760632139598528562, 760877039237988353]:
    guild_id = payload.guild_id
    guild = utils.find(lambda g : g.id == guild_id, bot.guilds)
    emoji = emojis.decode(str(payload.emoji))
    if emoji == ':computer:':
      role = utils.get(guild.roles, name = 'Desenvolvedor')
    elif emoji == ':briefcase:':
      role = utils.get(guild.roles, name = 'Negócios')
    elif emoji == ':microscope:':
      role = utils.get(guild.roles, name = 'Cientista')
    elif emoji == ':art:':
      role = utils.get(guild.roles, name = 'Designer')
    else:
      role = None
    if role is not None:
      member = payload.member
      if member is not None:
        await member.remove_roles(*[utils.get(guild.roles, name = cargo) \
          for cargo in cargos])
        await member.add_roles(role)
        logging.info(u"{0} mudou o cargo para {1}".format(member, role))
      else:
        logging.warning(u"Membro não encontrado.")
    else:
      logging.warning(u"Cargo não encontrado.")

  @bot.event
  async def on_raw_reaction_remove(payload):
    pass
