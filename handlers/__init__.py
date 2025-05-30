from aiogram import Router

from .generals import router as general_router
from .callbacks import router as callback_router
from .text import router as text_router

router = Router()

router.include_routers(general_router, callback_router, text_router)


