#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hashlib import blake2b # pylint: disable=E0611
from base64 import b64encode


def secure_hashing(value: str, salt: str) -> str:
    salt = salt.encode('utf-8')
    h = blake2b(key=salt, digest_size=32)
    h.update(value.encode('utf-8'))
    return b64encode(h.digest()).decode()
