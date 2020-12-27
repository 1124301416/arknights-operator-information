import time
from PIL import Image

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def operator_update(name):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    URL = 'http://prts.wiki/w/' + name

    driver.get(URL)
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
    driver.set_window_size(1300, S('Height'))  # May need manual adjustment
    time.sleep(5)
    driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')

    driver.quit()

    im = Image.open(r"web_screenshot.png")
    box = (200, 550, 1220, im.tile[0][1][3] - 2000)

    crop = im.crop(box)
    crop.load()
    crop.save(name + ".png", 'png')

    # f = open("/Users/luke/Desktop/keyword_answer.txt", "a+")
    # f.write(name + 'b->' + name + ".png\n")


operator_update('莫斯提马')
