
import pandas as pd
import re

def swap_phrases_in_column_b(file_path, sheet_name):
    # Đọc dữ liệu từ file Excel
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Định nghĩa các cặp từ cần thay thế
    swap_dict = {
        "có": "TMP_khong",   # Sử dụng từ tạm thời
        "không": "TMP_co",
        "trên": "TMP_duoi",
        "dưới": "TMP_tren",
        "trắng": "TMP_den",
        "đen": "TMP_trang",
        "trước": "T_sau",
        "sau": "T_truoc",
        "xa": "T_gan",
        "gần": "T_xa",
        "muộn": "t_som",
        "sớm": "t_muon",
        "khó": "t_de",
        "dễ": "t_kho",
        "tốt": "t_xau",
        "xấu": "t_tot",
        "trong": "t_ngoai",
        "ngoài": "t_trong",
        "nhiều": "t_it",
        "ít": "t_nhieu",
        "nóng": "t_lanh",
        "lạnh": "t_nong",
        "hết": "t_con",
        "còn": "t_het",
        "nhanh": "t_cham",
        "chậm": "t_nhanh",
        "dày": "t_mong",
        "mỏng": "t_day",
        
    }

    # Định nghĩa các từ tạm thời chuyển thành giá trị cuối cùng
    final_dict = {
        "TMP_khong": "không",
        "TMP_co": "có",
        "TMP_duoi": "dưới",
        "TMP_tren": "trên",
        "TMP_trang": "trắng",
        "TMP_den": "đen",
        "T_truoc": "trước",
        "T_sau": "sau",
        "T_xa": "xa",
        "T_gan": "gần",
        "t_muon": "muộn",
        "t_som": "sớm",
        "t_kho": "khó",
        "t_de": "dễ",
        "t_tot": "tốt",
        "t_xau": "xấu",
        "t_trong": "trong",
        "t_ngoai": "ngoài",
        "t_nhieu": "nhiều",
        "t_it": "ít",
        "t_nong": "nóng",
        "t_lanh": "lạnh",
        "t_het": "hết",
        "t_con": "còn",
        "t_nhanh": "nhanh",
        "t_cham": "chậm",
        "t_mong": "mỏng",
        "t_day": "dày"
        
    }

    # Định nghĩa hàm chuyển đổi sử dụng biểu thức chính quy
    def swap_phrase(val, dictionary):
        for key, value in dictionary.items():
            # Sử dụng re.sub để thay thế từ khóa bằng giá trị tương ứng
            val = re.sub(r'\b' + re.escape(key) + r'\b', value, val)
        return val

    # Áp dụng bước 1: Thay thế từ bằng từ tạm thời
    df['ngược lại'] = df['thành phần'].apply(lambda x: swap_phrase(x, swap_dict))

    # Áp dụng bước 2: Thay thế từ tạm thời bằng từ cuối cùng
    df['ngược lại'] = df['ngược lại'].apply(lambda x: swap_phrase(x, final_dict))

    # Lưu lại kết quả vào file Excel mới
    new_file_path = file_path.replace('.xlsx', '_modified.xlsx')
    df.to_excel(new_file_path, sheet_name=sheet_name, index=False)

    print(f"Kết quả đã được lưu tại {new_file_path}")

# Sử dụng hàm
file_path = 'saito_2.xlsx'
sheet_name = 'sheet1'
swap_phrases_in_column_b(file_path, sheet_name)

'''
import pandas as pd
import re

def swap_phrases_in_column_b(file_path, sheet_name):
    # Đọc dữ liệu từ file Excel
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Đọc các cặp từ cần thay thế từ hai cột
    swap_dict_df = pd.read_excel(file_path, sheet_name=sheet_name, usecols=['C1', 'C2'])
    swap_dict = pd.Series(swap_dict_df['C2'].values, index=swap_dict_df['C1']).to_dict()

    # Đọc các từ tạm thời và giá trị cuối cùng từ hai cột
    final_dict_df = pd.read_excel(file_path, sheet_name=sheet_name, usecols=['D1', 'D2'])
    final_dict = pd.Series(final_dict_df['D2'].values, index=final_dict_df['D1']).to_dict()

    # Định nghĩa hàm chuyển đổi sử dụng biểu thức chính quy
    def swap_phrase(val, dictionary):
        if pd.isna(val):
            return val
        for key, value in dictionary.items():
            # Sử dụng re.sub để thay thế từ khóa bằng giá trị tương ứng
            val = re.sub(r'\b' + re.escape(key) + r'\b', value, val)
        return val

    # Áp dụng bước 1: Thay thế từ bằng từ tạm thời
    df['ngược lại'] = df['a'].apply(lambda x: swap_phrase(x, swap_dict))

    # Áp dụng bước 2: Thay thế từ tạm thời bằng từ cuối cùng
    df['ngược lại'] = df['ngược lại'].apply(lambda x: swap_phrase(x, final_dict))

    # Lưu lại kết quả vào file Excel mới
    new_file_path = file_path.replace('.xlsx', '_modified_2.xlsx')
    df.to_excel(new_file_path, sheet_name=sheet_name, index=False)

    print(f"Kết quả đã được lưu tại {new_file_path}")

# Sử dụng hàm
file_path = 'saito_3.xlsx'
sheet_name = 'sheet1'
swap_phrases_in_column_b(file_path, sheet_name)
'''