from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_forex_rate(date, currency_code):
    driver_path = "path/to/chromedriver"
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get("https://www.boc.cn/sourcedb/whpj/")

    # 定位日期和货币输入框，并输入相应的值
    date_input = driver.find_element("id", "your_date_input_id")
    date_input.clear()
    date_input.send_keys(date)

    currency_input = driver.find_element("id", "your_currency_input_id")
    currency_input.clear()
    currency_input.send_keys(currency_code)

    # 模拟键盘输入回车
    currency_input.send_keys(Keys.RETURN)

    # 通过selenium定位到“现汇卖出价”的元素，并获取值
    forex_rate = driver.find_element("your_locator_for_forex_rate").text

    # 将结果写入result.txt文件
    with open("result.txt", "w") as result_file:
        result_file.write(f"Date: {date}, Currency Code: {currency_code}, Forex Rate: {forex_rate}")

    # 关闭浏览器
    driver.quit()

# 示例调用
get_forex_rate("20211231", "USD")
