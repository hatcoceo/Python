
import pandas as pd

# Đọc dữ liệu từ tệp Excel
file_path = 'ngan_sach_nhanh_chong_2023_1.xlsx'
df = pd.read_excel(file_path)

# Đếm số lần xuất hiện của mỗi thứ , ngày, tháng trong tuần
ngay_counts = df['Ngày 2'].value_counts()
thu_counts = df['Thứ'].value_counts()
thang_counts = df['Tháng'].value_counts()



# In kết quả
print(ngay_counts)
print(thu_counts)
print(thang_counts)
