from string import punctuation

from aiogram import types, Router
from filters.chat_types import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup', ]))

restricted_words = {'кабан', 'хомяк', 'боба'}

def clean_text(text: str):
  return text.lower().translate(str.maketrans('', '', punctuation))


@user_group_router.edited_message()
@user_group_router.message()
async def cleaner(message: types.Message):
  if restricted_words.intersection(clean_text(message.text.lower()).split()):
    await message.answer(f'{message.from_user.full_name}, соблюдайте порядок в чате, а то забаню!')
    await message.delete()
    # await message.chat.ban(message.from_user.id)