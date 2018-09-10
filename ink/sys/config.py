# -*- coding: utf-8 -*-

import json
from attrdict import AttrDict


conf = AttrDict()

def load_conf(filename: str):
    with open(filename, 'r') as f:
        raw_conf = json.load(f)
    global conf
    conf = AttrDict(raw_conf['configurations'])
    return conf
