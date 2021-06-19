# Copyright (c) Facebook, Inc. and its affiliates.

import unittest
from unittest.mock import MagicMock, patch

import torch
from tests.trainers.test_training_loop import TrainerTrainingLoopMock
from tests.trainers.test_utils import get_config


class TestEvalLoop(unittest.TestCase):
    def setUp(self):
        torch.manual_seed(2)

    @patch(
        "mmf.common.test_reporter.PathManager",
        return_value=MagicMock(return_value=None),
    )
    @patch("mmf.common.test_reporter.get_mmf_env", return_value="")
    def test_eval_loop(self, a, b):
        config = get_config({"training": {"max_updates": 2, "max_epochs": 2}})
        trainer = TrainerTrainingLoopMock(num_train_data=100, config=config)
        trainer.load_datasets()
        combined_report, meter = trainer.evaluation_loop("val")
        self.assertAlmostEqual(combined_report["losses"]["loss"], 493377.5312)
        self.assertAlmostEqual(combined_report["logits"].item(), -0.2379742, 6)
