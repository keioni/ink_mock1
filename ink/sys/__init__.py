# -*- coding: utf-8 -*-

import os
import json

from attrdict import AttrDict


conf = AttrDict()

conf_file = os.environ.get('INK_CONF_FILE')
if conf_file:
    with open(conf_file, 'r') as f:
        raw_conf = json.load(f)
    if raw_conf:
        conf_head = raw_conf.get('configurations')
        if conf_head:
            conf = AttrDict(conf_head)
        else:
            conf = AttrDict(raw_conf)
