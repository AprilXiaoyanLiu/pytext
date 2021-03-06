#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

import torch

from .representation_base import RepresentationBase


class PassThroughRepresentation(RepresentationBase):
    def __init__(
        self, config: RepresentationBase.Config, input_module_dim: int
    ) -> None:
        super().__init__(config)
        self.representation_dim = input_module_dim

    def forward(self, embedded_tokens: torch.Tensor, *args) -> torch.Tensor:
        return embedded_tokens
