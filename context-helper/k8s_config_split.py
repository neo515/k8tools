#!/bin/env python3
# coding:  utf8

# 拆分config中每个context为独立的文件
# 如果想将某个集群的链接权限给别人，这个或许可以快速搞定这个需求。

# import pprint
import yaml
# import json
import os

yaml_file=os.path.join(os.path.expanduser('~'),'.kube/config')

yaml_f=open(yaml_file)
configs=yaml.load(yaml_f,Loader=yaml.FullLoader)

# output_dir=os.path.join(os.path.expanduser('~'),'.kube/split')
output_dir="split"

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# config={'apiVersion': 'v1', 'kind': 'Config', 'preferences': {}, 'clusters': [], 'contexts': [], 'users': []}

for context in configs["contexts"]:
    config={'apiVersion': 'v1', 'kind': 'Config', 'preferences': {}, 'clusters': [], 'contexts': [], 'users': []}
    context_name=context["name"]
    context_cluster_name=context["context"]["cluster"]
    context_user_name=context["context"]["user"]

    config['contexts'].append(context)

    for user in configs["users"]:
        if user["name"]==context_user_name:
            config['users'].append(user)
            break

    for cluster in configs["clusters"]:
        if cluster["name"]==context_cluster_name:
            config['clusters'].append(cluster)
            break


    config_new=os.path.join(output_dir,context_name)
    with open(config_new,'w') as f:
        yaml.dump(config,f)

