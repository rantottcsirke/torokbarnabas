from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "http://hotel-v3.progmasters.hu/"

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get(URL)

wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Hotel"))).click()
time.sleep(2)

checkboxes = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='checkbox']")))
for box in checkboxes:
    if not box.is_selected():
        box.click()

driver.find_element(By.XPATH, "//button[contains(text(),'Szoba szolgáltatás szűrések törlése')]").click()
time.sleep(1)

for box in checkboxes:
    assert not box.is_selected()

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".hotel-card a"))).click()
time.sleep(2)

desc = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".long-description"))).text
assert len(desc) > 500

wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Bejelentkez"))).click()
wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("tesztuser")
driver.find_element(By.NAME, "password").send_keys("tesztjelszo")
driver.find_element(By.XPATH, "//button[contains(text(),'Bejelentkezés')]").click()
time.sleep(2)

assert driver.find_element(By.PARTIAL_LINK_TEXT, "Kilépés")
driver.quit()