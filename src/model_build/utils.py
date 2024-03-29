import os

from sagemaker.estimator import Framework, Estimator
from typing import Dict, Optional


class ContainerEstimator(Framework):
    def __init__(
        self,
        entry_point,
        framework_version=None,
        py_version=None,
        source_dir=None,
        hyperparameters: Optional[Dict]=None,
        image_uri=None,
        distribution=None,
        **kwargs
    ):
        super(ContainerEstimator, self).__init__(
            entry_point, source_dir, hyperparameters, image_uri=image_uri, **kwargs
        )
        self.framework_version = framework_version
        self.py_version = None
        if hyperparameters:
            hyperparameters["tracking_uri"] = os.environ["MLFLOW_TRACKING_URI"]

    def _configure_distribution(self, distributions):
        return None

    def create_model(
        self,
        model_server_workers=None,
        role=None,
        vpc_config_override=None,
        entry_point=None,
        source_dir=None,
        dependencies=None,
        image_uri=None,
        **kwargs
    ):
        return None

