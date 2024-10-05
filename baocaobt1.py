import tkinter as tk
from tkinter import messagebox

# Hàm tính toán
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

# Hàm để reset form
def reset():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_result.delete(0, tk.END)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Form Tính Toán")
root.geometry("400x300")
root.configure(bg="white")

# Tiêu đề
label_title = tk.Label(root, text="FORM TÍNH TOÁN", font=("Arial", 16, "bold"), fg="green", bg="white")
label_title.pack(pady=10)

# Label và Entry cho a
label_a = tk.Label(root, text="a:", font=("Arial", 12), bg="white")
label_a.place(x=50, y=60)
entry_a = tk.Entry(root, width=20, font=("Arial", 12))
entry_a.place(x=100, y=60)

# Label và Entry cho b
label_b = tk.Label(root, text="b:", font=("Arial", 12), bg="white")
label_b.place(x=50, y=100)
entry_b = tk.Entry(root, width=20, font=("Arial", 12))
entry_b.place(x=100, y=100)

# Label và Entry cho kết quả
label_result = tk.Label(root, text="Kết quả:", font=("Arial", 12), bg="white")
label_result.place(x=30, y=140)
entry_result = tk.Entry(root, width=20, font=("Arial", 12))
entry_result.place(x=100, y=140)

# Tạo các nút phép toán
button_plus = tk.Button(root, text="+", width=5, height=2, bg="green", fg="white", font=("Arial", 12),
                        command=lambda: calculate("+"))
button_plus.place(x=50, y=180)

button_minus = tk.Button(root, text="-", width=5, height=2, bg="green", fg="white", font=("Arial", 12),
                         command=lambda: calculate("-"))
button_minus.place(x=120, y=180)

button_multiply = tk.Button(root, text="*", width=5, height=2, bg="green", fg="white", font=("Arial", 12),
                            command=lambda: calculate("*"))
button_multiply.place(x=190, y=180)

button_divide = tk.Button(root, text="/", width=5, height=2, bg="green", fg="white", font=("Arial", 12),
                          command=lambda: calculate("/"))
button_divide.place(x=260, y=180)

# Nút reset
button_reset = tk.Button(root, text="Reset", width=10, height=2, bg="green", fg="white", font=("Arial", 12),
                         command=reset)
button_reset.place(x=150, y=230)

# Chạy giao diện
root.mainloop()
