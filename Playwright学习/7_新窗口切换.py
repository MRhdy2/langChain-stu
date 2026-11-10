from playwright.sync_api import sync_playwright
pw = sync_playwright().start()

browser = pw.chromium.launch(headless=False)

# 创建 BrowserContext 对象
context = browser.new_context()

# 通过context 创建page
page = context.new_page()

page.goto("https://www.byhy.net/cdn2/files/selenium/sample3.html")

# 点击链接，打开新窗口
page.locator("a").click()

# 等待2秒， 不能用 time.sleep
page.wait_for_timeout(2000)

# pages属性是 所有窗口对应Page对象的列表
newPage = context.pages[1]
oldPage = context.pages[0]
# 打印新网页窗口标题
print(newPage.title())
# 将新网页窗口置顶
newPage.bring_to_front()
# 进行新网页截图
newPage.screenshot(path="newPage.png")
# 打印老网页窗口标题
print(oldPage.title())
# 进行老网页截图
oldPage.screenshot(path="oldPage.png")