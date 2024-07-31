
import pandas as pd

# Đọc dữ liệu từ tệp Excel
file_path = 'ngan_sach_nhanh_chong_2023_1.xlsx'
df = pd.read_excel(file_path)

# Đếm số lần xuất hiện của mỗi ngày trong tuần
ngay_counts = df['Ngày 2'].value_counts()
thu_counts = df['Thứ'].value_counts()
thang_counts = df['Tháng'].value_counts()



# In kết quả
print(ngay_counts)
print(thu_counts)
print(thang_counts)
'''
import pandas as pd
import unicodedata

# Hàm để chuẩn hóa chuỗi ký tự và chuyển về chữ thường
def normalize_string(s):
    if isinstance(s, float):  # Kiểm tra nếu s là float (có thể là NaN)
        return ''
    return unicodedata.normalize('NFKC', s.strip().lower())

# Đọc dữ liệu từ tệp Excel
file_path = 'ngan_sach_nhanh_chong_2024.xlsx'
df = pd.read_excel(file_path)

# Chuyển đổi tất cả các giá trị trong cột 'Days' sang chuỗi và chuẩn hóa
df['TK'] = df['TK'].astype(str).apply(normalize_string)

# Đếm số lần xuất hiện của mỗi ngày trong tuần
day_counts = df['TK'].value_counts()

# In kết quả
print(day_counts)
'''