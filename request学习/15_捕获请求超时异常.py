"""
Timeout表示请求超时异常，通常是由于网络延迟、服务器响应慢或请求超时设置过短等原因导致的。

可以使用try-except语句来捕获Timeout异常，从而处理请求超时的情况。
"""
import requests
from requests.exceptions import Timeout

try:
    # 发送一个请求，设置超时时间为1秒
    response = requests.get('https://httpbin.org/delay/3', timeout=1)
    print(response.text)
    print("请求成功，状态码:", response.status_code)
except Timeout as timeout_err:
    print(f"请求超时发生: {timeout_err}")  # 捕获Timeout异常并打印错误信息