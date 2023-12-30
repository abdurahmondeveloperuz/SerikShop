from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
vkontakte = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton("🇰🇿 Kazakhstan(KZ)",callback_data="country:kazakhstan:vkonatkte"),
		InlineKeyboardButton("🇮🇳 India(IN)",callback_data="country:india:vkonatkte"),
	],
	[
		InlineKeyboardButton("🇳🇱 Netherlands(NL)",callback_data="country:netherlands:vkonatkte"),
		InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="country:russia:vkonatkte"),
	],
	[
		InlineKeyboardButton("🇪🇪 Estonia(EE)",callback_data="country:estonia:vkonatkte"),
		InlineKeyboardButton("🇰🇬 Kyrgyzstan(KG)",callback_data="country:kyrgyzstan:vkonatkte"),
	],
	[
		InlineKeyboardButton("🇧🇷 Brazil(BR)",callback_data="country:brazil:vkonatkte"),
	],
	[
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
	],
])

tiktok = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton("🇮🇩 Indonesia(ID)",callback_data="country:indonesia:tiktok"),
		InlineKeyboardButton("🇻🇳 Vietnam(VN)",callback_data="country:vietnam:tiktok")
	],
	[
		InlineKeyboardButton("🇮🇳 India(IN)",callback_data="country:india:tiktok"),

	],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]
])