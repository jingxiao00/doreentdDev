from pathlib import Path

from doreentd.trader.app import BaseApp
from doreentd.trader.constant import Direction
from doreentd.trader.object import TickData, BarData, TradeData, OrderData
from doreentd.trader.utility import BarGenerator, ArrayManager

from .base import APP_NAME
from .engine import CtaEngine
from .template import CtaTemplate, CtaSignal, TargetPosTemplate


class CtaStrategyApp(BaseApp):
    """"""

    app_name = APP_NAME
    app_module = __module__
    app_path = Path(__file__).parent
    display_name = "CTA策略"
    engine_class = CtaEngine
    widget_name = "CtaManager"
    icon_name = "cta.ico"
