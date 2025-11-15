from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Новое напоминание", callback_data="newtask")],
                                     [InlineKeyboardButton(text="Мои напоминания", url="https://www.youtube.com/watch?v=qRyshRUA0xM&list=PLV0FNhq3XMOJ31X9eBWLIZJ4OVjBwb-KM&index=4")]],)


month = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Январь", callback_data="month_one"), InlineKeyboardButton(text="Февраль", callback_data="month_two"), InlineKeyboardButton(text="Март", callback_data="month_three")],
                                     [InlineKeyboardButton(text="Апрель", callback_data="month_four"), InlineKeyboardButton(text="Май", callback_data="month_five"), InlineKeyboardButton(text="Июнь", callback_data="month_six")],
                                     [InlineKeyboardButton(text="Июль", callback_data="month_seven"), InlineKeyboardButton(text="Август", callback_data="month_eight"), InlineKeyboardButton(text="Сентябрь", callback_data="month_nine")],
                                     [InlineKeyboardButton(text="Октябрь", callback_data="month_ten"), InlineKeyboardButton(text="Ноябрь", callback_data="month_eleven"), InlineKeyboardButton(text="Декабрь", callback_data="month_twelve")]],)



number = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Январь", callback_data="month_one"), InlineKeyboardButton(text="Февраль", callback_data="month_two"), InlineKeyboardButton(text="Март", callback_data="month_three")],
                                     [InlineKeyboardButton(text="Апрель", callback_data="month_four"), InlineKeyboardButton(text="Май", callback_data="month_five"), InlineKeyboardButton(text="Июнь", callback_data="month_six")],
                                     [InlineKeyboardButton(text="Июль", callback_data="month_seven"), InlineKeyboardButton(text="Август", callback_data="month_eight"), InlineKeyboardButton(text="Сентябрь", callback_data="month_nine")],
                                     [InlineKeyboardButton(text="Октябрь", callback_data="month_ten"), InlineKeyboardButton(text="Ноябрь", callback_data="month_eleven"), InlineKeyboardButton(text="Декабрь", callback_data="month_twelve")],
                                     [InlineKeyboardButton(text="Январь", callback_data="month_one"), InlineKeyboardButton(text="Февраль", callback_data="month_two"), InlineKeyboardButton(text="Март", callback_data="month_three")],
                                     [InlineKeyboardButton(text="Апрель", callback_data="month_four"), InlineKeyboardButton(text="Май", callback_data="month_five"), InlineKeyboardButton(text="Июнь", callback_data="month_six")],
                                     [InlineKeyboardButton(text="Июль", callback_data="month_seven"), InlineKeyboardButton(text="Август", callback_data="month_eight"), InlineKeyboardButton(text="Сентябрь", callback_data="month_nine")],
                                     [InlineKeyboardButton(text="Октябрь", callback_data="month_ten"), InlineKeyboardButton(text="Ноябрь", callback_data="month_eleven"), InlineKeyboardButton(text="Декабрь", callback_data="month_twelve")],
                                     [InlineKeyboardButton(text="Январь", callback_data="month_one"), InlineKeyboardButton(text="Февраль", callback_data="month_two"), InlineKeyboardButton(text="Март", callback_data="month_three")],
                                     [InlineKeyboardButton(text="Январь", callback_data="month_one"), InlineKeyboardButton(text="Февраль", callback_data="month_two"), InlineKeyboardButton(text="Март", callback_data="month_three")]],)

