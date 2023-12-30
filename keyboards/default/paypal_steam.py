from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
paypal = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇸🇬 Singapore(SG)",callback_data="country:singapore:pypal")

    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")

    ]
])

steam = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton("🇦🇷 Argentinas(AR)",callback_data="country:argentina:steam"),

        
	],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")
    ]
])