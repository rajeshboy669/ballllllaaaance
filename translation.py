from pyrogram.types import *
from config import *



SIMPLE_START_MESSAGE_REPLY_MARKUP = InlineKeyboardMarkup([
    [[
        InlineKeyboardButton("Update Channel", url="https://t.me/ANLINKS_IN"),
        InlineKeyboardButton("Support 🤝", url="https://t.me/Anlinks_in_support"),
        ],[
        InlineKeyboardButton("Connect To Anlinks🛠️", url=f"https://Anlinks.in/member/tools/api")
    ]]
])


BALANCE_TEXT = '''Your Details

Username - {username}

Publisher Balance - {pbalance}

Referral Balance - {rbalance}

Total Balance - {tbalance}

'''

ACCOUNT_TEXT = '''Your Details

Username - {username}

Publisher Balance - {pbalance}

Referral Balance - {rbalance}

Total Balance - {tbalance}

'''

START_MESSAGE = '''Hi there {user}, I am a Bulk Link Converter for Anlinks.in. I Can Convert Links Directly From Your Anlinks.in Account

1. Go To 👉 https://Anlinks.in/member/tools/api
2. Then Copy API Key
3. Then Type /api than give a single space and then paste your API Key (see example to understand more...)

(See Example.👇)
Example:
/api 1234567890abcdef1234567890abcdef12345678


⭐️ If you need any help or Support Contact Us at @AnLinks_in_support
'''

SUPPORT_MESSAGE = '''
Any Problem Please Contact Me 👉 @Anlinks_in_support'''

CONNECT_TEXT = """
☝️ SEND YOUR API TOKEN TO ME.

Click On The Button Below
Copy Api Token From Website
Paste & Send Token To Me.
"""


CUSTOM_ALIAS_MESSAGE = """For Custom Alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex: https://t.me/example | Example"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""




CONNECT_REPLY_MARKUP = InlineKeyboardMarkup([
    [ 
        InlineKeyboardButton("GET API TOKEN 🎫", url=f"https://anlinks.in/member/tools/api")
    ],
])


SUPPORT_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("⏪ Back", callback_data="start_dkbotz"),
    ],
])



BACK_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('⬅️ Back', callback_data=f'help_dkbotz')
    ],

])

USER_ABOUT_MESSAGE = """
- Website: [{base_site}](https://{base_site})

- {base_site} API: {shortener_api}

- Username: @{username}

- Header Text: 
{header_text}

- Footer Text: 
{footer_text}

- Banner Image: {banner_image}
"""


SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, 
`/set_api [api]`
            
Ex: `/set_api cbd63775f798fe0e58c67a56e6ce8b70c495cda4`

Get API From [{base_site}](https://{base_site}/ref/DKBOTZ)

Current {base_site} API: `{shortener_api}`"""

HEADER_MESSAGE = """Reply to the Header Text You Want

This Text will be added to the top of every message caption or text

For adding line break use \n
To Remove Header Text: `/header remove`"""

FOOTER_MESSAGE = """Reply to the Footer Text You Want

This Text will be added to the bottom of every message caption or text

For adding line break use \n
To Remove Footer Text: `/footer remove`"""

USERNAME_TEXT = """Current Username: {username}

Usage: `/username your_username` (without @)

This username will be automatically replaced with other usernames in the post

To remove this username, `/username remove`"""

BANNER_IMAGE = """
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://www.nicepng.com/png/detail/436-4369539_movie-logo-film.png`"""


BANNED_USER_TXT = """
Usage: `/ban [User ID]`

Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
