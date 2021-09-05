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
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from utils import USERNAME, mp
from config import Config
U=USERNAME
CHAT=Config.CHAT
msg=Config.msg
HOME_TEXT = "<b>Salam, [{}](tg://user?id={})\n\nMahni Botuna-a xoş gəlmisiniz🖐🖐.</b>"
HELP = """

<b>Botu qrupa əlavə edib və yoneticilik verməyiniz şərtdir.

Səsli söhbəti başladın

/play <mahnı adı> 

/splay <mahni adi> </b>

**Ümumi Əmrlər**:
**/play** <mahni adi>
**/splay** <mahni adi>
**/player**  Hazırki ifa olunan mahnını gostərir
**/help** Komek
**/playlist** Pleylisti gostərir.

**Admin Commands**:
**/skip** Növbəti mahnıya keçid edir
**/join**  Səsli söhbətə qoşulur
**/leave**  Mövcud səsli söhbətdən cıxış edir
**/shuffle** Pleylisti qarışdırır
**/cplay** Bir kanalın musiqi fayllarından musiqi çalır
**/vc** Hansı VC-nin birləşdirildiyini yoxlayın.
**/stop**  Mahnını durdurur.
**/radio** Radionu başladır
**/stopradio** Radio Stream dayandırır
**/clearplaylist** Pleylisti silir
**/clean** İstifadə edilməmiş RAW PCM sənədlərini silir
**/pause** Mahnini duraklatır
**/resume** Mahnını davam elətdirir
**/mute**  Mahnini səssizə alır
**/unmute**  Mahnini səssizdən açır
**/restart** Botu yeniləyir və yenidən başladır
"""




@Client.on_message(filters.command(['start', f'start@{U}']))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('Developer', url='https://t.me/mehdizade_abdulla'),
        InlineKeyboardButton('Mafia AZ', url='https://t.me/MafiaAzeribaycan'),
    ],
    [
        InlineKeyboardButton('👨🏼‍🦯 Help', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    m=await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await mp.delete(m)
    await mp.delete(message)



@Client.on_message(filters.command(["help", f"help@{U}"]))
async def show_help(client, message):
    buttons = [
        [
        InlineKeyboardButton('Developer', url='https://t.me/medizade_abdulla'),
        InlineKeyboardButton('Mafia AZ', url='https://t.me/MafiaAzeribaycan'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    if msg.get('help') is not None:
        await msg['help'].delete()
    msg['help'] = await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
    await mp.delete(message)
