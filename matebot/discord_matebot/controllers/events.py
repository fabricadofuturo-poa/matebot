# -*- coding: utf-8 -*-
#
#  Matebot
#  
#  Copyleft 2012-2020 Iuri Guilherme <https://github.com/iuriguilherme>,
#     Matehackers <https://github.com/matehackers>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

import logging

from discord.ext.commands import Bot
from matebot.plugins import nsa20

def add_events(bot: Bot):
  ## Nasa Space Apps 2020
  nsa20.add_commands(bot)
  @bot.command()
  async def design(ctx):
    await ctx.send(u"digite !design se você é designer ou web designer;")

  @bot.event
  async def on_ready():
    logging.info(u"""Conectada com sucesso, o nosso nome de usuário é {0.user}\
""".format(bot))
