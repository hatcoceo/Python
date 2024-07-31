import pandas as pd

# Đọc tệp Excel
df = pd.read_excel('Bài đăng.xlsx')

# Giả sử cột bạn muốn thống kê có tên là 'nội dung''
# Tạo một cột mới để lưu số lượng từ
df['SoLuongTu'] = df['nội dung'].apply(lambda x: len(str(x).split()))

# In kết quả
print(df[['nội dung', 'SoLuongTu']])

# Lưu kết quả ra tệp Excel mới nếu cần
df.to_excel('ket_qua_thong_ke.xlsx', index=False)
#
