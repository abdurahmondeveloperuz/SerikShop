from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
twitter = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton(text="🇷🇺 Russian Federation(RU)",callback_data="country:russia:twitter"),
		InlineKeyboardButton(text="🇧🇷 Brazil(BR)",callback_data="country:brazil:twitter"),
	],
	[
		InlineKeyboardButton(text="🇲🇾 Malaysia(MY)",callback_data="country:malaysia:twitter"),
		InlineKeyboardButton(text="🇭🇺 Hungary(HU)",callback_data="country:hungary:twitter"),
	],
	[
		InlineKeyboardButton(text="🇰🇬 Kyrgyzstan(KG)",callback_data="country:kyrgyzstan:twitter"),
		InlineKeyboardButton(text="🇺🇸 United States(US)",callback_data="country:usa:twitter"),
	],	
	[
		InlineKeyboardButton(text="🇪🇪 Estonia(EE)",callback_data="country:estonia:twitter"),
		InlineKeyboardButton(text="🇮🇳 India(IN)",callback_data="country:india:twitter"),
	],
	[
		InlineKeyboardButton(text="🇻🇳 Vietnam(VN)",callback_data="country:vietnam:twitter"),
		InlineKeyboardButton(text="🇳🇱 Netetherlands(NL)",callback_data="country:netherlands:twitter"),
	],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]
])
whatsapp = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton(text="🇲🇽 Mexico(MX)",callback_data="country:mexico:whatsapp"),
		InlineKeyboardButton(text="🇷🇺 Russian Federation(RU)",callback_data="country:russia:whatsapp"),

	],
	[
		InlineKeyboardButton(text="🇵🇱 Poland(PL)",callback_data="country:poland:whatsapp"),
		InlineKeyboardButton(text="🇳🇪 Niger(NE)",callback_data="country:niger:whatsapp"),
	],
	[
		InlineKeyboardButton(text="🇰🇬 Kyrgyzstan(KG)",callback_data="country:kyrgyzstan:whatsapp"),
		InlineKeyboardButton(text="🇪🇸 Spain(ES)",callback_data="country:spain:whatsapp"),
	],
	[
		InlineKeyboardButton(text="🇲🇦 Morocco(MA)",callback_data="country:morocco:whatsapp"),
		InlineKeyboardButton(text="🇧🇷 Brazil(BR)",callback_data="country:brazil:whatsapp"),
	],
	[
		InlineKeyboardButton(text="🇧🇩 Bangladesh(BD)",callback_data="country:bangladesh:whatsapp"),
		InlineKeyboardButton(text="🇹🇷 Turkey(TR)",callback_data="country:india:whatsapp"),
	],
	[
		InlineKeyboardButton(text="🇫🇷 France(FR)",callback_data="country:france:whatsapp"),
		InlineKeyboardButton(text="🇺🇸 United States(US)",callback_data="country:usa:whatsapp"),	
	],
	[
		InlineKeyboardButton(text="🇰🇿 Kazakhstan(KZ)",callback_data="country:kazakhstan:whatsapp"),
		InlineKeyboardButton(text="🇵🇰 Pakistan(PK)",callback_data="country:pakistan:whatsapp"),	
	],
	[
		InlineKeyboardButton(text="🇩🇪 Germany(DE)",callback_data="country:germany:whatsapp"),
		InlineKeyboardButton(text="🇶🇦 Qatar(QA)",callback_data="country:qatar:whatsapp"),	
	],
	[
		InlineKeyboardButton(text="🇸🇪 Sweden(SE)",callback_data="country:sweden:whatsapp"),
		InlineKeyboardButton(text="🇨🇦 Canada(CA)",callback_data="country:canada:whatsapp"),	
	],
	[
		InlineKeyboardButton(text="🇧🇭 Bahrain(BH)",callback_data="country:bahrain:whatsapp"),
		InlineKeyboardButton(text="🇹🇭 Thailand(TH)",callback_data="country:thailand:thailand"),	

	],
	[
		InlineKeyboardButton(text="🇰🇼 Kuwait(KW)",callback_data="country:kuwait:whatsapp"),
		InlineKeyboardButton(text="🇷🇴 Romania(RO)",callback_data="country:romania:whatsapp"),	
	],
	[
		InlineKeyboardButton(text="🇮🇹 Italy(IT)",callback_data="country:italy:whatsapp"),
		InlineKeyboardButton(text="🇵🇭 Philippens(PH)",callback_data="country:philippens:whatsapp"),	
	],
	[
		InlineKeyboardButton(text="🇰🇭 Combodia(KH)",callback_data="country:combodia:whatsapp"),
		InlineKeyboardButton(text="🇦🇺 Australia(AU)",callback_data="country:australia:whatsapp"),	
	],
	[
		InlineKeyboardButton(text="🇩🇰 Denmark(DK)",callback_data="country:denmark:whatsapp"),
		InlineKeyboardButton(text="🇱🇹 Lithuania(LT)",callback_data="country:lithuania:whatsapp"),	
	],
	[
		InlineKeyboardButton(text="🇸🇬 Singapure(SG)",callback_data="country:singapure:whatsapp"),
		InlineKeyboardButton(text="🇳🇿 New Zealand(NZ)",callback_data="country:newzealand:whatsapp"),	
	],
	[
		InlineKeyboardButton(text="🇭🇰 Hong Kong(HK)",callback_data="country:hongkong:whatsapp"),
		InlineKeyboardButton(text="🇲🇾 Malaysia(MY)",callback_data="country:malaysia:whatsapp"),	
	],
	[
		InlineKeyboardButton(text="🇳🇱 Netherlands(NL)",callback_data="country:netherlands:whatsapp"),
		InlineKeyboardButton(text="🇧🇲 Bermuda(BM)",callback_data="country:bermuda:whatsapp"),	
	],
	[
		InlineKeyboardButton(text="🇻🇳 Vietnam(VN)",callback_data="country:vietnam:whatsapp"),
		InlineKeyboardButton(text="🇻🇪 Venezuela(VE)",callback_data="country:venezuela:whatsapp"),	
	],
	[
		InlineKeyboardButton(text="🇰🇪 Kenya(KE)",callback_data="country:kenya:whatsapp"),
		InlineKeyboardButton(text="🇮🇩 Indonesia(ID)",callback_data="country:indonesia:whatsapp"),	
	],
	[
		InlineKeyboardButton(text="🇮🇳 India(IN)",callback_data="country:india:whatsapp"),
		InlineKeyboardButton(text="🇸🇦 Saudi Arabia(SA)",callback_data="country:saudiarabia:whatsapp"),	
	],
	[
		InlineKeyboardButton(text="🇵🇹 Portugal(PT)",callback_data="country:portugal:whatsapp"),
		
	],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]
])