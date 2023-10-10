from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select
product_names=[]
product_prices=[]
product_ratings=[]
driver=webdriver.Chrome()
driver.get("http://www.google.com")
driver.maximize_window()
driver.implicitly_wait(10)
#Google Search
driver.find_element(By.ID, "APjFqb").send_keys("amazon")
driver.find_element(By.NAME, "btnK").click()
#Amazon
driver.find_element(By.CLASS_NAME, "VuuXrf").click()

dropdown = Select(driver.find_element(By.ID, "searchDropdownBox"))
dropdown.select_by_visible_text("Electronics")
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Dell Laptop")
driver.find_element(By.ID, "nav-search-submit-button").click()
driver.find_element(By.ID, "low-price").send_keys("30000")
driver.find_element(By.ID, "high-price").send_keys("50000")
driver.find_element(By.CLASS_NAME, "a-button-input").click()

no_of_pages=driver.find_element(By.XPATH, "//*[@class='s-pagination-item s-pagination-disabled']").text
print(no_of_pages)

Productlist = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
for product in Productlist:
    #Name
    products = product.find_elements(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']")
    for pro in products:
        product_names.append(pro.text)
    #Price
    prices = product.find_elements(By.XPATH, ".//span[@class='a-price-whole']")
    for price in prices:
        product_prices.append(price.text)
    #Rating
    try:
        ratings = product.find_elements(By.XPATH, ".//div[@class='a-row a-size-small']/span[1]")
        if len(ratings) > 0:
            for rating in ratings:
                product_ratings.append(rating.text)
        else:
            product_ratings.append("0")
    except:
        pass

driver.quit()


for name, price, rate in zip(product_names, product_prices, product_ratings):
    print(name, price, rate)

