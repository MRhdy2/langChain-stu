"""
1.在计算机网络中，代理（Proxy）是一种充当中间人的服务器，它在客户端和目标服务器之间起到转发和代理的作用。
当客户端发送请求时，代理服务器接收请求并将其转发给目标服务器。
然后，代理服务器接收来自目标服务器的响应，并将其转发回客户端。
2.在使用 requests 库发送 HTTP 请求时，代理（Proxy）可以用于访问被限制或无法直接访问的网站、隐藏真实的 IP 地址、实现访问控制等功能。
通过配置代理，请求将通过代理服务器，而不是直接与目标服务器通信。
这样，目标服务器会认为请求来自代理服务器，而不是真实的客户端。
"""
import requests

# 通过proxies参数全局代理
proxies = {
    'http': 'http://xxx.com:8080',
    'https': 'https://xxx.com:8080'
}# 设置代理服务器的地址和端口
response = requests.get('http://www.example.com', proxies=proxies)
print(response.text)

# 使用环境变量设置代理
import os
os.environ['HTTP_PROXY'] = 'http://xxx.com:8080'
os.environ['HTTPS_PROXY'] = 'https://xxx.com:8080'
response = requests.get('http://www.example.com')

# 环境变量中读取代理设置
proxy = "http://xxx.com:8080"
session = requests.Session()
session.proxies = {
    'http': proxy,
    'https': proxy
}
response = session.get('http://www.example.com')

proxies = {
    # 设置用户: 密码@ 地址 : 端口
    'http': 'http://user_name:password@xxx.com:8080',
    'https': 'https://user_name:password@xxx.com:8080'
}
response = requests.get('http://www.example.com', proxies=proxies)
