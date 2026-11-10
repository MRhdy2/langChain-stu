from playwright.sync_api import sync_playwright
pw = sync_playwright().start()
browser = pw.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://www.byhy.net/cdn2/files/selenium/test4.html")


def handleDlg(dialog):
    page.wait_for_timeout(1000)
    dialog.accept('你好啊') # 输入信息，并确定

page.on("dialog", handleDlg)

# 点击 confirm 按钮
page.locator('#b3').click()

input('....')
browser.close()
pw.stop()