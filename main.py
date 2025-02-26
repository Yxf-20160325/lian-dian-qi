 import tkinter as tk
import pyautogui
import threading
import time
# 全局变量，用于控制连点的开关
running = False

def start_clicking():
    time.sleep(3)
    global running
    running = True
    try:
        # 获取用户输入的点击间隔时间和点击次数
        interval = float(entry_interval.get())
        click_count = int(entry_count.get())
        # 禁用开始按钮
        button_start.config(state=tk.DISABLED)
        # 创建一个新线程来执行连点操作
        thread = threading.Thread(target=clicking, args=(interval, click_count))
        thread.start()
    except ValueError:
        # 处理输入非数字的异常
        result_label.config(text="请输入有效的数字！")

def stop_clicking():
    global running
    running = False

def clicking(interval, click_count):
    global running
    count = 0
    while running and count < click_count:
        # 执行鼠标左键点击操作
        pyautogui.click()
        count += 1
        # 显示当前点击次数
        result_label.config(text=f"已点击 {count} 次")
        # 等待指定的间隔时间
        time.sleep(interval)
    if running:
        result_label.config(text="已完成指定次数的点击。")
    else:
        result_label.config(text="连点已停止。")
    # 重新启用开始按钮
    button_start.config(state=tk.NORMAL)

# 创建主窗口
root = tk.Tk()
root.title("连点器")
root.geometry("600x600")
label = tk.Label(root, text="连点器")
label.pack()
label2 = tk.Label(root, text="开始后将在3秒后开始")
label2.pack()

# 创建标签和输入框，用于设置点击间隔时间
label_interval = tk.Label(root, text="点击间隔时间 (秒):")
label_interval.pack(pady=10)

entry_interval = tk.Entry(root)
entry_interval.insert(0, "0.1")  # 默认间隔时间为0.1秒
entry_interval.pack(pady=5)

# 创建标签和输入框，用于设置点击次数
label_count = tk.Label(root, text="点击次数:")
label_count.pack(pady=10)

entry_count = tk.Entry(root)
entry_count.insert(0, "10")  # 默认点击次数为10次
entry_count.pack(pady=5)

# 创建开始、停止按钮和关闭按钮
button_start = tk.Button(root, text="开始连点", command=start_clicking)
button_start.pack(pady=20)

button_stop = tk.Button(root, text="停止连点", command=stop_clicking)
button_stop.pack(pady=10)

button_quit = tk.Button(root, text="退出", command=root.quit)
button_quit.pack(pady=20)
# 创建用于显示结果的标签
result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# 运行主循环
root.mainloop()
