import random
import discord
from discord.ext import commands
from cryptlib import decrypt
import os

# A dice bot for use with Discord
bot = discord.Client()
bot = commands.Bot(command_prefix='!', description="""Um bot de RPG criado para o RPG Cronicas de um Reino Reverso!\n\n
													  =====Comandos=====\n\n
													  1) 'r' - Digite $r {Numero de Dados}d{Tipo de Dado} para efetuar uma rolagem Simples.
													  2) 'r' - Digite $r {Numero de Dados}d{Tipo de Dado}+{Valor a ser somado} para efetuar uma rolagem com acrescimo.
													  3) 'd' - Digite $r {Numero de Dados}d{Tipo de Dado} para efetuar uma rolagem Simples com Reações.
													  4) 'd' - Digite $r {Numero de Dados}d{Tipo de Dado}+{Valor a ser somado} para efetuar uma rolagem com acrescimo.""")                                                      

# Determines if a message is owned by the bot
def is_me(m):
	return m.author == bot.user

@bot.event
async def on_ready():
	print('Logado Como:')
	print(bot.user.name)
	print(bot.user.id)
	print('------')


#Sessão Rolagens Normais============================================================================================================
@bot.command(pass_context=True, description='')
async def r(ctx, r: str):

	try:
		result = []
		total = 0
		som = 0
		author_id = ctx.message.author.id
		myid = f'<@{author_id}>'		

	except Exception as e:
		print(f"LOG - Command(r): Erro na Definição de Variaveis({e})")

	try:
		if (r.find('d') != -1):
			num_of_dice, dice_type = r.split('d')
			if num_of_dice.strip() == "":
				num_of_dice = 1
			else:
				num_of_dice = int(num_of_dice)

			if (dice_type.find('+') != -1):
				dice_type, tresh = dice_type.split('+')
				dice_type = int(dice_type)
			else:
				dice_type = int(dice_type)
	except Exception as e:
		print(f"LOG - Command(r): Erro na definição do dado({e})")

	try:
		if (r.find('+') != -1):
			tresh, som = r.split('+')
			som = int(som)    

		for i in range(0, num_of_dice):
			n = random.randint(1, dice_type)
			result.append(n)
			total = total + n
	except Exception as e:
		print(f"LOG - Command(r): Erro na geração do numero aleatorio({e})")

	try:
		total = total + som    
	except Exception as e:
		print(f"LOG - Command(r): Erro na soma total do Dado({e})")
	
	try:
		if som == 0:
			await ctx.channel.send(f"{myid} :game_die:\n**Resultado: **{num_of_dice}d{dice_type} {result}\n**Total: **{total}\n")           
		else:
			await ctx.channel.send(f"{myid} :game_die:\n**Resultado: **{num_of_dice}d{dice_type} {result} + {som}\n**Total: **{total}\n")           
	except Exception as e:
		print(f"LOG - Command(r): Erro no envio da mensagem ao canal({e})")

	try:	
		await ctx.message.delete()    
	except Exception as e:
		print(f"LOG - Command(r): Erro ao Deletar mensagem anterior({e})")

	print(f"\n\nLOG: Rolagem(r)\nUser: {ctx.message.author}\nDado: {num_of_dice}d{dice_type}\nResultado: {result}\nTotal: {total}")

#Fim Sessão Rolagens Normais============================================================================================================

#Sessão Rolagens Reações============================================================================================================
@bot.command(pass_context=True, description='')
async def p(ctx, r: str):

	try:
		result = []
		total = 0
		som = 0
		message = ""  
		name = ""
		ext = ""
		author_id = ctx.message.author.id
		myid = f'<@{author_id}>'
	except Exception as e:
		print(f"LOG - Command(p): Erro na Definição de Variaveis({e})")

	try:
		if (r.find('d') != -1):
			num_of_dice, dice_type = r.split('d')
			if num_of_dice.strip() == "":
				num_of_dice = 1
			else:
				num_of_dice = int(num_of_dice)

			if (dice_type.find('+') != -1):
				dice_type, tresh = dice_type.split('+')
				dice_type = int(dice_type)
			else:
				dice_type = int(dice_type)
	except Exception as e:
		print(f"LOG - Command(p): Erro na definição do dado({e})")


	try:
		if (r.find('+') != -1):
			tresh, som = r.split('+')
			som = int(som)    

		for i in range(0, num_of_dice):
			n = random.randint(1, dice_type)        
			result.append(n)
			total = total + n
	except Exception as e:
		print(f"LOG - Command(p): Erro na geração do numero aleatorio({e})")

	
	try:
		for photo in os.listdir('./images/'):
			name, ext = photo.split('.')
			if int(name) == int(n):
				break

		if n <= 20:
			img = f'./images/{n}.{ext}'
		else:
			img = f'./images/100.jpg'

		if n == 1:            
			message = "Ai é Fooooooda!"                   
		elif n == 10:
			message = "Na meiuca!"            
		elif n == 20:
			message = "É que hoje vai ter festinha, aqui dentro do meu barraco! :notes:"
	except Exception as e:
		print(f"LOG - Command(p): Erro na definição de imagem({e})")

	try:
		total = total + som  
	except Exception as e:
		print(f"LOG - Command(p): Erro na soma total do Dado({e})")
	
	try:
		if som == 0:
			await ctx.channel.send(f"{myid} :game_die:\n**Resultado: **{num_of_dice}d{dice_type} {result}\n**Total: **{total}\n**Pingu: **{message}\n", file=discord.File(img))                   
		else:
			await ctx.channel.send(f"{myid} :game_die:\n**Resultado: **{num_of_dice}d{dice_type} {result} + {som}\n**Total: **{total}\n**Pingu: **{message}\n", file=discord.File(img))
	except Exception as e:
		print(f"LOG - Command(p): Erro no envio da mensagem ao canal({e})")

	try:
		await ctx.message.delete()
	except Exception as e:
		print(f"LOG - Command(p): Erro ao Deletar mensagem anterior({e})")
	
	print(f"\n\nLOG: Rolagem(p)\nUser: {ctx.message.author}\nDado: {num_of_dice}d{dice_type}\nResultado: {result}\nTotal: {total}")
#Fim Sessão Rolagens Reações============================================================================================================    

#Sessão Rolagens Privadas============================================================================================================
@bot.command(pass_context=True, description='')
async def s(ctx, r: str):

	try:
		result = []
		total = 0
		som = 0	

		author_id = ctx.message.author.id
		myid = f'<@{author_id}>'
	except Exception as e:
		print(f"LOG - Command(s): Erro na Definição de Variaveis({e})")

	try:
		if (r.find('d') != -1):
			num_of_dice, dice_type = r.split('d')
			if num_of_dice.strip() == "":
				num_of_dice = 1
			else:
				num_of_dice = int(num_of_dice)

			if (dice_type.find('+') != -1):
				dice_type, tresh = dice_type.split('+')
				dice_type = int(dice_type)
			else:
				dice_type = int(dice_type)
	except Exception as e:
		print(f"LOG - Command(s): Eclientrro na definição do dado({e})")


	try:
		if (r.find('+') != -1):
			tresh, som = r.split('+')
			som = int(som)    

		for i in range(0, num_of_dice):
			n = random.randint(1, dice_type)
			result.append(n)
			total = total + n
	except Exception as e:
		print(f"LOG - Command(s): Erro na geração do numero aleatorio({e})")

	try:
		total = total + som	    
	except Exception as e:
		print(f"LOG - Command(s): Erro na soma total do Dado({e})")

	try:
		if som == 0:		
			await ctx.author.send(f"{myid} :game_die:\n**Resultado: **{num_of_dice}d{dice_type} {result}\n**Total: **{total}\n")           
		else:		
			await ctx.author.send(f"{myid} :game_die:\n**Resultado: **{num_of_dice}d{dice_type} {result} + {som}\n**Total: **{total}\n")
	except Exception as e:
		print(f"LOG - Command(s): Erro no envio da mensagem ao canal({e})")	
	
	try:
		await ctx.message.delete()    
	except Exception as e:
		print(f"LOG - Command(s): Erro ao Deletar mensagem anterior({e})")
	
	print(f"\n\nLOG: Rolagem(s)\nUser: {ctx.message.author}\nDado: {num_of_dice}d{dice_type}\nResultado: {result}\nTotal: {total}")

#Fim Sessão Rolagens Privadas============================================================================================================ 

try:
	#bot.run(decrypt(b'gAAAAABhgauX3kDylPw79EHVyxQR4ZetxGCA3-aow5SmeMlKufam8xvvoxspciJeVTmHIQebip0nwd2fQNpstcqDBEm5VgbDHx093A6gKpBEiM_fbR0mgIHUUGr_WkHCKDqZyD6K4o0vUIa8PsPCcMPpblgp7P9t5A==').decode("utf-8"))
	bot.run('OTA0ODUzMjQ0NTEyMTk0Njcw.GYEe7P.XrOq7Y-BrEOTwsOk_3wk-PAMNsls1CYJ2ttCvU')
except Exception as e:
	print(f"LOG - Command(run): Erro ao iniciar o sistema({e})")
