from time import sleep
import pyautogui

def Follow(driver):
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]')\
        .click()
        sleep(2)
        scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div")
        scroll()
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        print(names)
        # close button
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")\
            .click()
        return names

def scroll():
    x, y = pyautogui.size()
    pyautogui.moveTo(x/2, y/2)
    for i in range(0, 10):
        pyautogui.scroll(-1000)
        sleep(0.1)
        print(i)