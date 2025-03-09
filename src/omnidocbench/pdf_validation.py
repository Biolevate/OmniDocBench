# coding: utf-8
import argparse
import io
import os
import pathlib

import yaml

import omnidocbench.dataset
import omnidocbench.metrics
import omnidocbench.task
from omnidocbench.registry.registry import DATASET_REGISTRY, EVAL_TASK_REGISTRY


def process_args(args):
    parser = argparse.ArgumentParser(
        description="Render latex formulas for comparison."
    )
    parser.add_argument("--config", "-c", type=str, default="./configs/end2end.yaml")
    parameters = parser.parse_args(args)
    return parameters


def pdf_validation(config_path: str):
    if isinstance(config_path, (str, pathlib.Path)):
        with io.open(os.path.abspath(config_path), "r", encoding="utf-8") as f:
            cfg = yaml.load(f, Loader=yaml.FullLoader)
    else:
        raise TypeError("Unexpected file type")

    if cfg is not None and not isinstance(cfg, (list, dict, str)):
        raise IOError(  # pragma: no cover
            f"Invalid loaded object type: {type(cfg).__name__}"
        )

    for task_var in cfg.keys():
        if not cfg.get(task_var):
            print(f"No config for task {task_var}")
        dataset_var = cfg[task_var]["dataset"]["dataset_name"]
        # metrics_list = [METRIC_REGISTRY.get(i) for i in cfg[task]['metrics']] # TODO: 直接在主函数里实例化
        metrics_list = cfg[task_var]["metrics"]  # 在task里再实例化
        val_dataset = DATASET_REGISTRY.get(dataset_var)(cfg[task_var])
        val_task = EVAL_TASK_REGISTRY.get(task_var)
        # val_task(val_dataset, metrics_list)
        if cfg[task_var]["dataset"]["prediction"].get("data_path"):
            save_name = (
                os.path.basename(cfg[task_var]["dataset"]["prediction"]["data_path"])
                + "_"
                + cfg[task_var]["dataset"].get("match_method", "quick_match")
            )
        else:
            save_name = os.path.basename(
                cfg[task_var]["dataset"]["ground_truth"]["data_path"]
            ).split(".")[0]
        print("###### Process: ", save_name)
        if cfg[task_var]["dataset"]["ground_truth"].get("page_info"):
            val_task(
                val_dataset,
                metrics_list,
                cfg[task_var]["dataset"]["ground_truth"]["page_info"],
                save_name,
            )  # 按页面区分
        else:
            val_task(
                val_dataset,
                metrics_list,
                cfg[task_var]["dataset"]["ground_truth"]["data_path"],
                save_name,
            )  # 按页面区分


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="PDF Validation Script")
    parser.add_argument(
        "--config", type=str, required=True, help="Path to the configuration file"
    )
    args = parser.parse_args()

    pdf_validation(args.config)
