
import pandas as pd
from collections import Counter
import re

# Đọc dữ liệu từ file Excel
file_path = 'bài đăng.xlsx'
df = pd.read_excel(file_path)

# Kết hợp tất cả các nội dung thành một chuỗi dài
all_text = ' '.join(df['nội dung'].dropna().astype(str))

# Chuyển chuỗi thành các từ riêng lẻ
words = re.findall(r'\w+', all_text.lower())

# Đếm tần suất xuất hiện của các từ
word_count = Counter(words)

# Chuyển đổi kết quả thành DataFrame để dễ xem
word_count_df = pd.DataFrame(word_count.items(), columns=['word', 'count']).sort_values(by='count', ascending=False)

# Hiển thị toàn bộ các hàng trong DataFrame
pd.set_option('display.max_rows', None)

print(word_count_df)

