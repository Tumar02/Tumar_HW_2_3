from aiogram.utils import executor
import logging

from config import dp
from handlers import handler, callback, extra, admin

handler.register_handlers(dp)
callback.register_callback(dp)
extra.register_extra(dp)
admin.register_admin(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)


