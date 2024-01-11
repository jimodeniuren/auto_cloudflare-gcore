# 导入requests库，用于发送http请求
import requests



# 定义接口的地址
url = "https://monitor.gacjie.cn/api/ajax/get_gcore_v4"
url2 = "https://monitor.gacjie.cn/api/ajax/get_cloud_flare_v4"
# 发送get请求，获取响应
response = requests.get(url)

address_list = []
# 判断响应的状态码是否为200，表示成功
if response.status_code == 200:
    # 解析响应的内容，转换为python字典
    data = response.json()
    # 创建一个空列表，用于存储address的值
    # 遍历data中的data键对应的列表
    for item in data["data"]:
        # 获取每个item中的address键对应的值
        address = item["address"]
        # 把address的值添加到列表中
        address_list.append(address)

response = requests.get(url2)

address_list2 = []
# 判断响应的状态码是否为200，表示成功
if response.status_code == 200:
    # 解析响应的内容，转换为python字典
    data = response.json()
    # 创建一个空列表，用于存储address的值
    # 遍历data中的data键对应的列表
    for item in data["data"]:
        # 获取每个item中的address键对应的值
        address = item["address"]
        # 把address的值添加到列表中
        address_list2.append(address)


# 导入json和base64模块
import json
import base64

# 定义add数组

# 定义json对象
json_obj = {
  "v": "2",
  "ps": "",
  "add": "",
  "port": "80",
  "id": "",
  "aid": "0",
  "scy": "auto",
  "net": "ws",
  "type": "none",
  "host": "",
  "path": "/ws?ed=2048",
  "tls": "none",
  "sni": "",
  "alpn": ""
}

# 定义一个空的list
new_list = []
new_list.append("")
i = 1
# 依次遍历add数组
fff = json_obj["ps"]
for a in address_list:
  # 用其中的元素替换json对象中的add
  json_obj["ps"] = fff + str(i)
  json_obj["add"] = a
  # 把得到的新json转换为字符串
  json_str = json.dumps(json_obj)
  # 用base64加密
  json_b64 = base64.b64encode(json_str.encode())
  # 在前面添加vmess://
  new_str = "vmess://" + json_b64.decode()
  # 把得到的新字符串保存到list中
  new_list.append(new_str)

  i+=1
i = 1
# 依次遍历add数组
for a in address_list2:
  # 用其中的元素替换json对象中的add
  json_obj["ps"] = "" + str(i)
  json_obj["add"] = a
  json_obj["port"] = "8080"
  json_obj["host"] = ""
  # 把得到的新json转换为字符串
  json_str = json.dumps(json_obj)
  # 用base64加密
  json_b64 = base64.b64encode(json_str.encode())
  # 在前面添加vmess://
  new_str = "vmess://" + json_b64.decode()
  # 把得到的新字符串保存到list中
  new_list.append(new_str)

  i+=1
full_list = ""
# 打印list中的内容
for s in new_list:
  full_list += s + "\n"
full_list = str(base64.b64encode(full_list.encode())).strip().split("'")[1]
# print(full_list)

with open("index.html", "w") as f:
        f.write(full_list)


