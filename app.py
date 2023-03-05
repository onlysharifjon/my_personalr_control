import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.default.startkey import startbut, startbutl, xodimlar

shablon = []
API_TOKEN = '6127618874:AAEJMqXRgqBx5waHJ0EifgNkCRdu8d2SJ9w'

logging.basicConfig(level=logging.INFO)
d = []
ADMINS = [5172746353, 233029021]


class NameStates(StatesGroup):
    name_step = State()
    familiya = State()
    Sharif = State()
    shir = State()
    seriya_num = State()
    seruya_number = State()
    name_avto = State()
    tel_num = State()
    uquv = State()
    result = State()
    region = State()


bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        f"<b>👋Assalomu Aleykum</b>\n\n<b>👤Hurmatli:</b> {message.from_user.first_name}\n\n<b>🤝Shartnoma tuzishni xohlaysizmi</b>",
        reply_markup=startbut)


@dp.message_handler(text='Orqaga🔙')
async def back_1(message: types.Message):
    await message.answer("Mal`lumotlarni qayta kiritishingiz mumkin")
    await message.answer("<b>👥Ismingizni kiriting !</b>", reply_markup=xodimlar)
    await NameStates.name_step.set()


@dp.message_handler(text="YOQ ❌")
async def yok(message: types.Message):
    await message.answer("Xayr Salomat bo`ling👋")


@dp.message_handler(text="HA ✅")
async def tr(message: types.Message, state: FSMContext):
    await message.answer("<b>👥Kompaniya nomini kiriting !</b>", reply_markup=xodimlar)
    await NameStates.name_step.set()


@dp.message_handler(state=NameStates.name_step, content_types=types.ContentTypes.TEXT)
async def ups(message: types.Message, state: FSMContext):
    if message.text == "Orqaga🔙":
        await message.answer("Mal`lumotlarni qayta kiritishingiz mumkin")
        await message.answer("<b>👥Ismingizni kiriting !</b>", reply_markup=xodimlar)
        await NameStates.name_step.set()
    else:
        names = message.text
        d.append(names)
        await message.answer("Xodimlar sonini kiriting")
        await state.finish()
        await NameStates.familiya.set()


@dp.message_handler(state=NameStates.familiya, content_types=types.ContentTypes.TEXT)
async def ups_och(message: types.Message, state: FSMContext):
    if message.text == "Orqaga🔙":
        await message.answer("Mal`lumotlarni qayta kiritishingiz mumkin")
        await message.answer("<b>👥Ismingizni kiriting !</b>", reply_markup=xodimlar)
        await NameStates.name_step.set()
    else:
        familiyas = message.text
        d.append(familiyas)
        await message.answer("<b>BotFather dan olingan Token ni kiriting</b>")
        await state.finish()
        await NameStates.Sharif.set()


@dp.message_handler(state=NameStates.Sharif, content_types=types.ContentTypes.TEXT)
async def ups_Sharifsw(message: types.Message, state: FSMContext):
    if message.text == "Orqaga🔙":
        await message.answer("Mal`lumotlarni qayta kiritishingiz mumkin")
        await message.answer("<b>👥Ismingizni kiriting !</b>", reply_markup=xodimlar)
        await NameStates.name_step.set()
    else:
        sharif_user = message.text
        d.append(sharif_user)
        await message.answer("Xodimlarni Ism Familyasi va User_id larini namunadagidek kiriting")
        await message.answer("NAMUNA\n\nXodim1 - User_ID1\nXodim2 - User_ID2\n.\n.\n.")
        await state.finish()
        await NameStates.shir.set()


@dp.message_handler(state=NameStates.shir, content_types=types.ContentTypes.TEXT)
async def ups_dirssk(message: types.Message, state: FSMContext):
    xodimlar = message.text
    d.append(xodimlar)
    tut = ["🏢Idora: ", "🧑🏻‍💻Xodimlar soni: ", "🤖Token: ", "Xodim- "]
    text = ""
    for i in range(len(d)):
        if i != 2:
            text = text + "\n\n" + f"<b>{tut[i]}</b>{str(d[i])}"
        else:
            text = text + "\n\n" + f"{str(d[i])}"
            text = text + "\n\n" + f"ADMIN ID = {message.from_user.id} : ADMIN Ismi -{message.from_user.full_name}"

    await message.answer(text)
    await message.answer("<b>Ma`lumotlar to`g`riligiga ishonch hosil qiling!</b>", reply_markup=startbut)
    await state.finish()
    await NameStates.region.set()

    @dp.message_handler(state=NameStates.region, content_types=types.ContentTypes.CONTACT)
    async def ups_dirssk(message: types.Message, state: FSMContext):
        con = message.contact
        await message.answer("Sizning ma`lumotlaringiz Adminga jo`natildi ")
        for i in range(len(ADMINS)):
            await bot.send_message(ADMINS[i], "✅YANGI XABAR")
            await bot.send_contact(ADMINS, con)
            await bot.send_message(ADMINS[i], text)
        d.clear()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
