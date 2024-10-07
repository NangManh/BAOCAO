import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            if b != 0:
                result = a / b
            else:
                messagebox.showerror("Lỗi", "Không thể chia cho 0")
                return
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập giá trị hợp lệ")

def reset():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_result.delete(0, tk.END)

root = tk.Tk()
root.title("Form Tính Toán")
root.geometry("500x400")  
root.configure(bg="#f0f8ff")  

def on_enter(e):
    e.widget['background'] = '#5f9ea0'

def on_leave(e):
    e.widget['background'] = e.widget.default_bg

label_title = tk.Label(root, text="FORM TÍNH TOÁN", font=("Arial", 20, "bold"), fg="#4682b4", bg="#f0f8ff")
label_title.pack(pady=20)

label_a = tk.Label(root, text="Nhập số a:", font=("Arial", 14), bg="#f0f8ff")
label_a.place(x=50, y=100)
entry_a = tk.Entry(root, width=20, font=("Arial", 14), bd=3, relief="groove")
entry_a.place(x=200, y=100)

label_b = tk.Label(root, text="Nhập số b:", font=("Arial", 14), bg="#f0f8ff")
label_b.place(x=50, y=150)
entry_b = tk.Entry(root, width=20, font=("Arial", 14), bd=3, relief="groove")
entry_b.place(x=200, y=150)

label_result = tk.Label(root, text="Kết quả:", font=("Arial", 14), bg="#f0f8ff")
label_result.place(x=50, y=200)
entry_result = tk.Entry(root, width=20, font=("Arial", 14), bd=3, relief="groove")
entry_result.place(x=200, y=200)

buttons_config = {
    "width": 5, 
    "height": 2, 
    "font": ("Arial", 12, "bold"), 
    "bg": "#4682b4", 
    "fg": "white", 
    "relief": "raised"
}

button_plus = tk.Button(root, text="+", **buttons_config, command=lambda: calculate("+"))
button_plus.place(x=100, y=270)
button_plus.default_bg = button_plus['bg']
button_plus.bind("<Enter>", on_enter)
button_plus.bind("<Leave>", on_leave)

button_minus = tk.Button(root, text="-", **buttons_config, command=lambda: calculate("-"))
button_minus.place(x=180, y=270)
button_minus.default_bg = button_minus['bg']
button_minus.bind("<Enter>", on_enter)
button_minus.bind("<Leave>", on_leave)

button_multiply = tk.Button(root, text="*", **buttons_config, command=lambda: calculate("*"))
button_multiply.place(x=260, y=270)
button_multiply.default_bg = button_multiply['bg']
button_multiply.bind("<Enter>", on_enter)
button_multiply.bind("<Leave>", on_leave)

button_divide = tk.Button(root, text="/", **buttons_config, command=lambda: calculate("/"))
button_divide.place(x=340, y=270)
button_divide.default_bg = button_divide['bg']
button_divide.bind("<Enter>", on_enter)
button_divide.bind("<Leave>", on_leave)

button_reset = tk.Button(root, text="Reset", width=10, height=2, bg="#32cd32", fg="white", font=("Arial", 12, "bold"),
                         command=reset)
button_reset.place(x=200, y=330)
button_reset.default_bg = button_reset['bg']
button_reset.bind("<Enter>", on_enter)
button_reset.bind("<Leave>", on_leave)

entry_a.focus()
root.mainloop()
