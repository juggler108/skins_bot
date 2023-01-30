from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from core.keyboards.inline import get_main_menu_ikb, get_our_location_ikb, get_consultation_ikb, get_our_social_ikb, \
    get_main_menu_button
from core.utils.dbconnect import add_data_sqlite


async def get_start(message: Message):
    await add_data_sqlite(message.from_user.id, message.from_user.first_name)
    await message.answer(text=f'Привет <b>{message.from_user.first_name}</b>. Рад Вас видеть!\n'
                              f'Я бот студии <b>массажа</b> и <b>депиляции</b>.\nПомогу:\n\n'
                              f'🤔 Найти ответы на вопросы\n'
                              f'🚀 Связаться с нужным специалистом\n'
                              f'🗓 Записаться на процедуры\n\n'
                              f'Что Вас интересует?\n\n',
                         reply_markup=get_main_menu_ikb())
    await message.delete()


async def get_main_menu(callback: CallbackQuery, bot: Bot):
    await bot.send_message(chat_id=callback.from_user.id,
                           text='🧰 Основное меню ⤵⤵⤵',
                           reply_markup=get_main_menu_ikb())
    await callback.message.delete()
    await callback.answer()


async def get_consultation(callback: CallbackQuery, bot: Bot):
    await bot.send_message(chat_id=callback.from_user.id,
                           text='🤔 Какую консультыцию вы хотели бы получить? ⤵⤵⤵',
                           reply_markup=get_consultation_ikb())
    await callback.message.delete()
    await callback.answer()


async def get_faq(callback: CallbackQuery):
    await callback.answer(text='Эта информация обновляется. Вы можете затать свой вопрос '
                               'в разделе "Получить консультацию"',
                          show_alert=True)


async def get_our_location(callback: CallbackQuery, bot: Bot):
    await bot.send_message(chat_id=callback.from_user.id,
                           text=f'🚗 Нас можно найти здесь ⤵⤵⤵',
                           reply_markup=get_our_location_ikb())
    await callback.message.delete()
    await callback.answer()


async def get_our_social(callback: CallbackQuery, bot: Bot):
    await bot.send_message(chat_id=callback.from_user.id,
                           text='📱 Наши социальные сети ⤵⤵⤵',
                           reply_markup=get_our_social_ikb())
    await callback.message.delete()
    await callback.answer()


async def get_about_us(callback: CallbackQuery, bot: Bot):
    await bot.send_message(chat_id=callback.from_user.id,
                           text='Студия Шафран – это не только оздоровительный массаж, депиляция без боли и '
                                'профессиональное тейпирование, но и забота о каждом клиенте, индивидуальный подход и '
                                'расслабляющая атмосфера. Наши мастера имеют большой опыт работы и постоянно учатся, '
                                'чтобы идти в ногу со временем и соответствовать новейшим трендам. Вас ждут сеансы '
                                'лечебного и реабилитационного массажа, быстрое восстановление после родов, а также '
                                'ценные рекомендации по поддержанию здоровья. Уникальная процедура тейпирования '
                                'способна облегчить симптомы почти любой болезни. Мастер депиляции проведет сеанс '
                                'легко и безболезненно, оставив лишь гладкую кожу и уверенность в себе. Мы используем '
                                'только натуральные экологичные материалы, не вызывающие раздражение кожи. Мы дорожим '
                                'нашими посетителями, поэтому многие из них уже стали постоянными. Вы точно оцените '
                                'теплую атмосферу салона и высокую квалификацию наших мастеров.',
                           reply_markup=get_main_menu_button())
    await callback.message.delete()
    await callback.answer()
