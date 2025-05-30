
from aiogram import types, Router, F


router = Router()


@router.callback_query(F.data == 'p1')
async def callback_p1(callback: types.CallbackQuery):
    await callback.message.answer('Пюрешка с котлеткой')
    await callback.answer()


@router.callback_query(F.data == 'p2')
async def callback_p2(callback: types.CallbackQuery):
    await callback.message.answer('Пюрешка с макарошками')
    await callback.answer()


@router.callback_query(F.data == 'p3')
async def callback_p3(callback: types.CallbackQuery):
    await callback.message.answer('Пюрешка с рисом')
    await callback.answer()


