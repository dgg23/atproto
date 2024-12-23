##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2024 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


import typing as t

from atproto_client.models import base, string_formats


class Data(base.DataModelBase):
    """Input data model for :obj:`app.bsky.graph.unmuteThread`."""

    root: string_formats.AtUri  #: Root.


class DataDict(t.TypedDict):
    root: string_formats.AtUri  #: Root.
