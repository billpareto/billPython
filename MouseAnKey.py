import time

from pynput import mouse,keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller





# 键盘控制器
Ctlkeyboard = keyboard.Controller()


#组合键控制
with Ctlkeyboard.pressed(Key.alt):
    Ctlkeyboard.press(Key.tab)
    Ctlkeyboard.release(Key.tab)

'''
def on_press(key):
    try:
        print('字母键： {} 被按下'.format(key.char))
    except AttributeError:
        print('特殊键： {} 被按下'.format(key))

#keyboard.Key.alt+Key.tab
def on_release(key):
    print('{} 释放了'.format(key))
    if key == Key.esc:
        # 释放了esc 键，停止监听
        return False


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

# 开始监听
# 监听启动方式2：非阻断式
listener.start()

# 监听键盘键入
with keyboard.Events() as events:
    for event in events:

        # 监听esc键，释放esc键，停止监听。
        if event.key == keyboard.Key.esc:
            print('接收到事件 {}, 停止监听'.format(event))
            break
        else:
            if isinstance(event, keyboard.Events.Press):
                print('按下按键 {} '.format(event))
            elif isinstance(event, keyboard.Events.Release):
                print('松开按键 {}'.format(event))

'''




# 鼠标控制器
ctlmouse = mouse.Controller()

# 给点反应时间
time.sleep(2)

# 获取当前鼠标位置
print('当前鼠标位置： {}'.format(ctlmouse.position))

#ctlmouse.position=(460,215)
ctlmouse.click(Button.left,1)