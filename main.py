#MIT License

#Copyright (c) 2021 SUBIN

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
try:
    import asyncio
    from pyrogram import Client, idle, filters
    import os
    from config import Config
    from utils import mp, USERNAME, FFMPEG_PROCESSES
    from pyrogram.raw import functions, types
    import os
    import sys
    from time import sleep
    from threading import Thread
    from signal import SIGINT
    import subprocess
    
except ModuleNotFoundError:
    import os
    import sys
    import subprocess
    file=os.path.abspath("requirements.txt")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', file, '--upgrade'])
    os.execl(sys.executable, sys.executable, *sys.argv)


CHAT=Config.CHAT
bot = Client(
    "Musicplayer",
    Config.API_ID,
    Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")
async def main():
    async with bot:
        await mp.start_radio()
def stop_and_restart():
    bot.stop()
    os.system("git pull")
    sleep(10)
    os.execl(sys.executable, sys.executable, *sys.argv)


bot.run(main())
bot.start()

@bot.on_message(filters.command(["restart", f"restart@{USERNAME}"]) & filters.user(Config.ADMINS) & (filters.chat(CHAT) | filters.private))
async def restart(client, message):
    await message.reply_text("🔄 Bot Yenilənir və Yenidən Başladılır ...")
    await asyncio.sleep(3)
    try:
        await message.delete()
    except:
        pass
    process = FFMPEG_PROCESSES.get(CHAT)
    if process:
        try:
            process.send_signal(SIGINT)
        except subprocess.TimeoutExpired:
            process.kill()
        except Exception as e:
            print(e)
            pass
        FFMPEG_PROCESSES[CHAT] = ""
    Thread(
        target=stop_and_restart
        ).start()    


bot.send(
    functions.bots.SetBotCommands(
        commands=[
           types.BotCommand(
                command="start",
                description="Botu Başladır"
            ),
            types.BotCommand(
                command="help",
                description="Komək"
            ),
            types.BotCommand(
                command="play",
                description="Mahnı adı"
            ),
            types.BotCommand(
                command="splay",
                description="Mahnı adı"
            ),
            types.BotCommand(
                command="player",
                description="Cari oynayan mahnını idarəetmə ilə göstərir"
            ),
            types.BotCommand(
                command="playlist",
                description="Hazırda tələb olunan mahnı siyahısı"
            ),
            types.BotCommand(
                command="cplay",
                description="Kanaldan musiqi fayllarını oxuyur"
            ),
            types.BotCommand(
                command="skip",
                description="Növbəti mahnıya keçid edir"
            ),
            types.BotCommand(
                command="clearplaylist",
                description="Mövcud pleylisti təmizləyir"
            ),
            types.BotCommand(
                command="shuffle",
                description="Pleylisti qarışdırır"
            ),
            types.BotCommand(
                command="join",
                description="MusicBotu səsli sohbətə qatır"
            ),
            types.BotCommand(
                command="leave",
                description="MusicBotu səsli sohbətdən cıxarır"
            ),
            types.BotCommand(
                command="vc",
                description="Ckeck if VC is joined"
            ),
            types.BotCommand(
                command="stop",
                description="Mahnını dayandırır"
            ),
            types.BotCommand(
                command="radio",
                description="Radionu başladır"
            ),
            types.BotCommand(
                command="stopradio",
                description="Radionu dayandırır"
            ),
            types.BotCommand(
                command="clean",
                description="RAW fayllarını təmizləyir"
            ),
            types.BotCommand(
                command="pause",
                description="Mahnını duraklatır"
            ),
            types.BotCommand(
                command="resume",
                description="Mahnını davam etdirir"
            ),
            types.BotCommand(
                command="mute",
                description="Mahnını səssizə alır"
            ),
            types.BotCommand(
                command="volume",
                description="Səs səviyyəsini çoxaldır/azaldır 0-200"
            ),
            types.BotCommand(
                command="unmute",
                description="Mahnını səssizdən açır"
            ),
            types.BotCommand(
                command="restart",
                description="Botu yeniləyir və yenidən başladır"
            )
        ]
    )
)

idle()
bot.stop()
