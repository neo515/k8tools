#!/bin/env python3
# coding:  utf8

# 转换k8s的context文件
# config  --> json (有改写)

import pprint
import yaml
import json
import os

yaml_file=os.path.join(os.path.expanduser('~'),'.kube/config')

yaml_f=open(yaml_file)
configs=yaml.load(yaml_f,Loader=yaml.FullLoader)

clusters=configs['clusters']
contexts=configs['contexts']
users=configs['users']

contexts_new=[]
for context in contexts:
    c={}
    c["name"]=context["name"]
    c["cluster"]={}
    c["user"]={}
    context_cluster_name=context["context"]["cluster"]
    context_user_name=context["context"]["user"]
    for cluster in clusters:
        if cluster["name"] == context_cluster_name:
            c["cluster"].update(cluster["cluster"])
            c["cluster"]["name"]=cluster["name"]
            # print(cluster)
            break
    for user in users:
        if user["name"] == context_user_name:
            c["user"].update(user["user"])
            c["user"]["name"]=user["name"]
            break
    contexts_new.append(c)

# pprint.pprint(contexts_new,indent=4)
print(json.dumps(contexts_new,indent=4))

# output=os.path.join(os.path.expanduser('~'),'.kube/config.json')
# with open(output,'w') as f:
#     json.dump(contexts_new,f,indent=4)
