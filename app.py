#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Matebot
#  
#  Copyleft 2012-2020 Iuri Guilherme <https://github.com/iuriguilherme>,
#     Matehackers <https://github.com/matehackers>,
#     Fábrica do Futuro <https://github.com/fabricadofuturo-poa>,
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
## Do jeito mais difícil para o mais fácil:
##  1) ./start.py
##  2) python3 start.py
##  3) pipenv run start.py aiogram matebot
##  4) pipenv run matebot
##  5) Ler o README.md ;)

### Logging
import logging
logging.basicConfig(level=logging.INFO)
# ~ logging.basicConfig(level=logging.DEBUG)

import subprocess, sys

from matebot.discord_matebot import app as discord_bot

if __name__ == "__main__":
  mode = 'discord'
  bot = 'nasabot'
  ## TODO fazer validação de verdade
  if len(sys.argv) > 1:
    mode = sys.argv[1]
    print(u"Modo de operação: %s" % (mode))
    if len(sys.argv) > 2:
      bot = sys.argv[2]
      print(
        u"Usando token do bot \"{}\" do arquivo de configuração.\
          ".format(bot)
      )
    else:
      print(u"Nome do bot não informado, {} presumido".format(bot))
  else:
    print(u"Modo de operação não informado, {} presumido.".format(mode))
    print(u"Nome do bot não informado, {} presumido".format(bot))
  if mode == 'discord':
    discord_bot(bot)
  else:
    print(u"Não entendi nada, não consegui iniciar. Leia o manual por favor.")
