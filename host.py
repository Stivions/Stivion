import discord
from discord.ext import commands
import os

# Configuración del bot
TOKEN = 'YMTMxODQwNTA0MjA4NDExODUyOA.GUJlPn.oHyY43UFAZLnXIuASfrM6e5pr4-jAlcf5NPHX0'
bot = commands.Bot(command_prefix='!')

# Comando de prueba
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Comando para iniciar el bot
if __name__ == "__main__":
    if not os.path.exists('./.gitignore'):
        with open('.gitignore', 'w') as f:
            f.write('*.pyc\n__pycache__/\n')

    # Ejecutar el bot
    bot.run(TOKEN)