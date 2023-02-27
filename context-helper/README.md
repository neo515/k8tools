# k8tools
## 一、说明
k8s_config2json.py   #将config文件输出为json格式，并重新格式化每个context的输出格式便于阅读。

k8s_json2config.py   #将k8s_config2json.py输出的json文件转回config文件。一般结合k8s_config2json.py一起使用。

k8s_config_split.py   #拆分config中的每一个context为独立的“config” context文件。

### 1. k8s_config2json.py

> 默认情况下，config文件内容可读性并不好。该脚本将重新”整理“输出为json，输出格式如下。
>
> 脚本使用方法： python3 k8s_config2json.py > formatted_config.json

```json
{
    // 每个context独立输出
    // CN-Prod-01-admin context
    {
        "name": "CN-Prod-01-admin",
        "cluster": {
            "certificate-authority-data": "******",
            "server": "https://CN-Prod-01.privatelink.southeastasia.azmk8s.io:443",
            "name": "CN-Prod-01"
        },
        "user": {
            "client-certificate-data": "******",
            "client-key-data": "******",
            "token": "******",
            "name": "clusterAdmin_AZ-RG-CS-K8s-CNPlatform-PaaS-AP-01_CN-Prod-01"
        }
    },
    // CN-Prod-02-admin context
    {
        "name": "CN-Prod-02-admin",
        "cluster": {
            "certificate-authority-data": "******",
            "server": "https://CN-Prod-01.privatelink.southeastasia.azmk8s.io:443",
            "name": "CN-Prod-01"
        },
        "user": {
            "client-certificate-data": "******",
            "client-key-data": "******",
            "token": "******",
            "name": "clusterAdmin_AZ-RG-CS-K8s-CNPlatform-PaaS-AP-01_CN-Prod-01"
        }
    },
    ...
}
```

### 2. k8s_json2config.py

> 根据需要修改formatted_config.json后，重新转回config

### 3. k8s_config_split.py

> 拆分config文件为独立的context


## 二、best practice

```shell
# 
1. git clone git@github.com:neo515/k8tools.git
2. cd k8stools; python3 k8s_config2json.py > formatted_config.json
3. 调整formatted_config.json
4. python3 k8s_json2config.py
```
