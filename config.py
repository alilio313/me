import os
API_ID = int(os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")

FULL_INFO = (
    "💢 - Full info about the username @{username}\n\n"
    "💠 - Owner address : {address}\n"
    "⁉ - Status : {status}\n"
    "💰 - Price : {ton} TON\n\n"
    "😜 **@{me}**[⁩](https://nft.fragment.com/username/{username}.webp)"
)

WELCOME_TEXT = (
    "- Welcome to **fragment.com** bot\n\n"
    "🤷‍♂️ How to use this bot?\n"
    "  -| In a private/group chat send : nft + @username\n"
    "  -| In inline mode : `@{} nerd`\n\n"
    "✨ Powered by: **@Y88F8**"
    )
