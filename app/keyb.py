from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Новое напоминание", callback_data="newtask")],])


month = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Январь", callback_data="month_one"), InlineKeyboardButton(text="Февраль", callback_data="month_two"), InlineKeyboardButton(text="Март", callback_data="month_three")],
                                     [InlineKeyboardButton(text="Апрель", callback_data="month_four"), InlineKeyboardButton(text="Май", callback_data="month_five"), InlineKeyboardButton(text="Июнь", callback_data="month_six")],
                                     [InlineKeyboardButton(text="Июль", callback_data="month_seven"), InlineKeyboardButton(text="Август", callback_data="month_eight"), InlineKeyboardButton(text="Сентябрь", callback_data="month_nine")],
                                     [InlineKeyboardButton(text="Октябрь", callback_data="month_ten"), InlineKeyboardButton(text="Ноябрь", callback_data="month_eleven"), InlineKeyboardButton(text="Декабрь", callback_data="month_twelve")]],)



number_31 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="1", callback_data="day_One"), InlineKeyboardButton(text="2", callback_data="day_Two"), InlineKeyboardButton(text="3", callback_data="day_Three")],
                                     [InlineKeyboardButton(text="4", callback_data="day_Four"), InlineKeyboardButton(text="5", callback_data="day_Five"), InlineKeyboardButton(text="6", callback_data="day_Six")],
                                     [InlineKeyboardButton(text="7", callback_data="day_Seven"), InlineKeyboardButton(text="8", callback_data="day_Eight"), InlineKeyboardButton(text="9", callback_data="day_Nine")],
                                     [InlineKeyboardButton(text="10", callback_data="day_Ten"), InlineKeyboardButton(text="11", callback_data="day_Eleven"), InlineKeyboardButton(text="12", callback_data="day_Twelve")],
                                     [InlineKeyboardButton(text="13", callback_data="day_Thirteen"), InlineKeyboardButton(text="14", callback_data="day_Fourteen"), InlineKeyboardButton(text="15", callback_data="day_Fifteen")],
                                     [InlineKeyboardButton(text="16", callback_data="day_Sixteen"), InlineKeyboardButton(text="17", callback_data="day_Seventeen"), InlineKeyboardButton(text="18", callback_data="day_Eighteen")],
                                     [InlineKeyboardButton(text="19", callback_data="day_Nineteen"), InlineKeyboardButton(text="20", callback_data="day_Twenty"), InlineKeyboardButton(text="21", callback_data=" day_Twenty-one")],
                                     [InlineKeyboardButton(text="22", callback_data=" day_Twenty-two"), InlineKeyboardButton(text="23", callback_data="day_Twenty-three"), InlineKeyboardButton(text="24", callback_data="day_Twenty-four")],
                                     [InlineKeyboardButton(text="25", callback_data="day_Twenty-five"), InlineKeyboardButton(text="26", callback_data="day_Twenty-six"), InlineKeyboardButton(text="27", callback_data="day_Twenty-seven")],
                                     [InlineKeyboardButton(text="28", callback_data="day_Twenty-eight"), InlineKeyboardButton(text="29", callback_data="day_Twenty-nine"), InlineKeyboardButton(text="30", callback_data="day_Thirty")],
                                      [InlineKeyboardButton(text="31", callback_data="day_Thirty-one")]],)


number_28 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="1", callback_data="day_One"), InlineKeyboardButton(text="2", callback_data="day_Two"), InlineKeyboardButton(text="3", callback_data="day_Three")],
                                     [InlineKeyboardButton(text="4", callback_data="day_Four"), InlineKeyboardButton(text="5", callback_data="day_Five"), InlineKeyboardButton(text="6", callback_data="day_Six")],
                                     [InlineKeyboardButton(text="7", callback_data="day_Seven"), InlineKeyboardButton(text="8", callback_data="day_Eight"), InlineKeyboardButton(text="9", callback_data="day_Nine")],
                                     [InlineKeyboardButton(text="10", callback_data="day_Ten"), InlineKeyboardButton(text="11", callback_data="day_Eleven"), InlineKeyboardButton(text="12", callback_data="day_Twelve")],
                                     [InlineKeyboardButton(text="13", callback_data="day_Thirteen"), InlineKeyboardButton(text="14", callback_data="day_Fourteen"), InlineKeyboardButton(text="15", callback_data="day_Fifteen")],
                                     [InlineKeyboardButton(text="16", callback_data="day_Sixteen"), InlineKeyboardButton(text="17", callback_data="day_Seventeen"), InlineKeyboardButton(text="18", callback_data="day_Eighteen")],
                                     [InlineKeyboardButton(text="19", callback_data="day_Nineteen"), InlineKeyboardButton(text="20", callback_data="day_Twenty"), InlineKeyboardButton(text="21", callback_data=" day_Twenty-one")],
                                     [InlineKeyboardButton(text="22", callback_data=" day_Twenty-two"), InlineKeyboardButton(text="23", callback_data="day_Twenty-three"), InlineKeyboardButton(text="24", callback_data="day_Twenty-four")],
                                     [InlineKeyboardButton(text="25", callback_data="day_Twenty-five"), InlineKeyboardButton(text="26", callback_data="day_Twenty-six"), InlineKeyboardButton(text="27", callback_data="day_Twenty-seven")],
                                     [InlineKeyboardButton(text="28", callback_data="day_Twenty-eight")]])


number_30 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="1", callback_data="day_One"), InlineKeyboardButton(text="2", callback_data="day_Two"), InlineKeyboardButton(text="3", callback_data="day_Three")],
                                     [InlineKeyboardButton(text="4", callback_data="day_Four"), InlineKeyboardButton(text="5", callback_data="day_Five"), InlineKeyboardButton(text="6", callback_data="day_Six")],
                                     [InlineKeyboardButton(text="7", callback_data="day_Seven"), InlineKeyboardButton(text="8", callback_data="day_Eight"), InlineKeyboardButton(text="9", callback_data="day_Nine")],
                                     [InlineKeyboardButton(text="10", callback_data="day_Ten"), InlineKeyboardButton(text="11", callback_data="day_Eleven"), InlineKeyboardButton(text="12", callback_data="day_Twelve")],
                                     [InlineKeyboardButton(text="13", callback_data="day_Thirteen"), InlineKeyboardButton(text="14", callback_data="day_Fourteen"), InlineKeyboardButton(text="15", callback_data="day_Fifteen")],
                                     [InlineKeyboardButton(text="16", callback_data="day_Sixteen"), InlineKeyboardButton(text="17", callback_data="day_Seventeen"), InlineKeyboardButton(text="18", callback_data="day_Eighteen")],
                                     [InlineKeyboardButton(text="19", callback_data="day_Nineteen"), InlineKeyboardButton(text="20", callback_data="day_Twenty"), InlineKeyboardButton(text="21", callback_data=" day_Twenty-one")],
                                     [InlineKeyboardButton(text="22", callback_data=" day_Twenty-two"), InlineKeyboardButton(text="23", callback_data="day_Twenty-three"), InlineKeyboardButton(text="24", callback_data="day_Twenty-four")],
                                     [InlineKeyboardButton(text="25", callback_data="day_Twenty-five"), InlineKeyboardButton(text="26", callback_data="day_Twenty-six"), InlineKeyboardButton(text="27", callback_data="day_Twenty-seven")],
                                     [InlineKeyboardButton(text="28", callback_data="day_Twenty-eight"), InlineKeyboardButton(text="29", callback_data="day_Twenty-nine"), InlineKeyboardButton(text="30", callback_data="day_Thirty")]],)

check = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Да", callback_data="Yes_1")],
                                              [InlineKeyboardButton(text="Нет", callback_data="No_0")]])

task = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Текст", callback_data="text")],
                                              [InlineKeyboardButton(text="Месяц", callback_data="m")],
                                              [InlineKeyboardButton(text="Число", callback_data="n")],
                                              [InlineKeyboardButton(text="Время", callback_data="t")]])