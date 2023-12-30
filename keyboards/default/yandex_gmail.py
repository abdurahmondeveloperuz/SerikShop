from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
yandex = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="country:russia:yandex"),
	
	],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")
    ]
])

gmail = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton("🇮🇳 India(IN)",callback_data="country:india:Google"),
		InlineKeyboardButton("🇧🇷 Brazil(BR)",callback_data="country:brazil:Google")
	],
	[
		InlineKeyboardButton("🇰🇪 Kenya(KE)",callback_data="country:kenya:Google"),
		InlineKeyboardButton("🇺🇦 Ukraine(UA)",callback_data="country:ukarine:Google")
	],
	[
		InlineKeyboardButton("🇫🇷 France(FR)",callback_data="country:france:Google"),
		InlineKeyboardButton("🇵🇪 Peru(PE)",callback_data="country:peru:Google")
	],
	[
		InlineKeyboardButton("🇲🇽 Mexico(MX)",callback_data="country:mexico:Google"),
		InlineKeyboardButton("🇹🇷 Turkey(TR)",callback_data="country:turkey:Google")
	],
	[
		InlineKeyboardButton("🇳🇮 Nicaragua(NI)",callback_data="country:nicagura:Google"),
		InlineKeyboardButton("🇰🇬 Kyrgyzstan(KG)",callback_data="country:kyrgyzstan:Google")
	],
	[
		InlineKeyboardButton("🇰🇭 Combodia(KH)",callback_data="country:colombia:Google"),
		InlineKeyboardButton("🇹🇭 Thailand(TH)",callback_data="country:thailand:Google")
	],
	[
		InlineKeyboardButton("🇺🇸 United States(US)",callback_data="country:usa:Google"),
		InlineKeyboardButton("🇲🇾 Malaysia(MY)",callback_data="country:malaysia:Google")
	],
	[
		InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="country:russia:Google"),
		     
	],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")
    ]
])




