from selenium import webdriver

# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# binary = FirefoxBinary('~PycarhmProjects/ecommerce_istebu/app/')
# http://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path

browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')

assert 'İştebu!' in browser.title

