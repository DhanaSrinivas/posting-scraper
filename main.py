from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tabulate import tabulate

driver = webdriver.Chrome()

# Navigating towards our link
driver.get(url="https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787")
time.sleep(1)

# Selecting the first row
button = driver.find_element(By.CSS_SELECTOR,"tbody>tr>td>a")
button.click()

time.sleep(1)


data = []


# Getting hold of the values of desired fields for the first posting


est_val = driver.find_element(By.XPATH, '//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[3]/td[2]').text

desc = driver.find_element(By.XPATH, '//*[@id="current_project"]/div/div[3]/div/table/tbody/tr[3]/td[2]').text

date = driver.find_element(By.XPATH, '//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[1]/td[2]').text


data.append([est_val, desc, date])

# Getting hold of the values of desired fields for the other 4 postings
for i in range(4):
    # We are using the "next_button" to navigate from one posting to another
    next_button = driver.find_element(By.ID, "id_prevnext_next")
    next_button.click()

    time.sleep(1)

    e_val = driver.find_element(By.XPATH, '//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[3]/td[2]').text

    des = driver.find_element(By.XPATH, '//*[@id="current_project"]/div/div[3]/div/table/tbody/tr[3]/td[2]').text

    date1 = driver.find_element(By.XPATH, '//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[1]/td[2]').text

    data.append([e_val, des, date1])

driver.quit()

# The recorded data is well represented in the tabular form
headers = [" Est. Value Notes", "Description", "Closing Date"]
table = tabulate(data, headers=headers, tablefmt="fancy_grid")
print(table)

