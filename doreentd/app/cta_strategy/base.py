"""
Defines constants and objects used in CtaStrategy App.
"""

from dataclasses import dataclass, field
from enum import Enum
from datetime import timedelta

from doreentd.trader.constant import Direction, Offset, Interval
from doreentd.trader.object import OrderData
from doreentd.trader.object import OrderType

APP_NAME = "CtaStrategy"


class EngineType(Enum):
    LIVE = "实盘"
    BACKTESTING = "回测"


class BacktestingMode(Enum):
    BAR = 1
    TICK = 2


@dataclass
class LimitOrder(OrderData):
    type: OrderType = OrderType.LIMIT
    
@dataclass
class StopOrder(OrderData):
    type: OrderType = OrderType.STOP



EVENT_CTA_LOG = "eCtaLog"
EVENT_CTA_STRATEGY = "eCtaStrategy"

INTERVAL_DELTA_MAP = {
    Interval.MINUTE: timedelta(minutes=1),
    Interval.HOUR: timedelta(hours=1),
    Interval.DAILY: timedelta(days=1),
}
