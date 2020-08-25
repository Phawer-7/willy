from telebot import types

HOROSCOPE = {
    "Овен": "aries",
    "Телец": "taurus",
    "Близнецы": "gemini",
    "Рак": "cancer",
    "Лев": "lion",
    "Дева": "virgo",
    "Весы": "libra",
    "Скорпион": "scorpio",
    "Стрелец": "sagittarius",
    "Козерог": "capricorn",
    "Водолей": "aquarius",
    "Рыбы": "pisces",
}

inline_horoscope = types.InlineKeyboardMarkup()
inline_horoscope.row(types.InlineKeyboardButton(text="Овен", callback_data=f'{HOROSCOPE["Овен"]}'),
                     types.InlineKeyboardButton(text="Телец", callback_data=f'{HOROSCOPE["Телец"]}'))

inline_horoscope.row(types.InlineKeyboardButton(text="Близнецы", callback_data=f'{HOROSCOPE["Близнецы"]}'),
                     types.InlineKeyboardButton(text="Рак", callback_data=f'{HOROSCOPE["Рак"]}'))

inline_horoscope.row(types.InlineKeyboardButton(text="Лев", callback_data=f'{HOROSCOPE["Лев"]}'),
                     types.InlineKeyboardButton(text="Дева", callback_data=f'{HOROSCOPE["Дева"]}'))

inline_horoscope.row(types.InlineKeyboardButton(text="Весы", callback_data=f'{HOROSCOPE["Весы"]}'),
                     types.InlineKeyboardButton(text="Скорпион", callback_data=f'{HOROSCOPE["Скорпион"]}'))

inline_horoscope.row(types.InlineKeyboardButton(text="Стрелец", callback_data=f'{HOROSCOPE["Стрелец"]}'),
                     types.InlineKeyboardButton(text="Козерог", callback_data=f'{HOROSCOPE["Козерог"]}'))

inline_horoscope.row(types.InlineKeyboardButton(text="Водолей", callback_data=f'{HOROSCOPE["Водолей"]}'),
                     types.InlineKeyboardButton(text="Рыбы", callback_data=f'{HOROSCOPE["Рыбы"]}'))
