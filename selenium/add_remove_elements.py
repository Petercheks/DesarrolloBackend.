import unittest
from selenium import webdriver
from time import sleep


class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Pedro\Desktop\DesarrolloBackend\selenium\chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/')

    def test_add_remove(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="content"]/ul/li[2]/a').click()

        elements_added = int(input('Cuantos quieres agregar?: '))
        elements_removed = int(input('Cuantos quieres eliminar?: '))
        total_elements = elements_added - elements_removed

        add = driver.find_element_by_xpath('//*[@id="content"]/div/button')
        for i in range(elements_added):
            add.click()
            sleep(1)

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button[1]')
                delete_button.click()
            except:
                print('Quieres eliminar mas elementos de los que existen!')
                break
        
        if total_elements > 0:
            print(f'Hay {total_elements} elementos en pantalla.')
        else:
            print('Hay 0 elementos en pantalla.')


        sleep(5)
                
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity = 2)