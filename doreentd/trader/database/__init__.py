import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from doreentd.trader.database.database import BaseDatabaseManager

if "VNPY_TESTING" not in os.environ:
    from doreentd.trader.setting import get_settings
    from .initialize import init

    settings = get_settings("database.")
    database_manager: "BaseDatabaseManager" = init(settings=settings)
