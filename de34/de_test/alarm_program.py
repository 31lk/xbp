import time
import tkinter as tk
from tkinter import messagebox

# アラーム設定用リスト
record = []

# アラーム設定ウィンドウ
def set_alarm():
    def save_alarm():
        hour = int(option_hours.get())
        minute = int(option_minutes.get())
        record.append((hour, minute))
        alarm_window.destroy()

    alarm_window = tk.Tk()
    alarm_window.title("アラーム設定")
    
    option_hours = tk.StringVar(alarm_window)
    option_minutes = tk.StringVar(alarm_window)

    # 時間選択のドロップダウンメニュー
    hour_label = tk.Label(alarm_window, text="時:")
    hour_label.pack(side=tk.LEFT)
    hour_dropdown = tk.OptionMenu(alarm_window, option_hours, *range(24))
    hour_dropdown.pack(side=tk.LEFT)

    minute_label = tk.Label(alarm_window, text="分:")
    minute_label.pack(side=tk.LEFT)
    minute_dropdown = tk.OptionMenu(alarm_window, option_minutes, *range(60))
    minute_dropdown.pack(side=tk.LEFT)

    save_button = tk.Button(alarm_window, text="設定", command=save_alarm)
    save_button.pack()

    alarm_window.mainloop()

# アラーム表示ウィンドウ
def show_alarm(hour, minute):
    alarm_message = f"アラーム時間: {hour}時{minute}分"
    messagebox.showinfo("アラーム", alarm_message)

# アラームチェックと表示
def check_alarms():
    while True:
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min
        for alarm in record:
            hour, minute = alarm
            if current_hour == hour and current_minute == minute:
                show_alarm(hour, minute)
                record.remove(alarm)
        time.sleep(1)

# アラーム設定ウィンドウを表示
set_alarm()

# アラームチェックを開始
check_alarms()
