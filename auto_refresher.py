import threading
import tkinter as tk
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def run_button_press():
    url = url_entry.get()
    sec = sec_entry.get()

    if not url or not sec:
        error_msg.config(text="URL or Interval is empty. Please enter a valid Argument.", fg="red")
        return

    error_msg.config(text="")

    global stop_flag
    stop_flag = False

    threading.Thread(target=auto_refresh, args=(url, int(sec)), daemon=True).start()

def stop_button_press():
    global stop_flag
    stop_flag = True

def auto_refresh(url, sec):
    driver = webdriver.Chrome()

    try:
        driver.get(url)

        while not stop_flag:
            time.sleep(sec)
            driver.refresh()
    finally:
        driver.quit()

root = tk.Tk()

root.title("Auto Refresher")
root.geometry("600x340")
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(background = "#1d1d1d")

url_label = Label(root, text="\nEnter the URL", bg="#1d1d1d", fg="#8e27ea", font=("Cambria", 16, "bold"))
url_label.pack()

url_entry = tk.Entry(root, justify="center")
url_entry.pack(ipadx= 70, ipady=1.5)

sec_label = Label(root, text="\nEnter the Interval", bg="#1d1d1d", fg="#8e27ea", font=("Cambria", 16, "bold"))
sec_label.pack()

Label(root, text="in seconds", bg="#1d1d1d", fg="#8e27ea", font=("Cambria", 10,)).pack(pady=(0, 6))

sec_entry = tk.Entry(root, justify="center", width=8)
sec_entry.pack(ipady=1.5)
sec_entry.insert(0, "5")

run_button = tk.Button(root,
                       command=run_button_press,
                       background="#8e27ea",
                       foreground="#1d1d1d",
                       activebackground="#9640e3",
                       width=10,
                       height=1,
                       border=0,
                       cursor="hand2",
                       text="Run",
                       font=("Cambria", 16, "bold"))
run_button.pack(pady=16)

stop_button = tk.Button(root,
                        command=stop_button_press,
                        background="#75282e",
                        foreground="#1d1d1d",
                        activebackground="#8f383e",
                        width=6,
                        height=1,
                        border=0,
                        cursor="hand2",
                        text="Stop",
                        font=("Cambria", 16, "bold"))
stop_button.pack(pady=16)

error_msg = Label(root, text="", bg="#1d1d1d", fg="red", font=("Cambria", 12))
error_msg.pack()

root.mainloop()