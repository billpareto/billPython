from time import sleep
import pygetwindow as gw
import pyautogui as pg
import win32api,win32con,win32process
import win32gui





all_windows =  gw.getAllWindows()

for window in all_windows:
    if "Microsoft\u200b Edge" in window.title:
        window.activate()
        break

sleep(10)
print(pg.position())
pg.click(x=pg.position().x,y=pg.position().y)


'''
ie_options = webdriver.IeOptions()

ie_options.attach_to_edge_chrome = True
#ie_options.edge_executable_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
#C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe

driver = webdriver.Ie(options=ie_options)

driver.switch_to.window(262166)


driver.get("http://eir.cmclink.com")

#elem = driver.find_element(By.ID, 'tttteeeexxxxtttt1')
#elem.send_keys("billdong"+Keys.TAB )
#elem = driver.find_element(By.ID, 'tttteeeexxxxtttt2')
#elem.send_keys("Szedi83484082" + Keys.TAB)


#只好调用JavaScript代码
js = """document.getElementById("tttteeeexxxxtttt1").value = "billdong"\n
document.getElementById("tttteeeexxxxtttt2").value = "Szedi83484082"\n
document.getElementById("TextBoxValidateCode").focus()"""
driver.execute_script(js)

all_handles = driver.window_handles

for handle in all_handles:
    print("handle: ",handle)'''
#driver.quit()
sleep(10)