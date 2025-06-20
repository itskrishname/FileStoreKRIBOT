from aiohttp import web
from plugins import web_server
import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
from config import API_HASH, API_ID, LOGGER, BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, CHANNEL_ID, PORT
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1009999999999



class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=API_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        if FORCE_SUB_CHANNEL:
            try:
                link = (await self.create_chat_invite_link(chat_id=FORCE_SUB_CHANNEL, creates_join_request=True)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    link = (await self.create_chat_invite_link(chat_id=FORCE_SUB_CHANNEL, creates_join_request=True)).invite_link
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot Can't Export Invite link From Force Sub Channel !")
                self.LOGGER(__name__).warning(f"Please Double Check The FORCE_SUB_CHANNEL Value And Make Sure Bot Is Admin In Channel With Invite Users Via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL}")
                self.LOGGER(__name__).info("\nBot Stopped. https://t.me/NEW_ANIMES_HINDI_DUB_INDIA For Support")
                sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Hey 🖐")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure Bot Is Admin In DB Channel, And Double Check The CHANNEL_ID Value, Current Value: {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/NEW_ANIMES_HINDI_DUB_INDIA For Support")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated By \nhttps://t.me/SECRECT_BOT_UPDATES")
        self.LOGGER(__name__).info(f"""ミ💖  Sᴇᴄʀᴇᴄᴛ 𝐁ᴏᴛ 𝐔ᴘᴅᴀᴛᴇs 💖彡""")
        self.username = usr_bot_me.username
        
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot Stopped...")
            





# Developer 
# Don't try 🥺
# Telegram Channel @NEW_ANIMES_HINDI_DUB_INDIA
# Backup Channel @NEW_ANIMES_HINDI_DUB_INDIA
# Developer @NEW_ANIMES_HINDI_DUB_INDIA
