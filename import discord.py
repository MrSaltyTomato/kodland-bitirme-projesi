import discord
from discord.ext import commands

# Enable necessary intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Required for reading messages

# Create the bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

# Causes of climate change
def get_climate_causes():
    return (
        "**İklim Değişikliğinin Nedenleri:**\n"
            "1️⃣ Fosil yakıtların yakılması (kömür, petrol, gaz)\n"
            "2️⃣ Ormanların yok edilmesi\n"
            "3️⃣ Endüstriyel emisyonlar\n"
            "4️⃣ Tarım (hayvancılıktan kaynaklanan metan)\n"
            "5️⃣ Atık ve çöplükler (metan salınımı)\n"
            "6️⃣ Ulaşım emisyonları\n\n"
            "✅ **Yenilenebilir enerjiye geçmek ve karbon ayak izlerini azaltmak yardımcı olabilir!**"
            )

# Solutions to climate change
def get_climate_solutions():
    return (
        "**İklim Değişikliğine Çözümler:**\n"
        "✅ Yenilenebilir enerjiye geçin (güneş, rüzgar, hidro)\n"
        "✅ Fosil yakıt kullanımını azaltın ve temiz enerji politikalarını destekleyin\n"
        "✅ Ağaç dikin ve ormanları koruyun\n"
        "✅ Et tüketimini azaltın (hayvancılıktan daha az metan)\n"
        "✅ Atıkları azaltın, geri dönüştürün ve kompost yapın\n"
        "✅ Toplu taşımayı, bisikletleri veya elektrikli araçları kullanın\n\n"
        "🌱 Her eylem önemlidir! Daha yeşil bir gelecek için birlikte çalışalım! 💚"

    )



# Benefits of taking action
def get_climate_benefits():
    return (
        "**İklim Çözümlerinin Faydaları:**\n"
        "🌞 **Yenilenebilir enerjiye geçiş** → Daha az kirlilik, daha temiz hava ve enerji bağımsızlığı\n"
        "🌲 **Ormanları koruma** → Daha fazla oksijen, daha az CO₂ ve daha iyi yaban hayatı yaşam alanları\n"
        "🥦 **Daha az et yeme** → Daha az metan emisyonu, daha sağlıklı beslenme ve daha düşük su kullanımı\n"
        "♻️ **Geri dönüşüm ve kompostlama** → Daha az çöp sahası atığı, daha az kirlilik ve kaynakların korunması\n"
        "🚲 **Toplu taşıma veya bisiklet kullanma** → Daha az karbon emisyonu, daha sağlıklı topluluklar ve daha az trafik\n\n"
        "🌍 Küçük eylemler gezegenimiz üzerinde **büyük bir olumlu etkiye** yol açar!"
    
    )
# Full overview of climate change
def get_climate_overview():
    return (
        "**🌍 İklim Değişikliği: Genel Görünüm 🌍**\n\n"
        "İklim değişikliği, fosil yakıtların yakılması, ormansızlaşma ve endüstriyel emisyonlar gibi insan faaliyetlerinin neden olduğu küresel bir krizdir. "
        "Bu eylemler sera gazlarını serbest bırakır, ısıyı hapseder ve küresel sıcaklıkların artmasına neden olur. "
        "Bu, daha aşırı hava olaylarına, deniz seviyelerinin yükselmesine ve çevresel bozulmalara yol açar.\n\n"
        "**İyi haber?** Karşı koyabiliriz! Temiz enerji kullanarak, atıkları azaltarak, ormanları koruyarak ve "
        "sürdürülebilir seçimler yaparak iklim değişikliğini yavaşlatabilir ve gezegenimizi gelecek nesiller için koruyabiliriz.\n\n"
        "**🌱 Katılmak ister misiniz? Fark yaratan bu gerçek dünya örgütlerine göz atın:**\n"
        "🌍 [The Climate Reality Project](https://www.climaterealityproject.org/)\n"
        "🌿 [Greenpeace](https://www.greenpeace.org/)\n"
        "🌎 [World Yaban Hayatı Fonu (WWF)](https://www.worldwildlife.org/)\n"
        "🌞 [350.org](https://350.org/)\n\n"
        "Birlikte daha temiz, daha yeşil bir gelecek yaratabiliriz! 💚"
    )


# Event: Bot is ready
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Type !climate 🌍"))
    print(f'✅ Bot is online! Logged in as {bot.user}')

# Command: Respond with climate change causes
@bot.command()
async def climate(ctx):
    await ctx.send(get_climate_causes())

# Command: Respond with solutions to climate change
@bot.command()
async def solutions(ctx):
    await ctx.send(get_climate_solutions())

# Command: Respond with benefits of climate solutions
@bot.command()
async def benefits(ctx):
    await ctx.send(get_climate_benefits())

# Command: Give an overview of climate change + real-world organizations
@bot.command()
async def overview(ctx):
    await ctx.send(get_climate_overview())

# Run the bot (replace 'tokenherelol' with your actual bot token)
bot.run("tokenherelol")
