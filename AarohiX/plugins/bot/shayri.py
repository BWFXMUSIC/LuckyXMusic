
from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AarohiX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

SHAYRI = [ " **           ** \n\n**Bahut aacha lagta hai tujhe satana Aur fir pyar se tujhe manana.** ",
           " **            ** \n\n**Meri zindagi Meri jaan ho tum Mere sukoon ka Dusra naam ho tum.** ",
           " **      ,      ** \n\n****Tum Meri Wo Khushi Ho Jiske Bina, Meri Saari Khushi Adhuri Lagti Ha.** ",
           " **    ,        ** \n\n**Kash woh din jldi aaye Jb tu mere sath 7 feron me bndh jaye.** ",
           " **             ** \n\n**apna hath mere dil pr rakh do aur apna dil mere naam kar do.** ",
           " **               ** \n\n**Mahadev na koi gadi na koi bangla chahiye salamat rhe mera pyar bas yahi dua chahiye.** ",
           " **         ** \n\n**Fikr to hogi na tumhari ikloti mohabbat ho tum meri.** ",
           " **              ** \n\n**suno jaanu aap sirf kitchen sambhal lena ap ko sambhlne ke liye me hun naa.** ",
           " **         ** \n\n**So bat ki ek bat mujhe chahiye bas tera sath.** ",
           " **     ,    ,           ** \n\n**Bahut muskilon se paya hai tumhe Ab khona ni chahte ki tumhare they tumhare hai ab kisi or k hona nhi chahte.** ",
           " **          ** \n\n**Baby baten to roj karte haichalo aaj romance karte hai..** ",
           " **                ** \n\n**subha sham tujhe yad karte hai hum aur kya batayen ki tumse kitna pyar karte hai hum.** ",
           " **                 ** \n\n**Kisi se dil lag jane ko mohabbat nahi kehte jiske nina dil na lage use mohabbat kehte hai.** ",
           " **                 ** \n\n**mere dil ke lock ki chabi ho tum kya batayen jaan mere jeene ki eklauti wajah ho tum..** ",
           " **       ,       ,          ,       ** \n\n**Hum apki har cheez se pyar kar lenge apki har baat par etvar kar lenge bas ek bar keh do ki tum sirf mere ho hum zindagi bhar apka intzaar kar lenge..** ",
           " **              ** \n\n**Mohabbat kabhi special logo se nahi hoti jisse bhi hoti hai wahi special ban jate hai,.**",
           " **                ** \n\n**Tu meri jaan hai isme koi shak nahi tere alawa mujhe par kisi aur ka hak nhi..** ",
           " **      ,        ,         ,        ** \n\n**Pehli mohabbat meri hum jaan na sake pyar kya hota hai hum pehchan na sake humne unhe dil me basa liya is kadar ki jab chaha unhe dil se nikal na sake.** ",
           " **       ,        ,                  .** \n\n**khud nahi janti vo kitni pyari hai jan hai hamari par jan se jyda payari hai duriya ke hone se frak nahi pdta vo kal bhe hamari the or aaj bhe hamari hai.** ",
           " **        ,        ,        , -      ** \n\n**Chupke Se Aakar Iss Dil Mein Utar Jate Ho, Saanso Mein Meri Khushbu BanKe Bikhar Jate Ho,Kuchh Yun Chala Hai Tere Ishq Ka Jadoo, Sote-Jagte Tum Hi Tum Najar Aate Ho..** ",
           " **        ,            .** \n\n**Pyar karna sikha hai naftaro ka koi thor nahi bas tu hi tu hai is dil me dusra koi aur nahi hai.** ",
           " **     ,      ,     ,       **\n\n**Rab se apki khushiyan mangte hai duao me apki hansi mangte hai sochte hai apse kya mange chalo apse umar bhar ki mohabbat mangte hai..** ",
           " **                             .**\n\n**kash mere hoth tere hontho ko chu jayen dekhun jaha bas teri hi chehra nazar aaye ho jayen humara rishta kuch easa hothon ke sath humare dil bhi jud jaye.** ",
           " **       ,         ,       ,        .**\n\n**Aaj mujhe ye batane ki izazat de do, aaj mujhe ye sham sajane ki izazat de do, apne ishq me mujhe ked kr lo aaj jaan tum par lutane ki izazat de do..** ",
           " **        ,         .**\n\n**Jane log mohabbat ko kya kya naam dete hai hum to tere naam ko hi mohabbat kehte hai..** ",
           " **                              **\n\n**Dekh Ke Hame Wo Sir Jhukate Hai Bula Ke Mahfhil Me Najar Churate Hai Nafrat Hai Hamse To Bhi Koei Bat Nhi Par Gairo Se Mil Ke Dil Kyo Jalate Ho.** ",
           " **     ,        ,         ,          **\n\n**Tere bina tut kar bikhar jeynge tum mil gaye to gulshan ki tarha khil jayenge tum na mile to jite ji hi mar jayenge tumhe jo pa liya to mar kar bhi ji jayenge..** ",
           " **          ,       .**\n\n**Sanam teri kasam jese me zaruri hun teri khushi ke liye tu zaruri hai meri zindagi ke liye.** ",
           " **                     .**\n\n**Tumharfe gusse par mujhe pyar aaya hai is bedard duniya me koi to hai jisne mujhe pure hakk se dhamkaya hai.** ",
           " **                          .**\n\n**Palkon se Aankho ki hifajat hoti hai dhakad dil ki Aamanat hoti hai, ye rishta bhi bada pyara hota hai, kabhi chahat to kabhi shikayat hoti hai.** ",
           " **                            **\n\n**Muhabbt Ko Hab Log Khuda Mante Hai, Payar Karne Walo Ko Kyu Bura Mante Hai,Jab Jamana Hi Patthr Dil Hai,Fhir Patthr Se Log Kyu Duaa Magte Hai.** ",
           " **                       ,     **\n\n**Hua jab ishq ka ehsaas unhe akar wo pass humare sara din rate rahe, hum bhi nikale khudgarj itne yaro ki ood kar kafan ankhe band krke sote rhe.** ",
           " **                   -               **\n\n**Dil Ke Kone Se Ek Aawaj Aati Hai, Hame Har Pal Uaski Yad Aati Hai, Dil Puchhta Hai Bar Bar Hamse Ke, Jitna Ham Yad Karte Hai Uanhe, Kya Uanhe Bhi Hamari Yad Aati Hai,** ",
           " **       ,         ,          ,        **\n\n**Kabhi Lafz Bhool Jaaun Kabhi Baat Bhool Jaaun, Tujhe Iss Kadar Chahun Ki Apni Jaat Bhool Jaaun, Kabhi Uthh Ke Tere Paas Se Jo Main Chal Dun, Jaate Huye Khud Ko Tere Paas Bhool Jaaun..** ",
           " **                  ,       .**\n\n**Aaina dekhoge to meri yad ayegi sath guzari wo mulakat yad ayegi pal bhar ke waqt thahar jayega jab apko meri koi bat yad ayegi.** ",
           " **                                .**\n\n**Pyar kiya to unki mohabbat nazar aai dard hua to palke unki bhar aai do dilon ki dhadkan me ek baat nazar aai dil to unka dhadka par awaz dil ki aai.** ",
           " **                        ,        .**\n\n**Kai chehre lekar log yahn jiya karte hai hum to bas ek hi chehre se pyar karte hai na chupaya karo tum is chehre ko kyuki hum ise dekh ke hi jiya karte hai.** ",
           " ** bf   gf                **\n\n**Sabke bf ko apni gf se baat karke nind aajati hai aur mere wale ko mujhse lade bina nind nhi aati.** ",
           " **        .           .**\n\n**Sacha pyar kaha kisi ke nasib me hota hai esa pyar kahan is duniya me kisi ko nasib hota hai.** " ]

# Command
SHAYRI_COMMAND = ["gf", "bf", "shayri"]

@app.on_message(
    filters.command(SHAYRI_COMMAND)
    & filters.group
    )
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(SHAYRI),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/LuckyRaja0"),
                    InlineKeyboardButton(
                        "", url=f"https://t.me/Badnam_Mohabbat")
                    
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(SHAYRI_COMMAND)
    & filters.private
    )
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(SHAYRI),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/LuckyRaja0"),
                    InlineKeyboardButton(
                        "", url=f"https://t.me/Badnam_Mohabbat")
                    
                ]
            ]
        ),
    )
