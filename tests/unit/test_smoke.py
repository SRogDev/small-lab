"""CPU smoke tests: the package imports and PyTorch works on CPU.

Deliberately minimal. These tests verify the environment, not a model:
no neural architecture is implemented to satisfy them.
"""

import torch

import small_lab


def test_package_imports_and_reports_version() -> None:
    assert small_lab.__version__ == "0.1.0"


def test_minimal_tensor_operation_on_cpu() -> None:
    x = torch.tensor([1.0, 2.0, 3.0])
    y = torch.tensor([4.0, 5.0, 6.0])
    assert torch.equal(x + y, torch.tensor([5.0, 7.0, 9.0]))
    assert x.device.type == "cpu"


def test_torch_is_available() -> None:
    assert torch.__version__
