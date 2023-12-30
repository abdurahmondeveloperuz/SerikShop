from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "📯Запуск бота"),
            types.BotCommand("help", "📄Руководство по использованию бота!"),
        ]
    )
