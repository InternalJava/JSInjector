from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

browser_type_list = ["Chrome", "Firefox"]
user_agent =  ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
'AppleWebKit/537.36 (KHTML, like Gecko) '
'Chrome/39.0.2171.95 Safari/537.36')

class JS():
    def Inject(browser_type : str, website : str, script : str):
        try:
            if browser_type in browser_type_list:
                if browser_type == browser_type_list[0]:
                    chrome_options = Options()
                    chrome_options.add_argument(f'user-agent={user_agent}')
                    chrome_options.add_experimental_option("detach", True)
                    driver = webdriver.Chrome(options=chrome_options)
                if browser_type == browser_type_list[1]:
                    firefox_options = Options()
                    firefox_options.add_argument(f'user-agent={user_agent}')
                    firefox_options.add_experimental_option("detach", True)
                    driver = webdriver.Firefox(options=firefox_options)
                driver.implicitly_wait(0.5)
                driver.get(website)
                driver.execute_script(script)
                return "Script '{0}' succesfully injected into: {1}".format(script, website)
        except:
            return "Failed to inject script '{0}' into: {1}".format(script, website)
