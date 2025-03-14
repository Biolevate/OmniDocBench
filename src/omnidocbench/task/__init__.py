from omnidocbench.registry.registry import EVAL_TASK_REGISTRY

from .detection_eval import DetectionEval
from .end2end_run_eval import End2EndEval
from .recognition_eval import RecognitionBaseEval

__all__ = ["RecognitionBaseEval", "DetectionEval", "End2EndEval"]

print("EVAL_TASK_REGISTRY: ", EVAL_TASK_REGISTRY.list_items())
