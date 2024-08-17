import discord
from discord.ext import commands
import dcbotimg

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def selam(ctx):
    await ctx.send(f"Selam {ctx.author}. Ben {bot.user}")

@bot.command()
async def Ph(ctx):
    if ctx.message.attachments:
        for dosya in ctx.message.attachments:
            await dosya.save(f"KullaniciResimleri/{dosya.filename}")
            await ctx.send("Bilgilerin elimize ulaştı!")
        x,y = dcbotimg.dcaktar(f"KullaniciResimleri/{dosya.filename}")
        y=round(y*100,1)
        
        if x == "Sosis Kopek\n":
            await ctx.send(f"Bu bir Sosis Köpek. %{y}, oranıyla eminim.")
        elif x == "Alman Köpek\n":
            await ctx.send(f"Bu bir Alman Köpek. %{y}, oranıyla eminim.")
        elif x == "Doberman\n":
            await ctx.send(f"Bu bir Doberman. %{y}, oranıyla eminim.")
        elif x == "Bilinmeyen\n":
            await ctx.send(f"Bu resim hakkında bilgim olmadığına %{y} oranıyla eminim, Lütfen başka bir resim gönderin.")    
        else:
            await ctx.send(f"Bu {x} sınıfına ait, %{y} oranında eminim")  
    else:
        await ctx.send("Malesef bilgileriniz elimize ulaşmadı")
        
        
bot.run("")