
from selenium import webdriver          # import selenium module

driver = webdriver.Chrome()     # Initialise chrome driver
#driver = webdriver.Chrome(executable_path="C:/Users/sss2327/AppData/Local/Programs/Python/Python39/chromedriver.exe")

driver.get("https://www.facebook.com/")     ## Open Url/website

print("Page title : ", driver.title)
print("Page Current URL : ", driver.current_url)
driver.get("https://www.amazon.com/")
print("Page title : ", driver.title)
print("Page Current URL : ", driver.current_url)

driver.close()      # Close current window
driver.quit()       # Quits all windows opened by your driver



###----------------------------------------------------------------------

### For latest version
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# s=Service('C:/Users/Morteza/Documents/Dev/chromedriver.exe')
# browser = webdriver.Chrome(service=s)
# url='https://www.google.com'
# browser.get(url)