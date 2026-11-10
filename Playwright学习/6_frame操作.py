from playwright.sync_api import sync_playwright
p = sync_playwright().start()

browser = p.chromium.launch(headless=False)
page = browser.new_page()

page.goto("https://www.byhy.net/cdn2/files/selenium/sample2.html")

# 产生一个  FrameLocator 对象
frame = page.frame_locator("iframe[src='sample1.html']")

# 再在其内部进行定位
lcs = frame.locator('.animal').all()
for lc in lcs:
    print(lc.inner_text(timeout=1000))