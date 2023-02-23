#!/bin/env python3
# coding:  utf8

# 将 formatted_config.json转回为config

import yaml
import json
import os.path
import pprint

config={'apiVersion': 'v1', 'kind': 'Config', 'preferences': {}, 'clusters': [], 'contexts': [], 'users': []}

config_json=os.path.join(os.path.expanduser('~'),'.kube/formatted_config.json')
# config_new =os.path.join(os.path.expanduser('~'),'.kube/config.new')
config_new = "config"


config_json_f=open(config_json)
contexts=json.load(config_json_f)

for context in contexts:
    context_name=context["name"]

    context_cluster=context["cluster"]
    context_cluster_name=context_cluster["name"]
    context_cluster.pop("name")

    context_user=context["user"]
    context_user_name=context_user["name"]
    context_user.pop("name")

    cluster={"cluster":context_cluster,"name":context_cluster_name}
    config["clusters"].append(cluster)

    # user
    user={"user":context_user,"name":context_user_name}
    config["users"].append(user)

    # context
    _context={"context":{"cluster":context_cluster_name,"user":context_user_name},"name":context_name}
    config["contexts"].append(_context)

with open(config_new,'w') as f:
    yaml.dump(config,f)

