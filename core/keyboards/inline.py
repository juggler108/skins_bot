from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_main_menu_ikb():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🗓 Запись Online', url='https://dikidi.net/436385?p=0.pi')
    keyboard_builder.button(text='🚗 Как нас найти', callback_data='how_find_us')
    keyboard_builder.button(text='🤔 Получить консультацию', callback_data='consultation')
    keyboard_builder.button(text='📱 Наши социальные сети', callback_data='social')
    keyboard_builder.button(text='📗 О нас', callback_data='about')
    keyboard_builder.button(text='❓ FAQ', callback_data='faq')
    keyboard_builder.adjust(1, 1, 1, 1, 1, 1)
    return keyboard_builder.as_markup()


def get_our_location_ikb():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='2Гис', url='https://2gis.ru/spb/firm/70000001053632571'),
    keyboard_builder.button(text='Яндекс карты', url='https://yandex.com.ge/profile/114701010916'),
    keyboard_builder.button(text='🧰 Основное меню', callback_data='main_menu')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()


def get_consultation_ikb():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Александр - массажист', url='https://t.me/dudkinsasha108')
    keyboard_builder.button(text='Ольга - мастер депиляции', url='https://t.me/Olga_depil108')
    keyboard_builder.button(text='🧰 Основное меню', callback_data='main_menu')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()


def get_our_social_ikb():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🐳 Вконтакте', url='https://vk.com/saffron108')
    keyboard_builder.button(text='🧰 Основное меню', callback_data='main_menu')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def get_main_menu_button():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🧰 Основное меню', callback_data='main_menu')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()
