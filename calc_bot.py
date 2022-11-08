import logging
import modul as m
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (ApplicationBuilder, ContextTypes, CommandHandler,
        ConversationHandler, MessageHandler, filters)

first, second, third, fourth, fifth, sixth = range(6)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO, filename='calc_bot.log', filemode='w')
reply_keyboard1 = [
    ['Рациональные', 'Комплексные'],
    ['Выйти из калькулятора'],]
markup1 = ReplyKeyboardMarkup(reply_keyboard1, one_time_keyboard=True)
reply_keyboard2 = [
    ['Сложение', 'Вычитание'],
    ['Умножение', 'Деление'],]
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}\n'
                f'Я бот-калькулятор.')
    await update.message.reply_text('С какими числами будем работать?',
        reply_markup=markup1,)
    return first

async def input_rat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text('Введите два числа через пробел. Пример, 3/5 7/15')
    return second

async def input_com(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text('Введите два числа через пробел. Пример, 1+2j 7+3j')
    return third

async def add_rat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global text
    sum = m.add_r(text)
    await update.message.reply_text(f'{sum}')
    await update.message.reply_text('С какими числами будем работать?',
        reply_markup=markup1,)
    return first

async def sub_rat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global text
    sub = m.sub_r(text)
    await update.message.reply_text(f'{sub}')
    await update.message.reply_text('С какими числами будем работать?',
        reply_markup=markup1,)
    return first

async def mult_rat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global text
    mult = m.mult_r(text)
    await update.message.reply_text(f'{mult}')
    await update.message.reply_text('С какими числами будем работать?',
        reply_markup=markup1,)
    return first

async def div_rat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global text
    div = m.div_r(text)
    await update.message.reply_text(f'{div}')
    await update.message.reply_text('С какими числами будем работать?',
        reply_markup=markup1,)
    return first

async def add_com(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global text
    sum = m.add_c(text)
    await update.message.reply_text(f'{sum}')
    await update.message.reply_text('С какими числами будем работать?',
        reply_markup=markup1,)
    return first

async def sub_com(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global text
    sub = m.sub_c(text)
    await update.message.reply_text(f'{sub}')
    await update.message.reply_text('С какими числами будем работать?',
        reply_markup=markup1,)
    return first

async def mult_com(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global text
    mult = m.mult_c(text)
    await update.message.reply_text(f'{mult}')
    await update.message.reply_text('С какими числами будем работать?',
        reply_markup=markup1,)
    return first

async def div_com(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    global text
    div = m.div_c(text)
    await update.message.reply_text(f'{div}')
    await update.message.reply_text('С какими числами будем работать?',
        reply_markup=markup1,)
    return first

async def save_input_r(update: Update, context: ContextTypes.DEFAULT_TYPE) ->  int:
    global text
    text = update.message.text
    await update.message.reply_text('Какое арифметическое действие выберете?',
        reply_markup=markup2,)
    return fourth

async def save_input_c(update: Update, context: ContextTypes.DEFAULT_TYPE) ->  int:
    global text
    text = update.message.text
    await update.message.reply_text(text)
    await update.message.reply_text('Какое арифметическое действие выберете?',
        reply_markup=markup2,)
    return sixth

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text('Вы вышли из калькулятора')
    return ConversationHandler.END

if __name__ == '__main__':
    token_bot = 'Ваш токен'
    app = ApplicationBuilder().token(token_bot).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            first: [
                MessageHandler(filters.Regex('^Рациональные$'), input_rat),
                MessageHandler(filters.Regex('^Комплексные$'), input_com),
            ],
            second: [
                MessageHandler(filters.TEXT & ~(filters.COMMAND), save_input_r),
            ],
            third: [
                MessageHandler(filters.TEXT & ~(filters.COMMAND), save_input_c),
            ],
            fourth: [
                MessageHandler(filters.Regex('^Сложение$'), add_rat),
                MessageHandler(filters.Regex('^Вычитание$'), sub_rat),
                MessageHandler(filters.Regex('^Умножение$'), mult_rat),
                MessageHandler(filters.Regex('^Деление$'), div_rat),
            ],
            sixth: [
                MessageHandler(filters.Regex('^Сложение$'), add_com),
                MessageHandler(filters.Regex('^Вычитание$'), sub_com),
                MessageHandler(filters.Regex('^Умножение$'), mult_com),
                MessageHandler(filters.Regex('^Деление$'), div_com),
            ],
        },
        fallbacks=[MessageHandler(filters.Regex("^Выйти из калькулятора$"), end)],
    )

    app.add_handler(conv_handler)

    app.run_polling()
