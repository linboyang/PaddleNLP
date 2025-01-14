# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
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
# flake8: noqa
from pipelines.nodes.retriever.base import BaseRetriever
from pipelines.nodes.retriever.dense import DensePassageRetriever
from pipelines.nodes.retriever.multimodal_retriever import MultiModalRetriever
from pipelines.nodes.retriever.parallel_retriever import ParallelRetriever
from pipelines.nodes.retriever.sparse import BM25Retriever
from pipelines.nodes.retriever.web import WebRetriever
