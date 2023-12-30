from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
ebay = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton(text="🇩🇪 Germany(DE)",callback_data="country:germany:ebay"),

        
	],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]
])


tinder = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇧🇷 Brazil(BR)",callback_data="country:brazil:tinder"),
        InlineKeyboardButton("🇫🇷 France(FR)",callback_data="country:france:tinder")
    ],
    [

        InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="country:russia:tinder"),
        InlineKeyboardButton("🇩🇪 Germany(DE)",callback_data="germany_tinder"),

    ],
    [
        InlineKeyboardButton("🇺🇸 United States(US)",callback_data="country:usa:tinder"),
        InlineKeyboardButton("🇲🇾 Malaysia(MY)",callback_data="country:malaysia:tinder")

    ],
    [
        InlineKeyboardButton("🇲🇩 Moldava(MD)",callback_data="country:moldova:tinder"),
        InlineKeyboardButton("🇮🇩 Indonesia(ID)",callback_data="country:indonesia:tinder")

    ],
    [
        InlineKeyboardButton("🇵🇹 Portugal(PT)",callback_data="country:portugal:tinder"),
        InlineKeyboardButton("🇧🇬 Bulgaria(BG)",callback_data="country:bulgaria:tinder")

    ],
    [
        InlineKeyboardButton("🇹🇭 Thailand(TH)",callback_data="country:honkong:tinder"),
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]
 
])