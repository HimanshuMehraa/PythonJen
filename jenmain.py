import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Ensure a parameter is passed

if len(sys.argv) < 2:
    print("Usage: python script.py <search_query>")
    sys.exit(1)

user_input = sys.argv[1]  # Get the user input from command-line argument

driver = webdriver.Chrome()

url = "https://news.ycombinator.com/news"

driver.get(url)
driver.maximize_window()

# Print the title of the page
print(driver.title)

# Find the search box and send the input
news = driver.find_element(By.XPATH, "//input[@name='q']")
news.send_keys(user_input)
news.send_keys(Keys.RETURN)

# Wait for the results to load and then print the number of stories
lis = driver.find_elements(By.CLASS_NAME, 'Story_title')
print(len(lis))

# Print the titles of the stories
for story in lis:
    title = story.find_element(By.TAG_NAME, 'a').text
    print(title)

driver.quit()
