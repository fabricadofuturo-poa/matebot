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

### Config
try:
  from instance.config import Config
  config = Config()
except Exception as e:
  print(u"""Arquivo de configuração não encontrado ou mal formado. Leia o manua\
l.\n{}""".format(str(e)))
  raise

### discord.py
## https://discord.com/developers/docs/intro
## https://discordpy.readthedocs.io/en/latest/
import discord
from discord import errors

### Discord MateBot
from matebot.discord_matebot import (
  # ~ models,
  # ~ views,
  controllers,
)
from matebot.discord_matebot.controllers.clients import MateBot
from matebot.discord_matebot.controllers.events import add_events

def app(bot_name):
  try:
    bot = MateBot(command_prefix="!", config = config, name = bot_name)
    add_events(bot)
    bot.run(config.bots[bot_name]['token'] or '')
  except KeyError as exception:
    logging.warning(u"""Problema com o arquivo de configuração. Já lerdes o man\
ual? Fizerdes tudo certo? Se tiverdes certeza de que está tudo certo e não func\
iona, pede ajuda no Github, no Telegram, no Discord, enfim...\nChave que não fo\
i encontrada no arquivo de configuração: {}""".format(str(exception)))
  except errors.LoginFailure:
    logging.warning(u"""Token não existe ou está errada. Favor consultar o manu\
al do Discord.""")
  except Exception as exception:
    logging.warning(u"Deu Errado: {}".format(repr(exception)))

### Código do Pedrinho
### FIXME portar tudo pro plugin nsa20
# ~ get.user
# ~ if user.database = true: //ve se o usuario ja esta registrado no banco de dados 
# ~ print('Posso te ajudar?')
# ~ else:            //ou se ele é um novo usuário que precisa ser registrado
# ~ printf('você é da Equipe de Controle ou Participante?') 
# ~ if answer=Equipe de Controle or Controle: 
# ~ print('digite o seu e-mail de registro:')
# ~ get.email
# ~ if (email=user.moderadores): //verifica se tem registro de admin                             //será uma lista de emails de quem é admin
# ~ print('tamo junto. vamos começar essa missão. preciso que tu me responda umas perguntas...'   
# ~ print('posso utilizar os seus dados para melhorar sua experiência na maratona de inovação NASA Space Apps Challenge 2020? Nós precisamos do seu nome, sobrenome, idade, email, cargo, estado do brasil e cidade escolhida. Você nós dá permisão? sim ou não?') //para estar de acordo com LGPD
# ~ if answer=sim:
# ~ print('qual sem nome?):
# ~ set.nome.user
# ~ print('qual seu sobrenome?):
# ~ set.sobrenome.user
# ~ print('qual sua idade?):
# ~ set.idade.user
# ~ print('qual seu email?):
# ~ set.email.user
# ~ print('qual seu cargo?
# ~ print('[emoji-brain] - mentor')
# ~ print('[emoji-anatomical_heart]')
# ~ print('[emoji-eye] - operação')
# ~ if  [emoji-brain]: //coloca a pessoa no cargo que ela disse ser
# ~ roleVer = '[emoji-brain]' //role to add
# ~ user = ctx.message.author //user
# ~ role = roleVer //change the name from roleVer to role
# ~ await ctx.send("""Tentando Verificar {}""".format(user))try:
# ~ await user.add_roles(discord.utils.get(user.guild.roles, name=role)) 
# ~ //add the role
# ~ except Exception as e:
# ~ await ctx.send('Rolou problema rodando esse comando..' + str(e)) 
# ~ //if error
# ~ else:
# ~ await ctx.send("""Verificado!: {}""".format(user)) 
# ~ //no errors, say verified

# ~ if  [emoji-anatomical_heart] //coloca a pessoa no cargo que ela disse ser
# ~ roleVer = '[emoji-brain]' //role to add
# ~ user = ctx.message.author //user
# ~ role = roleVer //change the name from roleVer to role
# ~ await ctx.send("""Tentando Verificar {}""".format(user))try:
# ~ await user.add_roles(discord.utils.get(user.guild.roles, name=role)) 
# ~ //add the role
# ~ except Exception as e:
# ~ await ctx.send('Rolou problema rodando esse comando..' + str(e)) 
# ~ //if error
# ~ else:
# ~ await ctx.send("""Verificado!: {}""".format(user)) 
# ~ //no errors, say verified

# ~ if  [emoji-eye] //coloca a pessoa no cargo que ela disse ser
# ~ roleVer = '[emoji-eye]' //role to add
# ~ user = ctx.message.author //user
# ~ role = roleVer //change the name from roleVer to role
# ~ await ctx.send("""Tentando Verificar {}""".format(user))try:
# ~ await user.add_roles(discord.utils.get(user.guild.roles, name=role)) 
# ~ //add the role
# ~ except Exception as e:
# ~ await ctx.send('Rolou problema rodando esse comando..' + str(e)) 
# ~ //if error
# ~ else:
# ~ await ctx.send("""Verificado!: {}""".format(user)) 
# ~ //no errors, say verified
# ~ printf(qual seu estado?)
# ~ set.estado.user
# ~ printf(qual sua cidade?)
# ~ set.cidade.user
# ~ print ('Essas são as principais dúvidas e informações gerais do hackathon: [inserir links gerais do hackathon]. Você tem mais alguma dúvida? sim ou não')
# ~ if answer=sim:
# ~ loop (FAQ) //entra no modo perguntas e respostas que podemos desenvolver
# ~ else:
# ~ loop  return loop (bot.on)
# ~ else answer=não:
# ~ return loop (bot.on)
# ~ else('ops... um impostor... volte para o começo!'):
# ~ client.channels.get(`alertas`).send(`aviso de tentativa de invasao feita pelo usuário`+get.user) //informa ao canal alerta que fulaninho tentou invadir
# ~ return loop (bot.on) //volta pro inicio do algoritmo
# ~ if answer=Participante:
# ~ print('posso utilizar os seus dados para melhorar sua experiência na maratona de inovação NASA Space Apps Challenge 2020? Nós precisamos do seu nome, sobrenome, idade, email, cargo, estado do brasil e cidade escolhida. Você nós dá permisão? sim ou não?') //para estar de acordo com LGPD
# ~ if answer=sim:
# ~ print('qual sem nome?):
# ~ set.nome.user
# ~ print('qual seu sobrenome?):
# ~ set.sobrenome.user
# ~ print('qual sua idade?):
# ~ set.idade.user
# ~ print('qual seu email?):
# ~ set.email.user
# ~ print('qual seu cargo?
# ~ print('[emoji-woman_technologist] - desenvolvedor')
# ~ print('[emoji-woman_artist] - designer')
# ~ print('[emoji-woman_cientist] - cientista')
# ~ print('[emoji-woman_in_tuxedo] - negócios')
# ~ if [emoji-woman_technologist]: //coloca a pessoa no cargo que ela disse ser
# ~ roleVer = '[emoji-woman_technologist]' //role to add
# ~ user = ctx.message.author //user
# ~ role = roleVer //change the name from roleVer to role
# ~ await ctx.send("""Tentando Verificar {}""".format(user))try:
# ~ await user.add_roles(discord.utils.get(user.guild.roles, name=role)) 
# ~ //add the role
# ~ except Exception as e:
# ~ await ctx.send('Rolou problema rodando esse comando..' + str(e)) 
# ~ //if error
# ~ else:
# ~ await ctx.send("""Verificado!: {}""".format(user)) 
# ~ //no errors, say verified

# ~ if [emoji-woman_artist]: //coloca a pessoa no cargo que ela disse ser
# ~ roleVer = '[emoji-woman_artist]' //role to add
# ~ user = ctx.message.author //user
# ~ role = roleVer //change the name from roleVer to role
# ~ await ctx.send("""Tentando Verificar {}""".format(user))try:
# ~ await user.add_roles(discord.utils.get(user.guild.roles, name=role)) 
# ~ //add the role
# ~ except Exception as e:
# ~ await ctx.send('Rolou problema rodando esse comando..' + str(e)) 
# ~ //if error
# ~ else:
# ~ await ctx.send("""Verificado!: {}""".format(user)) 
# ~ //no errors, say verified

# ~ if [emoji-woman_cientist]: //coloca a pessoa no cargo que ela disse ser
# ~ roleVer = '[emoji-woman_cientist]' //role to add
# ~ user = ctx.message.author //user
# ~ role = roleVer //change the name from roleVer to role
# ~ await ctx.send("""Tentando Verificar {}""".format(user))try:
# ~ await user.add_roles(discord.utils.get(user.guild.roles, name=role)) 
# ~ //add the role
# ~ except Exception as e:
# ~ await ctx.send('Rolou problema rodando esse comando..' + str(e)) 
# ~ //if error
# ~ else:
# ~ await ctx.send("""Verificado!: {}""".format(user)) 
# ~ //no errors, say verified

# ~ if [emoji-woman_in_tuxedo]: //coloca a pessoa no cargo que ela disse ser
# ~ roleVer = '[emoji-woman_in_tuxedo]' //role to add
# ~ user = ctx.message.author //user
# ~ role = roleVer //change the name from roleVer to role
# ~ await ctx.send("""Tentando Verificar {}""".format(user))try:
# ~ await user.add_roles(discord.utils.get(user.guild.roles, name=role)) 
# ~ //add the role
# ~ except Exception as e:
# ~ await ctx.send('Rolou problema rodando esse comando..' + str(e)) 
# ~ //if error
# ~ else:
# ~ await ctx.send("""Verificado!: {}""".format(user)) 
# ~ //no errors, say verified

# ~ printf(qual seu estado?)
# ~ set.estado.user
# ~ printf(qual sua cidade?)
# ~ set.cidade.user
# ~ print ('Essas são as principais dúvidas e informações gerais do hackathon: [inserir links gerais do hackathon]')
# ~ print ('Agora que você está registrado. Precisamos colocar você na sua equipe!')
# ~ print ('Você já tem uma equipe formada? sim ou não?')
# ~ if answer=sim:    //ja tem uma equipe
# ~ print('marque todos os seus amigxs abaixo: [para isso é só colocar @nomedousuario]')
# ~ def on_message(message): //ve quem ele colocou, procura o time em que eles
# ~ //estao e coloca o usuario nesse canal de texto 
# ~ //e no canal de voz
# ~ find.text_channel=user
# ~ if '!MOVE' in message.content.upper():
# ~ author = message.author
# ~ await client.move_member(author, text_channel)
# ~ else:                   //grupo ainda nao foi criado
# ~ print('Parece que ninguém criou esse grupo ainda')
# ~ get.user.estado  //pega estado para saber em qual regiao vai criar o time
# ~ bot.createChannel(server,name) //cria canal_texto no servidor da regiãoBR
# ~ print('marque todos os seus amigxs abaixo: [para isso é só colocar @nomedousuario. Se ele ainda não está registrado no discord, manda pra ele esse link: [inserir link de convite do Discord]')
# ~ client.channels.get(`channelID`).send(`Text`) //o robo manda essa mesma //mensagem que o usuário mandou para o canal que foi criado para o time, //marcando todos membros no novo canal_texto. Trocar channelID pelo ID do //novo canal da equipe e Text pelos nomes dos users que ele mandou e  //estão no mesmo grupo.
# ~ client.channels.get(`channelID`).send(`Essas são as principais dúvidas e informações gerais do hackathon: [inserir links gerais do hackathon]. Você tem mais alguma dúvida? sim ou não')
# ~ if answer sim:
# ~ loop (FAQ) //entra no modo FAQ que podemos desenvolver
# ~ else:
# ~ loop  return loop (bot.on)
# ~ else: // usuário não tem equipe nenhuma
# ~ // algoritmo deve colocar o usuario no canal procuro-time da regiãoBR escolhida
# ~ //no canal preciso de time o usuário deverá escolher um dos 22 desafios 
# ~ //(1 emoji pra cada desafio)
# ~ //e sempre que fechar 4 pessoas votando no mesmo emoji, cria um canal de texto
# ~ //e outro canal de voz com essas 4 pessoas, essa é a equipe
# ~ else:
# ~ return loop (bot.on)
# ~ else
# ~ return loop (bot.on)
# ~ else
# ~ return loop (bot.on)
# ~ } catch (err) {
           # ~ // There are various reasons why sending a message may fail.
           # ~ // The API might time out or choke and return a 5xx status,
           # ~ // or the bot may not have permission to send the
           # ~ // message (403 status).
           # ~ console.warn('Failed to respond to mention.');
           # ~ console.warn(err);
       # ~ }
   # ~ }
# ~ });

# ~ bot.on('error', err => {
   # ~ console.warn(err);
# ~ });

# ~ bot.connect();
