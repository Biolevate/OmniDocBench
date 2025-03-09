from omnidocbench.registry.registry import DATASET_REGISTRY

from .detection_dataset import DetectionDataset
from .end2end_dataset import End2EndDataset
from .md2md_dataset import Md2MdDataset
from .recog_dataset import RecognitionTextDataset

__all__ = [
    "End2EndDataset",
    "DetectionDataset",
    "Md2MdDataset",
    "RecognitionTextDataset",
]
