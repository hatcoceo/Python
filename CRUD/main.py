
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Kết nối đến cơ sở dữ liệu SQLite
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Tạo bảng
c.execute('''CREATE TABLE IF NOT EXISTS products
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
              name TEXT NOT NULL, 
              price REAL)''')

# Hàm thêm sản phẩm
def add_product():
    name = entry_name.get()
    price = entry_price.get()
    
    if name and price:
        try:
            c.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, float(price)))
            conn.commit()
            messagebox.showinfo("Success", "Product added successfully!")
            entry_name.delete(0, tk.END)
            entry_price.delete(0, tk.END)
            view_products()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid price.")
    else:
        messagebox.showerror("Error", "Please enter both name and price.")

# Hàm xem sản phẩm
def view_products():
    listbox.delete(0, tk.END)
    c.execute('SELECT * FROM products')
    for row in c.fetchall():
        listbox.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}")

# Hàm xóa sản phẩm
def delete_product():
    try:
        selected_item = listbox.curselection()[0]
        product = listbox.get(selected_item)
        product_id = product.split(',')[0].split(': ')[1]
        c.execute('DELETE FROM products WHERE id = ?', (product_id,))
        conn.commit()
        messagebox.showinfo("Success", "Product deleted successfully!")
        view_products()
    except IndexError:
        messagebox.showerror("Error", "Please select a product to delete.")

# Hàm cập nhật sản phẩm
def update_product():
    try:
        selected_item = listbox.curselection()[0]
        product = listbox.get(selected_item)
        product_id = product.split(',')[0].split(': ')[1]
        new_name = entry_name.get()
        new_price = entry_price.get()
        
        if new_name and new_price:
            c.execute('UPDATE products SET name = ?, price = ? WHERE id = ?', (new_name, float(new_price), product_id))
            conn.commit()
            messagebox.showinfo("Success", "Product updated successfully!")
            entry_name.delete(0, tk.END)
            entry_price.delete(0, tk.END)
            view_products()
        else:
            messagebox.showerror("Error", "Please enter both name and price.")
    except IndexError:
        messagebox.showerror("Error", "Please select a product to update.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid price.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Product Manager")

# Tạo nhãn và ô nhập liệu
tk.Label(root, text="Product Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Product Price:").grid(row=1, column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=1, column=1)

# Tạo các nút cho các thao tác CRUD
btn_add = tk.Button(root, text="Add Product", command=add_product)
btn_add.grid(row=2, column=0, columnspan=2)

btn_update = tk.Button(root, text="Update Product", command=update_product)
btn_update.grid(row=3, column=0, columnspan=2)

btn_delete = tk.Button(root, text="Delete Product", command=delete_product)
btn_delete.grid(row=4, column=0, columnspan=2)

# Tạo listbox để hiển thị các sản phẩm
listbox = tk.Listbox(root, width=50)
listbox.grid(row=5, column=0, columnspan=2)

# Xem sản phẩm khi mở ứng dụng
view_products()

# Chạy vòng lặp chính
root.mainloop()

# Đóng kết nối cơ sở dữ liệu khi đóng ứng dụng
conn.close()
