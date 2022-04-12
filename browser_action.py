from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
# driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# browser action 1 >> Open Web
driver.get("https://google.com")
sleep(2)

# browser action 2 >> Title Web
#window_title = driver.title
#print(window_title)

# browser action 3 >> Back Web
#driver.get("http://wikipedia.com")
#sleep(2)
#driver.back()
#sleep(2)
#browser action 4 >> forward
#driver.forward()
#sleep(2)
# browser action 4 >> refresh
#driver.refresh()
#sleep(2)

# browser action 5>> Open The window and switch to it(tab)
# driver.switch_to.new_window('tab')
#sleep(2)
# browser action 5>> Open The window and switch to it(window)
#driver.switch_to.new_window('window')
#sleep(2)
#driver.get('https://yahoo.com')
#sleep(1)
# browser action 6>> Current Window
#yahoo_window = driver.current_window_handle
# browser action 7>> All Handle
#all_handle = driver.window_handles
#print('all_handle' + str(all_handle))
# browser action 8 >> switch
#driver.switch_to.window(all_handle[0])
#sleep(1)

# browser action 9 >> Close Tab
#driver.close()
#sleep(1)
# browser action 10 >> Window_size
#window_size = driver.get_window_size()
# browser action 11 >> Set Window Size
driver.set_window_size(800,600)
sleep(2)
size = driver.get_window_size()
assert size['width']==800
#  browser action 11 >> get window postion
get_position = driver.get_window_position()
print(get_position)
#  browser action 11 >> set window postion
driver.set_window_position(400,500)
sleep(2)
assert driver.set_window_position(400,500)['x']==400
get = driver.get_window_position()
print(get)
driver.quit()
