from playwright.sync_api import sync_playwright
import re
p = sync_playwright().start()

browser = p.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://www.byhy.net/cdn2/files/selenium/stock1.html")

# 根据文本内容选择所有元素
elements = page.get_by_text(re.compile("^600")).all()
# 打印出元素文本
for ele in elements:
    print(ele.inner_text())