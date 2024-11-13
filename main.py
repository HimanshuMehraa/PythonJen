from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver= webdriver.Chrome()

url= "https://news.ycombinator.com/news"

driver.get(url)
driver.maximize_window()
user_input = input("Enter the type for which you want the news to be extracted: ")
news= driver.find_element(By.XPATH,"//input[@name='q']")
news.send_keys(user_input)
news.send_keys(Keys.RETURN)
print(driver.title)


lis= driver.find_elements(By.CLASS_NAME,'Story_title')
print(len(lis))

for story in lis:
    title = story.find_element(By.TAG_NAME, 'a').text
    print(title)

input()
