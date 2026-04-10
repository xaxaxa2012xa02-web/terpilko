import tkinter as tk
from tkinter import Toplevel

def open_custom_window(button_id, parent):
    # Створюємо дочірнє вікно
    child_window = Toplevel(parent)
    child_window.geometry("400x250")
    
    # Налаштування контенту залежно від ID
    data = {
        "btn1": ("Вікно №1: Головний біль", "незн нез незн."),
        "btn2": ("Вікно №2: Біль у животі", "та ну реально."),
        "btn3": ("Вікно №3: Біль у горлі", "що ви від мене хочете."),
        "btn4": ("Вікно №4: Кріпатура", "1234."),
        "btn5": ("Вікно №5: Діарея", "Фемтаніл, Крокодил, Бронхалик.")
    }
    
    title, message = data.get(button_id, ("Вікно", "..."))
    
    child_window.title(title)
    
    # Текст у вікні
    label = tk.Label(child_window, text=message, font=("Arial", 10), wraplength=350)
    label.pack(pady=40, padx=20)
    
    # Кнопка закриття
    close_btn = tk.Button(child_window, text="прикрити", command=child_window.destroy)
    close_btn.pack(pady=20)

# Головне вікно
root = tk.Tk()
root.title("Головне меню TERPILO")
root.geometry("300x450")

# Список кнопок
buttons_info = [
    {"id": "btn1", "text": "Головний біль"},
    {"id": "btn2", "text": "Біль у животі"},
    {"id": "btn3", "text": "Біль у горлі"},
    {"id": "btn4", "text": "Кріпатура"},
    {"id": "btn5", "text": "Діарея"}
]

# Створення кнопок у циклі
for info in buttons_info:
    btn = tk.Button(
        root, 
        text=info["text"], 
        height=2, 
        width=25,
        command=lambda i=info["id"]: open_custom_window(i, root)
    )
    btn.pack(pady=10)

# Запуск програми
root.mainloop()