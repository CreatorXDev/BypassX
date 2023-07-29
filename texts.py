from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackQueryHandler

gdrivetext = """__- appdrive \n\
- driveapp \n\
- drivehub \n\
- gdflix \n\
- drivesharer \n\
- drivebit \n\
- drivelinks \n\
- driveace \n\
- drivepro \n\
- driveseed \n\
    __"""


otherstext = """__- exe, exey \n\
- sub2unlock, sub2unlock \n\
- rekonise \n\
- letsboost \n\
- phapps2app \n\
- mboost	\n\
- sub4unlock \n\
- ytsubme \n\
- bitly \n\
- social-unlock	\n\
- boost	\n\
- gooly \n\
- shrto \n\
- tinyurl
    __"""


ddltext = """__- yandex \n\
- mediafire \n\
- uptobox \n\
- osdn \n\
- github \n\
- hxfile \n\
- 1drv (onedrive) \n\
- pixeldrain \n\
- antfiles \n\
- streamtape \n\
- racaty \n\
- 1fichier \n\
- solidfiles \n\
- krakenfiles \n\
- upload \n\
- akmfiles \n\
- linkbox \n\
- shrdsk \n\
- letsupload \n\
- zippyshare \n\
- wetransfer \n\
- terabox, teraboxapp, 4funbox, mirrobox, nephobox, momerybox \n\
- filepress \n\
- anonfiles, hotfile, bayfiles, megaupload, letsupload, filechan, myfile, vshare, rapidshare, lolabits, openload, share-online, upvid \n\
- fembed, fembed, femax20, fcdn, feurl, layarkacaxxi, naniplay, nanime, naniplay, mm9842 \n\
- sbembed, watchsb, streamsb, sbplay.
    __"""


shortnertext = """__- igg-games \n\
- olamovies\n\
- katdrive \n\
- drivefire\n\
- kolop \n\
- hubdrive \n\
- filecrypt \n\
- shareus \n\
- shortingly \n\
- gyanilinks \n\
- shorte \n\
- psa \n\
- sharer \n\
- new1.gdtot \n\
- adfly\n\
- gplinks\n\
- droplink \n\
- linkvertise \n\
- rocklinks \n\
- ouo \n\
- try2link \n\
- htpmovies \n\
- sharespark \n\
- cinevood\n\
- atishmkv \n\
- urlsopen \n\
- xpshort, techymozo \n\
- dulink \n\
- ez4short \n\
- krownlinks \n\
- teluguflix \n\
- taemovies \n\
- toonworld4all \n\
- animeremux \n\
- adrinolinks \n\
- tnlink \n\
- flashlink \n\
- short2url \n\
- tinyfy \n\
- mdiskshortners \n\
- earnl \n\
- moneykamalo \n\
- easysky \n\
- indiurl \n\
- linkbnao \n\
- mdiskpro \n\
- tnshort \n\
- indianshortner \n\
- rslinks \n\
- bitly, tinyurl \n\
- thinfi \n\
- pdisk \n\
- vnshortener \n\
- onepagelink \n\
__"""


HELP_TEXT = f'**--Just Send me any Supported Links From Below Mentioned Sites--** \n\n\
**List of Sites for DDL : ** \n\n{ddltext} \n\
**List of Sites for Shorteners : ** \n\n{shortnertext} \n\
**List of Sites for GDrive Look-ALike : ** \n\n{gdrivetext} \n\
**Other Supported Sites : ** \n\n{otherstext}'


def start(update, context):
    keyboard = [
        [InlineKeyboardButton("DDL Sites", callback_data='ddl')],
        [InlineKeyboardButton("Shorteners", callback_data='shorteners')],
        [InlineKeyboardButton("GDrive Look-ALike", callback_data='gdrive')],
        [InlineKeyboardButton("Other Sites", callback_data='others')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(HELP_TEXT, reply_markup=reply_markup)


def menu_selection(update, context):
    query = update.callback_query
    query.answer()
    if query.data == 'ddl':
        query.edit_message_text(ddltext)
    elif query.data == 'shorteners':
        query.edit_message_text(shortnertext)
    elif query.data == 'gdrive':
        query.edit_message_text(gdrivetext)
    elif query.data == 'others':
        query.edit_message_text(otherstext)

def main():
    updater = Updater("6164457879:AAH7FxFX5F9hIAruioBtWN3GY610ZR2VuCk", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(menu_selection))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
