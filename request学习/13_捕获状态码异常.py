"""
HTTPError表示HTTP错误状态码(4xx, 5xx)异常，通常是由于请求的资源不存在、权限不足或服务器内部错误等原因导致的。
可以使用响应对象的.raise_for_status()方法来检查响应状态码，如果状态码表示错误，则会抛出HTTPError异常。
"""
import requests
from requests.exceptions import HTTPError

try:
    response = requests.get('https://httpbin.org/status/404')  # 请求一个不存在的资源
    response.raise_for_status()  # 检查响应状态码，如果是错误状态码则抛出HTTPError异常
    print("请求成功，状态码:", response.status_code)
except HTTPError as http_err:
    print(f"HTTP错误发生: {http_err}")  # 捕获HTTPError异常并打印错误信息