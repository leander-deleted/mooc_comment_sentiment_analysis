from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome('/home/npp/software/chromedriver', chrome_options=chrome_options,  service_args=['--verbose', '--log-path=/home/npp/software/chromedriver.log'])