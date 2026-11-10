from playwright.sync_api import sync_playwright

pw = sync_playwright().start()
browser = pw.chromium.launch(headless=False)

page = browser.new_page()
page.goto("https://www.byhy.net/cdn2/files/selenium/test4.html")

# 处理 弹出对话框 的 回调函数
def handleDlg(dialog):
    # 等待1秒
    page.wait_for_timeout(1000)
    # 点击确定
    dialog.accept()
    # 打印 弹出框 提示信息
    print(dialog.message)

# 设置弹出对话框事件回调函数
page.on("dialog", handleDlg )

# 点击 alert 按钮
page.locator('#b1').click()
# 关闭浏览器
browser.close()
# 停止 Playwright
pw.stop()