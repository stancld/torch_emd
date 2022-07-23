# Copyright Dan Stancl.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from typing import TYPE_CHECKING

import torch

if TYPE_CHECKING:
    from torchtyping import TensorType


def network_simplex_algorith(network_graph: TensorType["source_dim", "target_dim", torch.float64]):
    pass


def earth_movers_distance(
    source_histogram: TensorType["source_dim", torch.float64],
    target_histogram: TensorType["target_dim", torch.float64],
    cost_matrix: TensorType["source_dim", "target_dim", torch.float64],
    max_iterations: int = 100000,
    center_dual: bool = True,
) -> TensorType["source_dim", "target_dim", torch.float64]:
    """Solve the Earth Mover's Distance problem using Network Simplex simple algorithm.

    Args:
        source_histogram:
        target_histogram:
        cost_matrix:
        max_iterations:
        center_dual:

    Return:
        Optimal transportation matrix

    Example:

    References:
    [1] Bonneel, N., Van De Panne, M., Paris, S., & Heidrich, W. (2011, December).  Displacement interpolation using
    Lagrangian mass transport. In ACM Transactions on Graphics (TOG) (Vol. 30, No. 6, p. 158). ACM.
    """
    if source_histogram.device != target_histogram.device:
        raise RuntimeError(
            "`source_histogram` and `target_histogram` tensors are expected to be placed on the same device. "
            f"But got {source_histogram.device} and {target_histogram.device}"
        )
    if source_histogram.shape[0] != cost_matrix.shape[0]:
        raise ValueError
    if target_histogram.shape[0] != cost_matrix.shape[1]:
        raise ValueError

    target_histogram *= source_histogram.sum() * target_histogram.sum()

    ## emd_wrap - network simplex simple
