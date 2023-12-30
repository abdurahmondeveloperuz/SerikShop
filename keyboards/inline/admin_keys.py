from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

amazon = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇮🇳 India(IN)",callback_data="admin:india:amazon"),
        InlineKeyboardButton("🇺🇸 United States(US)",callback_data="admin:usa:amazon"),

    ],
    [
        InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="admin:russia:amazon"),
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")
    
    ]
])

discord = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇫🇷 France(FR)",callback_data="admin:france:discord"),
        InlineKeyboardButton("🇮🇳 India(IN)",callback_data="admin:india:discord"),

    ],
    [

        InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="admin:russia:discord"),
        InlineKeyboardButton("🇧🇷 Brazil(BR)",callback_data="admin:brazil:discord")

    ],
    [
        InlineKeyboardButton("🇺🇸 United States(US)",callback_data="admin:usa:discord"),
        InlineKeyboardButton("🇲🇾 Malaysia(MY)",callback_data="admin:malaysia:discord")

    ],
    [
    ],
    [
        InlineKeyboardButton("🇰🇬 Kyrgyzstan(KG)",callback_data="admin:kyrgyzstan:discord"),
        InlineKeyboardButton("🇮🇩 Indonesia(ID)",callback_data="admin:indonesia:discord")

    ],
    [
        InlineKeyboardButton("🇰🇭 Combodia(KH)",callback_data="admin:combodia:discord"),
        InlineKeyboardButton("🇰🇷 Korea(KR)",callback_data="admin:korea:discord")

    ],
    [
        InlineKeyboardButton("🇻🇳 Vietnam(VN)",callback_data="admin:vietnam:discord"),
        InlineKeyboardButton("🇭🇰 Hong Kong(HK)",callback_data="admin:hongkong:discord"),

        

    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")
        
    ]
])
avito = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇷🇺 Russia Federation(RU)",callback_data="admin:russia:avito"),

        

    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")
    ]
])
sbermarket = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇷🇺 Russia Federation(RU)",callback_data="admin:russia:sbermarket"),

        
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]
])
samokat = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇷🇺 Russia Federation(RU)",callback_data="admin:russia:sbermarket"),
        
        
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")
    ]
])
ebay = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🇩🇪 Germany(DE)",callback_data="admin:germany:ebay"),

        
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]
])


tinder = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇧🇷 Brazil(BR)",callback_data="admin:brazil:tinder"),
        InlineKeyboardButton("🇫🇷 France(FR)",callback_data="admin:france:tinder")
    ],
    [

        InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="admin:russia:tinder"),
        InlineKeyboardButton("🇩🇪 Germany(DE)",callback_data="germany_tinder"),

    ],
    [
        InlineKeyboardButton("🇺🇸 United States(US)",callback_data="admin:usa:tinder"),
        InlineKeyboardButton("🇲🇾 Malaysia(MY)",callback_data="admin:malaysia:tinder")

    ],
    [
        InlineKeyboardButton("🇲🇩 Moldava(MD)",callback_data="admin:moldova:tinder"),
        InlineKeyboardButton("🇮🇩 Indonesia(ID)",callback_data="admin:indonesia:tinder")

    ],
    [
        InlineKeyboardButton("🇵🇹 Portugal(PT)",callback_data="admin:portugal:tinder"),
        InlineKeyboardButton("🇧🇬 Bulgaria(BG)",callback_data="admin:bulgaria:tinder")

    ],
    [
        InlineKeyboardButton("🇹🇭 Thailand(TH)",callback_data="admin:honkong:tinder"),
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]
 
])

instagram = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇰🇿 Kazakhstan(KZ)",callback_data="admin:kazakhstan:instagram"),
        InlineKeyboardButton("🇨🇦 Canada(CA)",callback_data="admin:canada_instagram:instagram"),

    ],
    [

        InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="admin:russia:instagram"),
        InlineKeyboardButton("🇧🇷 Brazil(BR)",callback_data="admin:brazil:instagram")

    ],
    [
        InlineKeyboardButton("🇺🇸 United States(US)",callback_data="admin:usa:instagram"),
        InlineKeyboardButton("🇳🇱 Netetherlands(NL)",callback_data="admin:netherlands:instagram")

    ],
    [
        InlineKeyboardButton("🇰🇬 Kyrgyzstan(KG)",callback_data="admin:kyrgyzstan:instagram"),
        InlineKeyboardButton("🇮🇩 Indonesia(ID)",callback_data="admin:indonesia:instagram")

    ],
    [
        InlineKeyboardButton("🇰🇭 Combodia(KH)",callback_data="admin:combodia:instagram"),
        InlineKeyboardButton("🇷🇴 Romania(RO)",callback_data="admin:romania:instagram")

    ],
    [
        InlineKeyboardButton("🇻🇳 Vietnam(VN)",callback_data="admin:vietnam:instagram"),
        InlineKeyboardButton("🇸🇬 Singapure(SG)",callback_data="admin:singapure:instagram")
    ],
    [
        InlineKeyboardButton("🇨🇭 Switzerland(CH)",callback_data="admin:switzerland:instagram"),
        InlineKeyboardButton("🇩🇪 Germany(DE)",callback_data="admin:germany:instagram"),



    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]
])

facebook = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇸🇰 Slovakia(SK)",callback_data="admin:slovakia:facebook"), 
        InlineKeyboardButton("🇮🇳 India(IN)",callback_data="admin:india:facebook"), 

    ],
    [

        InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="admin:russia:facebook"), 
        InlineKeyboardButton("🇧🇷 Brazil(BR)",callback_data="admin:brazil:facebook") 

    ],
    [
        InlineKeyboardButton("🇺🇸 United States(US)",callback_data="admin:unitedstates:facebook"), 
        InlineKeyboardButton("🇧🇬 Bulgaria(BG)",callback_data="admin:bulgaria:facebook") 

    ],
    [
        InlineKeyboardButton("🇰🇬 Kyrgyzstan(KG)",callback_data="admin:kyrgyzstan:facebook"), 
        InlineKeyboardButton("🇮🇩 Indonesia(ID)",callback_data="admin:unitedkingdom:facebook") 

    ],
    [
        InlineKeyboardButton("🇲🇳 Mongolia(MN)",callback_data="admin:mongolia:facebook"), 
        InlineKeyboardButton("🇵🇭 Philippens(PH)",callback_data="admin:philippens:facebook") 

    ],
    [
        InlineKeyboardButton("🇻🇳 Vietnam(VN)",callback_data="admin:vietnam:facebook"), 
        InlineKeyboardButton("🇬🇪 Georgia(GE)",callback_data="admin:georgia:facebook") 
    ],
    [
        InlineKeyboardButton("🇺🇦 Ukraine(UA)",callback_data="admin:ukraine:facebook"),
        InlineKeyboardButton("🇩🇪 Germany(DE)",callback_data="admin:germany:facebook"),


    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]
])
microsoft = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🇰🇬 Kyrgyzstan(KG)",callback_data="admin:kyrgyzstan:microsoft"),
        InlineKeyboardButton(text="🇻🇳 Vietnam(VN)",callback_data="admin:vietnam:microsoft")

    ],
    [
        InlineKeyboardButton(text="🇪🇪 Estonia(EE)",callback_data="admin:estonia:microsoft"),
        InlineKeyboardButton(text="🇨🇦 Canada(CA)",callback_data="admin:canada:microsoft")

    ],
    [
        InlineKeyboardButton(text="🇮🇳 India(IN)",callback_data="admin:india:microsoft"),
        InlineKeyboardButton(text="🇮🇩 Indonesia(ID)",callback_data="admin:indonesia:microsoft")

    ],
    [
        InlineKeyboardButton(text="🇳🇱 Netetherlands(NL)",callback_data="admin:netherlands:microsoft"),
        InlineKeyboardButton(text="🇷🇺 Russian Federation(RU)",callback_data="admin:russia:microsoft")

    ],
    [
        InlineKeyboardButton(text="🇧🇷 Brazil(BR)",callback_data="admin:brazil:microsoft"),
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")

    ]
])

apple = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🇰🇭 Combodia(KH)",callback_data="admin:combodia:microsoft"),
        InlineKeyboardButton(text="🇹🇹 Trininand and Tobago(TT)",callback_data="admin:tobago:microsoft")

    ],
    [
        InlineKeyboardButton(text="🇨🇳 China(CN)",callback_data="admin:china:microsoft"),
        InlineKeyboardButton(text="🇷🇺 Russian Federation(RU)",callback_data="admin:russia:microsoft")

    ],
    [
        InlineKeyboardButton(text="🇮🇳 India(IN)",callback_data="admin:india:microsoft"),
        InlineKeyboardButton(text="🇻🇳 Vietnam(VN)",callback_data="admin:vietnam:microsoft")

    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")

    ]
])
paypal = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇸🇬 Singapore(SG)",callback_data="admin:singapore:pypal")

    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")

    ]
])

steam = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇦🇷 Argentinas(AR)",callback_data="admin:argentina:steam"),

        
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")
    ]
])
telegram = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇿🇦 South Africa(ZA)",callback_data="admin:africa:telegram"),
        InlineKeyboardButton("🇰🇬 Kyrgyzstan(KG)",callback_data="admin:kyrgyzstan:telegram")

      
    ],
    [
        InlineKeyboardButton("🇻🇪 Venezuela(VE)",callback_data="admin:venezuela:telegram"),
        InlineKeyboardButton("🇵🇰 Pakistan(PK)",callback_data="admin:pakistan:telegram")

      
    ],
    [
        InlineKeyboardButton("🇹🇷 Turkey(TR)",callback_data="admin:turkey:telegram"),
        InlineKeyboardButton("🇦🇷 Argentinas(AR)",callback_data="admin:argentina:telegram")

      
    ],
    [
        InlineKeyboardButton("🇮🇳 India(IN)",callback_data="admin:india:telegram"),
        InlineKeyboardButton("🇻🇳 Vietnam(VN)",callback_data="admin:vietnam:telegram")

      
    ],
    [
        InlineKeyboardButton("🇬🇧 United Kingdom(UK)",callback_data="admin:unitedkingdom:telegram"),
        InlineKeyboardButton("🇺🇸 United States(US)",callback_data="admin:unitedstates:telegram")

      
    ],
    [
        InlineKeyboardButton("🇹🇭 Thailand(TH)",callback_data="admin:thailand:telegram"),
        InlineKeyboardButton("🇲🇾 Malaysia(MY)",callback_data="admin:malaysia:telegram")

      
    ],
    [
        InlineKeyboardButton("🇨🇬 Congo(CG)",callback_data="admin:congo:telegram"),
        InlineKeyboardButton("🇧🇷 Brazil(BR)",callback_data="admin:brazil:telegram")

      
    ],
    [
        InlineKeyboardButton("🇺🇦 Ukraine(UA)",callback_data="admin:ukraine:telegram"),
        InlineKeyboardButton("🇪🇬 Egypt(EG)",callback_data="admin:egypt:telegram")

      
    ],
    [
        InlineKeyboardButton("🇵🇭 Philippens(PH)",callback_data="admin:philippens:telegram"),
        InlineKeyboardButton("🇮🇩 Indonesia(ID)",callback_data="admin:indonesia:telegram")

      
    ],
    [
        InlineKeyboardButton("🇰🇿 Kazakhstan(KZ)",callback_data="admin:kazakhstan:telegram"),
        InlineKeyboardButton("🇨🇦 Canada(CA)",callback_data="admin:canada:telegram")

      
    ],
    [
        InlineKeyboardButton("🇬🇹 Guatemala(GT)",callback_data="admin:guatemala:telegram"),
        InlineKeyboardButton("🇭🇰 Hong Kong(HK)",callback_data="admin:hongkong:telegram")

      
    ],
    [
        InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="admin:russia:telegram"),
        InlineKeyboardButton("🇷🇴 Romania(RO)",callback_data="admin:romania:telegram")

      
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]
])

uber = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🇩🇪 Germany(DE)",callback_data="admin:germany:uber"),
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]

])

twitter = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🇷🇺 Russian Federation(RU)",callback_data="admin:russia:twitter"),
        InlineKeyboardButton(text="🇧🇷 Brazil(BR)",callback_data="admin:brazil:twitter"),
    ],
    [
        InlineKeyboardButton(text="🇲🇾 Malaysia(MY)",callback_data="admin:malaysia:twitter"),
        InlineKeyboardButton(text="🇭🇺 Hungary(HU)",callback_data="admin:hungary:twitter"),
    ],
    [
        InlineKeyboardButton(text="🇰🇬 Kyrgyzstan(KG)",callback_data="admin:kyrgyzstan:twitter"),
        InlineKeyboardButton(text="🇺🇸 United States(US)",callback_data="admin:usa:twitter"),
    ],  
    [
        InlineKeyboardButton(text="🇪🇪 Estonia(EE)",callback_data="admin:estonia:twitter"),
        InlineKeyboardButton(text="🇮🇳 India(IN)",callback_data="admin:india:twitter"),
    ],
    [
        InlineKeyboardButton(text="🇻🇳 Vietnam(VN)",callback_data="admin:vietnam:twitter"),
        InlineKeyboardButton(text="🇳🇱 Netetherlands(NL)",callback_data="admin:netherlands:twitter"),
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]
])
whatsapp = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🇲🇽 Mexico(MX)",callback_data="admin:mexico:whatsapp"),
        InlineKeyboardButton(text="🇷🇺 Russian Federation(RU)",callback_data="admin:russia:whatsapp"),

    ],
    [
        InlineKeyboardButton(text="🇵🇱 Poland(PL)",callback_data="admin:poland:whatsapp"),
        InlineKeyboardButton(text="🇳🇪 Niger(NE)",callback_data="admin:niger:whatsapp"),
    ],
    [
        InlineKeyboardButton(text="🇰🇬 Kyrgyzstan(KG)",callback_data="admin:kyrgyzstan:whatsapp"),
        InlineKeyboardButton(text="🇪🇸 Spain(ES)",callback_data="admin:spain:whatsapp"),
    ],
    [
        InlineKeyboardButton(text="🇲🇦 Morocco(MA)",callback_data="admin:morocco:whatsapp"),
        InlineKeyboardButton(text="🇧🇷 Brazil(BR)",callback_data="admin:brazil:whatsapp"),
    ],
    [
        InlineKeyboardButton(text="🇧🇩 Bangladesh(BD)",callback_data="admin:bangladesh:whatsapp"),
        InlineKeyboardButton(text="🇹🇷 Turkey(TR)",callback_data="admin:india:whatsapp"),
    ],
    [
        InlineKeyboardButton(text="🇫🇷 France(FR)",callback_data="admin:france:whatsapp"),
        InlineKeyboardButton(text="🇺🇸 United States(US)",callback_data="admin:usa:whatsapp"), 
    ],
    [
        InlineKeyboardButton(text="🇰🇿 Kazakhstan(KZ)",callback_data="admin:kazakhstan:whatsapp"),
        InlineKeyboardButton(text="🇵🇰 Pakistan(PK)",callback_data="admin:pakistan:whatsapp"), 
    ],
    [
        InlineKeyboardButton(text="🇩🇪 Germany(DE)",callback_data="admin:germany:whatsapp"),
        InlineKeyboardButton(text="🇶🇦 Qatar(QA)",callback_data="admin:qatar:whatsapp"),   
    ],
    [
        InlineKeyboardButton(text="🇸🇪 Sweden(SE)",callback_data="admin:sweden:whatsapp"),
        InlineKeyboardButton(text="🇨🇦 Canada(CA)",callback_data="admin:canada:whatsapp"), 
    ],
    [
        InlineKeyboardButton(text="🇧🇭 Bahrain(BH)",callback_data="admin:bahrain:whatsapp"),
        InlineKeyboardButton(text="🇹🇭 Thailand(TH)",callback_data="admin:thailand:thailand"), 

    ],
    [
        InlineKeyboardButton(text="🇰🇼 Kuwait(KW)",callback_data="admin:kuwait:whatsapp"),
        InlineKeyboardButton(text="🇷🇴 Romania(RO)",callback_data="admin:romania:whatsapp"),   
    ],
    [
        InlineKeyboardButton(text="🇮🇹 Italy(IT)",callback_data="admin:italy:whatsapp"),
        InlineKeyboardButton(text="🇵🇭 Philippens(PH)",callback_data="admin:philippens:whatsapp"), 
    ],
    [
        InlineKeyboardButton(text="🇰🇭 Combodia(KH)",callback_data="admin:combodia:whatsapp"),
        InlineKeyboardButton(text="🇦🇺 Australia(AU)",callback_data="admin:australia:whatsapp"),   
    ],
    [
        InlineKeyboardButton(text="🇩🇰 Denmark(DK)",callback_data="admin:denmark:whatsapp"),
        InlineKeyboardButton(text="🇱🇹 Lithuania(LT)",callback_data="admin:lithuania:whatsapp"),   
    ],
    [
        InlineKeyboardButton(text="🇸🇬 Singapure(SG)",callback_data="admin:singapure:whatsapp"),
        InlineKeyboardButton(text="🇳🇿 New Zealand(NZ)",callback_data="admin:newzealand:whatsapp"),    
    ],
    [
        InlineKeyboardButton(text="🇭🇰 Hong Kong(HK)",callback_data="admin:hongkong:whatsapp"),
        InlineKeyboardButton(text="🇲🇾 Malaysia(MY)",callback_data="admin:malaysia:whatsapp"), 
    ],
    [
        InlineKeyboardButton(text="🇳🇱 Netherlands(NL)",callback_data="admin:netherlands:whatsapp"),
        InlineKeyboardButton(text="🇧🇲 Bermuda(BM)",callback_data="admin:bermuda:whatsapp"),   
    ],
    [
        InlineKeyboardButton(text="🇻🇳 Vietnam(VN)",callback_data="admin:vietnam:whatsapp"),
        InlineKeyboardButton(text="🇻🇪 Venezuela(VE)",callback_data="admin:venezuela:whatsapp"),   
    ],
    [
        InlineKeyboardButton(text="🇰🇪 Kenya(KE)",callback_data="admin:kenya:whatsapp"),
        InlineKeyboardButton(text="🇮🇩 Indonesia(ID)",callback_data="admin:indonesia:whatsapp"),   
    ],
    [
        InlineKeyboardButton(text="🇮🇳 India(IN)",callback_data="admin:india:whatsapp"),
        InlineKeyboardButton(text="🇸🇦 Saudi Arabia(SA)",callback_data="admin:saudiarabia:whatsapp"),  
    ],
    [
        InlineKeyboardButton(text="🇵🇹 Portugal(PT)",callback_data="admin:portugal:whatsapp"),
        
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]
])
vkontakte = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇰🇿 Kazakhstan(KZ)",callback_data="admin:kazakhstan:vkonatkte"),
        InlineKeyboardButton("🇮🇳 India(IN)",callback_data="admin:india:vkonatkte"),
    ],
    [
        InlineKeyboardButton("🇳🇱 Netherlands(NL)",callback_data="admin:netherlands:vkonatkte"),
        InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="admin:russia:vkonatkte"),
    ],
    [
        InlineKeyboardButton("🇪🇪 Estonia(EE)",callback_data="admin:estonia:vkonatkte"),
        InlineKeyboardButton("🇰🇬 Kyrgyzstan(KG)",callback_data="admin:kyrgyzstan:vkonatkte"),
    ],
    [
        InlineKeyboardButton("🇧🇷 Brazil(BR)",callback_data="admin:brazil:vkonatkte"),
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ],
])

tiktok = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇮🇩 Indonesia(ID)",callback_data="admin:indonesia:tiktok"),
        InlineKeyboardButton("🇻🇳 Vietnam(VN)",callback_data="admin:vietnam:tiktok")
    ],
    [
        InlineKeyboardButton("🇮🇳 India(IN)",callback_data="admin:india:tiktok"),

    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_one")
    ]
])
yandex = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="admin:russia:yandex"),
    
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")
    ]
])

gmail = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🇮🇳 India(IN)",callback_data="admin:india:Google"),
        InlineKeyboardButton("🇧🇷 Brazil(BR)",callback_data="admin:brazil:Google")
    ],
    [
        InlineKeyboardButton("🇰🇪 Kenya(KE)",callback_data="admin:kenya:Google"),
        InlineKeyboardButton("🇺🇦 Ukraine(UA)",callback_data="admin:ukarine:Google")
    ],
    [
        InlineKeyboardButton("🇫🇷 France(FR)",callback_data="admin:france:Google"),
        InlineKeyboardButton("🇵🇪 Peru(PE)",callback_data="admin:peru:Google")
    ],
    [
        InlineKeyboardButton("🇲🇽 Mexico(MX)",callback_data="admin:mexico:Google"),
        InlineKeyboardButton("🇹🇷 Turkey(TR)",callback_data="admin:turkey:Google")
    ],
    [
        InlineKeyboardButton("🇳🇮 Nicaragua(NI)",callback_data="admin:nicagura:Google"),
        InlineKeyboardButton("🇰🇬 Kyrgyzstan(KG)",callback_data="admin:kyrgyzstan:Google")
    ],
    [
        InlineKeyboardButton("🇰🇭 Combodia(KH)",callback_data="admin:colombia:Google"),
        InlineKeyboardButton("🇹🇭 Thailand(TH)",callback_data="admin:thailand:Google")
    ],
    [
        InlineKeyboardButton("🇺🇸 United States(US)",callback_data="admin:usa:Google"),
        InlineKeyboardButton("🇲🇾 Malaysia(MY)",callback_data="admin:malaysia:Google")
    ],
    [
        InlineKeyboardButton("🇷🇺 Russian Federation(RU)",callback_data="admin:russia:Google"),
             
    ],
    [
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_social_two")
    ]
])