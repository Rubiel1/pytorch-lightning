# Copyright The PyTorch Lightning team.
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
from typing import Any, Callable, Optional

from torchmetrics import MeanAbsoluteError as _MeanAbsoluteError

from pytorch_lightning.utilities.deprecation import deprecated


class MeanAbsoluteError(_MeanAbsoluteError):

    @deprecated(target=_MeanAbsoluteError, ver_deprecate="1.3.0", ver_remove="1.5.0")
    def __init__(
        self,
        compute_on_step: bool = True,
        dist_sync_on_step: bool = False,
        process_group: Optional[Any] = None,
        dist_sync_fn: Callable = None,
    ):
        """
        This implementation refers to :class:`~torchmetrics.MeanAbsoluteError`.

        .. deprecated::
            Use :class:`~torchmetrics.MeanAbsoluteError`. Will be removed in v1.5.0.
        """
