from selenium import webdriver


url = "https://www.saucedemo.com"
driver = webdriver.Chrome()  
driver.get(url)


title = driver.title
current_url = driver.current_url


page_source = driver.page_source


print("Title:", title)
print("Current URL:", current_url)
print("Page Contents:", page_source)


driver.quit()
