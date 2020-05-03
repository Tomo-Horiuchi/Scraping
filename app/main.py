from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium import webdriver
import chromedriver_binary

 


#def job():
driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)#指定したdriverに対して最大で10秒間待機する
URL = "https://db.netkeiba.com/?pid=race_search_detail"
driver.get(URL)
wait.until(EC.presence_of_all_elements_located)#すべての要素が表示されるまで待ち先ほど指定
search_e = driver.find_element_by_class_name("search_detail_submit")
search_p_e = search_e.find_element_by_tag_name("p")
text = search_p_e.text#要素のなかのテキストを取得します
file_w = open('test.txt', 'w')
file_w.write(text)