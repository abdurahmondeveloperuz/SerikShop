from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("📱 Купить номер",callback_data="buy_number"),
        InlineKeyboardButton("🔝 Пополнить баланс",callback_data="top_balance"),

    ],
    [

        InlineKeyboardButton("📊 Cтатистика",callback_data="sts"),
        InlineKeyboardButton("💰 Мой баланс",callback_data="balance")
    ],
])


admin_tugma =  InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="👨‍💻 Панель администратора", callback_data="admin_panel")
        
    ]]
)

ortga_to_panel =  InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_panel")        
    ]]
)
ortga_to_main =  InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_main")        
    ]]
)

panel_tugma = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="📩 Реклама | 👤 Сообщение пользователю", callback_data="rek_user_message"),
        InlineKeyboardButton(text="📢 Настройки канала", callback_data="channel_tools")

    ],
    [
        InlineKeyboardButton(text="👤 Пользовательские настройки",callback_data='users_settings'),
        InlineKeyboardButton(text="🔻 Настройки бана", callback_data="ban_tools"),
    ],
    [
        InlineKeyboardButton(text="🤖 Настройки бота ",callback_data="bot_on_off"),
        InlineKeyboardButton(text="💰 Цены на номера",callback_data="number_prices"),

    ],
    [
        InlineKeyboardButton(text="💰 Balans API ",callback_data="balance_api"),

    ]
]
)
user_tools = InlineKeyboardMarkup(inline_keyboard=[
    [

        InlineKeyboardButton(text="💰 Добавить ₽ на счет", callback_data="add_funds"),
        InlineKeyboardButton(text="💰 Списать ₽ со счета", callback_data="minus_funds"), 

    ],
    [
        InlineKeyboardButton(text="🤖Информация oб yчетной записи",callback_data="inform_user")

    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="ortga_panel")     
    ]

]

)
channel_tools = InlineKeyboardMarkup(inline_keyboard=[
    [

        InlineKeyboardButton(text="📢 Добавить канал", callback_data="new_channel"),
        InlineKeyboardButton(text="📢 Извлечь каналы", callback_data="del_all_channels"), 

    ],
    [
        InlineKeyboardButton(text="🔖 Список каналов",callback_data="channels_list")

    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="ortga_panel")     
    ]

]

)
ban_tools = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🚫Заблокировать пользователя", callback_data="ban_man"),
        InlineKeyboardButton(text="🛑Разблокировать пользователя", callback_data="unban_man")
    ],
    [
        InlineKeyboardButton(text="🛑Разблокировать пользователей (всех)", callback_data="unban_men"),
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="ortga_panel")

    ]
]
)
bot_on_off = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="✅ Бот вкл",callback_data="bot_on"),
        InlineKeyboardButton(text="❌ Бот выкл",callback_data="bot_off")
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="ortga_panel") 
    ]
])


tugmasi = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="📩 Реклама", callback_data="rek_xb"),
        InlineKeyboardButton(text="👤 Сообщение пользователю", callback_data="user_xb"),
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="ortga_panel")     
    ]
]


)
tugmasi_rek = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="💬 Пересланное сообщение", callback_data="forward_xb_rek"),
        InlineKeyboardButton(text="✍️ Простое сообщение", callback_data="oddiy_xb_rek"),
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="ortga_panel")     
    ]
])
tugmasi_user = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="💬 Пересланное сообщение", callback_data="forward_xb_user"),
        InlineKeyboardButton(text="✍️ Простое сообщениe", callback_data="oddiy_xb_user"),
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="ortga_panel")     
    ]
    
])


numbers_list_one = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🛎 Instagram",callback_data="instagram"),
        InlineKeyboardButton(text="🛎 Facebook",callback_data="facebook")
    ],
    [
        InlineKeyboardButton(text="🛎 Ebay",callback_data="ebay"),
        InlineKeyboardButton(text="🛎 Tinder",callback_data="tinder")

    ],
    [
        InlineKeyboardButton(text="🛎 Telegram",callback_data="telegram"),
        InlineKeyboardButton(text="🛎 Uber",callback_data="uber")
    ],
    [
        InlineKeyboardButton(text="🛎 Twitter",callback_data="twitter"),
        InlineKeyboardButton(text="🛎 What's up",callback_data="whatsup")
    ],
    [
        InlineKeyboardButton(text="🛎 Vkontakte",callback_data="vkontakte"),
        InlineKeyboardButton(text="🛎 Tik Tok",callback_data="tiktok")
    ],
    [
        InlineKeyboardButton(text="🛎 SberMarket",callback_data="sbermarket"),
 
    ],
    [
        InlineKeyboardButton(text="🔜 Следующий",callback_data="next"),
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_main") 
    ]
])

numbers_list_two = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🛎 Yandex",callback_data="yandex"),
        InlineKeyboardButton(text="🛎 Gmail",callback_data="gmail"),

    ],
    [
        InlineKeyboardButton(text="🛎 PayPal",callback_data="paypal"),
        InlineKeyboardButton(text="🛎 Steam",callback_data="steam")
    ],  
    [
        InlineKeyboardButton(text="🛎 Amazon",callback_data="amazon"),
        InlineKeyboardButton(text="🛎 Discord",callback_data="discord")
    ],
    [
        InlineKeyboardButton(text="🛎 Avito",callback_data="avito"),
        InlineKeyboardButton(text="🛎 Samokat",callback_data="samokat")
    ],
    [
        InlineKeyboardButton(text="🛎 Microsoft",callback_data="microsoft"),
        InlineKeyboardButton(text="🛎 Apple",callback_data="apple")
    ],
    [
        InlineKeyboardButton(text="🔙 Предыдущий",callback_data="previus"),
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_main")  

    ]
])


numbers_list_one_admin = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🛎 Instagram",callback_data="instagram_edit"),
        InlineKeyboardButton(text="🛎 Facebook",callback_data="facebook_edit")
    ],
    [
        InlineKeyboardButton(text="🛎 Ebay",callback_data="ebay_edit"),
        InlineKeyboardButton(text="🛎 Tinder",callback_data="tinder_edit")

    ],
    [
        InlineKeyboardButton(text="🛎 Telegram",callback_data="telegram_edit"),
        InlineKeyboardButton(text="🛎 Uber",callback_data="uber_edit")
    ],
    [
        InlineKeyboardButton(text="🛎 Twitter",callback_data="twitter_edit"),
        InlineKeyboardButton(text="🛎 What's up",callback_data="whatsup_edit")
    ],
    [
        InlineKeyboardButton(text="🛎 Vkontakte",callback_data="vkontakte_edit"),
        InlineKeyboardButton(text="🛎 Tik Tok",callback_data="tiktok_edit")
    ],
    [
        InlineKeyboardButton(text="🛎 SberMarket",callback_data="sbermarket_edit"),
 
    ],
    [
        InlineKeyboardButton(text="🔜 Следующий",callback_data="next_edit"),
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_main") 
    ]
])

numbers_list_two_admin = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🛎 Yandex",callback_data="yandex_edit"),
        InlineKeyboardButton(text="🛎 Gmail",callback_data="gmail_edit"),

    ],
    [
        InlineKeyboardButton(text="🛎 PayPal",callback_data="paypal_edit"),
        InlineKeyboardButton(text="🛎 Steam",callback_data="steam_edit")
    ],  
    [
        InlineKeyboardButton(text="🛎 Amazon",callback_data="amazon_edit"),
        InlineKeyboardButton(text="🛎 Discord",callback_data="discord_edit")
    ],
    [
        InlineKeyboardButton(text="🛎 Avito",callback_data="avito_edit"),
        InlineKeyboardButton(text="🛎 Samokat",callback_data="samokat_edit")
    ],
    [
        InlineKeyboardButton(text="🛎 Microsoft",callback_data="microsoft_edit"),
        InlineKeyboardButton(text="🛎 Apple",callback_data="apple_edit")
    ],
    [
        InlineKeyboardButton(text="🔙 Предыдущий",callback_data="previus_edit"),
        InlineKeyboardButton(text="🔙 Hазад", callback_data="ortga_to_main")  

    ]
])


