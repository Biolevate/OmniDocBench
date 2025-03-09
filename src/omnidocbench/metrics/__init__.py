# from .cal_metric import call_TEDS, call_BLEU, call_METEOR, call_Edit_dist, call_CDM, call_Move_dist
from omnidocbench.registry.registry import METRIC_REGISTRY

from .cal_metric import (
    call_BLEU,
    call_CDM,
    call_Edit_dist,
    call_METEOR,
    call_TEDS,
)

__all__ = [
    "call_TEDS",
    "call_BLEU",
    "call_METEOR",
    "call_Edit_dist",
    "call_CDM",
]
