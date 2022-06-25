from time import sleep

from selene import config, browser
from selene.support.jquery_style_selectors import s

username = "tomaszA5"
password = "tomaszA5"

env = f"http://boardgamegeek.com/"
config.timeout = 5
config.start_maximized = True

browser.open_url(env)
s("[ggloginbutton]").click()
s("#inputUsername").type(username)
s("#inputPassword").type(password)
s("//button[normalize-space()='Sign In']").click()
sleep(10)