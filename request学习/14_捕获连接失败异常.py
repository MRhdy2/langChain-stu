"""
ConnectionError表示连接失败异常，通常是由于网络问题、服务器不可达或请求超时等原因导致的。

可以使用try-except语句来捕获ConnectionError异常，从而处理连接失败的情况。
"""
import requests
from requests.exceptions import ConnectionError

try:
    response = requests.get('https://example.com')
    response.raise_for_status()  # 检查请求是否成功
    print(response.text)
    print("请求成功！,执行后续操作")

except ConnectionError as conn_err:
    print(f"连接错误发生: {conn_err}")  # 捕获ConnectionError异常并打印错误信息