from selenium import webdriver
import time

browser = webdriver.Chrome('C:/Users/mubas/chromedriver/chromedriver')

browser.get('https://google.com')

time.sleep(2)

search_input = browser.find_element_by_name('q')
search_input.send_keys('Discord sucks')

time.sleep(2)

search_btn = browser.find_element_by_css_selector('input[type="submit"]')
search_btn.click()

'''
<input class="gLFyf gsfi" jsaction="paste:puy29d;" maxlength="2048" name="q" type="text" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="Search" value="" aria-label="Search" data-ved="0ahUKEwjX5POe-MHyAhXvrZUCHT3lACcQ39UDCAQ">
<input class="gNO89b" value="Google Search" aria-label="Google Search" name="btnK" type="submit" data-ved="0ahUKEwjmje2R-cHyAhWBI7kGHbhdA6oQ4dUDCAs">
'''
