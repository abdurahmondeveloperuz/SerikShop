from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
amazon = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇮🇳 India(IN)",callback_data="country:india:amazon"),
        InlineKeyboardButton("🇺🇸 United States(US)",callback_data="country:usa:amazon"),

    ],
    [
        InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="country:russia:amazon"),
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")
    
    ]
])

discord = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇫🇷 France(FR)",callback_data="country:france:discord"),
        InlineKeyboardButton("🇮🇳 India(IN)",callback_data="country:india:discord"),

    ],
    [

        InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="country:russia:discord"),
        InlineKeyboardButton("🇧🇷 Brazil(BR)",callback_data="country:brazil:discord")

    ],
    [
        InlineKeyboardButton("🇺🇸 United States(US)",callback_data="country:usa:discord"),
        InlineKeyboardButton("🇲🇾 Malaysia(MY)",callback_data="country:malaysia:discord")

    ],
    [
    ],
    [
        InlineKeyboardButton("🇰🇬 Kyrgyzstan(KG)",callback_data="country:kyrgyzstan:discord"),
        InlineKeyboardButton("🇮🇩 Indonesia(ID)",callback_data="country:indonesia:discord")

    ],
    [
        InlineKeyboardButton("🇰🇭 Combodia(KH)",callback_data="country:combodia:discord"),
        InlineKeyboardButton("🇰🇷 Korea(KR)",callback_data="country:korea:discord")

    ],
    [
        InlineKeyboardButton("🇻🇳 Vietnam(VN)",callback_data="country:vietnam:discord"),
        InlineKeyboardButton("🇭🇰 Hong Kong(HK)",callback_data="country:hongkong:discord"),

        

    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")
        
    ]
])