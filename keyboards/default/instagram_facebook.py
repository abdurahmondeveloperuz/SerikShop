from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
instagram = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇰🇿 Kazakhstan(KZ)",callback_data="country:kazakhstan:instagram"),
        InlineKeyboardButton("🇨🇦 Canada(CA)",callback_data="country:canada:instagram"),

    ],
    [

        InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="country:russia:instagram"),
        InlineKeyboardButton("🇧🇷 Brazil(BR)",callback_data="country:brazil:instagram")

    ],
    [
        InlineKeyboardButton("🇺🇸 United States(US)",callback_data="country:usa:instagram"),
        InlineKeyboardButton("🇳🇱 Netetherlands(NL)",callback_data="country:netherlands:instagram")

    ],
    [
        InlineKeyboardButton("🇰🇬 Kyrgyzstan(KG)",callback_data="country:kyrgyzstan:instagram"),
        InlineKeyboardButton("🇮🇩 Indonesia(ID)",callback_data="country:indonesia:instagram")

    ],
    [
        InlineKeyboardButton("🇰🇭 Combodia(KH)",callback_data="country:combodia:instagram"),
        InlineKeyboardButton("🇷🇴 Romania(RO)",callback_data="country:romania:instagram")

    ],
    [
        InlineKeyboardButton("🇻🇳 Vietnam(VN)",callback_data="country:vietnam:instagram"),
        InlineKeyboardButton("🇸🇬 Singapure(SG)",callback_data="country:singapore:instagram")
    ],
    [
        InlineKeyboardButton("🇨🇭 Switzerland(CH)",callback_data="country:switzerland:instagram"),
        InlineKeyboardButton("🇩🇪 Germany(DE)",callback_data="country:germany:instagram"),



	],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]
])

facebook = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇸🇰 Slovakia(SK)",callback_data="country:slovakia:facebook"), 
        InlineKeyboardButton("🇮🇳 India(IN)",callback_data="country:india:facebook"), 

    ],
    [

        InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="country:russia:facebook"), 
        InlineKeyboardButton("🇧🇷 Brazil(BR)",callback_data="country:brazil:facebook") 

    ],
    [
        InlineKeyboardButton("🇺🇸 United States(US)",callback_data="country:unitedstates:facebook"), 
        InlineKeyboardButton("🇧🇬 Bulgaria(BG)",callback_data="country:bulgaria:facebook") 

    ],
    [
        InlineKeyboardButton("🇰🇬 Kyrgyzstan(KG)",callback_data="country:kyrgyzstan:facebook"), 
        InlineKeyboardButton("🇮🇩 Indonesia(ID)",callback_data="country:unitedkingdom:facebook") 

    ],
    [
        InlineKeyboardButton("🇲🇳 Mongolia(MN)",callback_data="country:mongolia:facebook"), 
        InlineKeyboardButton("🇵🇭 Philippens(PH)",callback_data="country:philippens:facebook") 

    ],
    [
        InlineKeyboardButton("🇻🇳 Vietnam(VN)",callback_data="country:vietnam:facebook"), 
        InlineKeyboardButton("🇬🇪 Georgia(GE)",callback_data="country:georgia:facebook") 
    ],
    [
        InlineKeyboardButton("🇺🇦 Ukraine(UA)",callback_data="country:ukraine:facebook"),
        InlineKeyboardButton("🇩🇪 Germany(DE)",callback_data="country:germany:facebook"),


	],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]
])