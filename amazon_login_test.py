import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginText(unittest.TestCase):
    def setUp(self):     
        options = webdriver.ChromeOptions()
        
        # 關閉瀏覽器左上角通知提示
        prefs = {
            'profile.default_content_setting_values':
            {
                'notifications': 2
            }
        }
        options.add_experimental_option('prefs', prefs)  
        # 關閉'chrome目前受到自動測試軟體控制'的提示
        options.add_experimental_option('useAutomationExtension', False) 
        options.add_experimental_option('excludeSwitches', ['enable-automation'])

        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.maximize_window() 
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.amazon.com/")
    
    #@unittest.skip("skip test_invalid_login")
    def test_invalid_login(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "nav-link-accountList")))
            self.driver.find_element_by_id("nav-link-accountList").click()
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "ap_email")))
            self.driver.find_element_by_id("ap_email").send_keys("fakeaccount")
            self.driver.find_element_by_id("continue").click()
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "auth-error-message-box")))
            self.assertTrue(True)
        except:
            self.assertTrue(False, msg = "Wait Overtime")
            
            
    #@unittest.skip("skip test_valid_login")
    def test_valid_login(self):
        valid_email = "valid_email"
        valid_pwd = "valid_pwd"
        try:            
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "nav-link-accountList")))
            self.driver.find_element_by_id("nav-link-accountList").click()
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "ap_email")))
            self.driver.find_element_by_id("ap_email").send_keys(valid_email)
            self.driver.find_element_by_id("continue").click()
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "ap_password")))
            self.driver.find_element_by_id("ap_password").send_keys(valid_pwd)
            self.driver.find_element_by_id("signInSubmit").click()
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
            self.assertTrue(True)
        except:
            self.assertTrue(False, msg = "Wait Overtime")

    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main() 