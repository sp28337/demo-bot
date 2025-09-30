from aiogram import Router

from .info_kb_callback_handler import router as info_kb_callback_router
from .action_kb_callback_handlers import router as actions_kb_callback_router

router = Router(name=__name__)

router.include_routers(
    info_kb_callback_router,
    actions_kb_callback_router,
)
