import tkinter as tk
from tkinter import messagebox

def giai_phuong_trinh():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        
        if a == 0:
            if b == 0:
                ket_qua.set("Phương trình có vô số nghiệm")
            else:
                ket_qua.set("Phương trình vô nghiệm")
        else:
            x = -b / a
            # Hiển thị kết quả làm tròn 4 chữ số thập phân nếu cần
            ket_qua.set(f"Phương trình có nghiệm: x = {x:.4g}")
            
    except ValueError:
        messagebox.showerror("Lỗi nhập liệu", "Vui lòng chỉ nhập các chữ số hợp lệ vào ô a và b.")

# 1. Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Giải Phương Trình Bậc 1")
root.geometry("320x220")
root.eval('tk::PlaceWindow . center')

# 2. Tạo các thành phần giao diện (Widgets)
tk.Label(root, text="Giải phương trình ax + b = 0", font=("Arial", 12, "bold")).pack(pady=10)

frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=5)

tk.Label(frame_inputs, text="Nhập a:").grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(frame_inputs, width=15)
entry_a.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Nhập b:").grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(frame_inputs, width=15)
entry_b.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Giải Phương Trình", command=giai_phuong_trinh, bg="lightblue").pack(pady=10)

ket_qua = tk.StringVar()
tk.Label(root, textvariable=ket_qua, fg="red", font=("Arial", 11, "bold")).pack(pady=5)

# 3. Chạy vòng lặp giao diện
root.mainloop()