
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
        "giỏi": "t_dot",
        "dốt": "t_gioi",
        "hay": "t_do",
        "dở": "t_hay",
        "đắt": "t_re",
        "rẻ": "t_dat",
        "vui": "t_buon",
        "buồn": "t_vui",
        "đẹp": "t_xau",
        "xấu": "t_dep",
        "lười": "t_sieng",
        "siêng": "t_luoi",
        "lớn": "t_nho",
        "nhỏ": "t_lon",
        "kém": "t_kha",
        "khá": "t_kem",
        "khoẻ": "t_yeu",
        "yếu": "t_khoe",
        "ồn_ào": "t_im_lang",
        "im_lặng": "t_on_ao",
        "ồn": "t_im",
        "im": "t_on",
        "xui_xẻo": "t_may_man",
        "may_mắn": "t_xui_xeo",
        "nắng": "t_mua",
        "mưa": "t_nang",
        "hên": "_xui",
        "xui": "_hen",
        "quên": "_nho",
        "nhớ": "_quen",
        "đông":"_vang",
        "vắng":"_dong",
        "buổi_sáng":"_buoi_toi",
        "buổi_tối":"_buoi_sang",
        "này":"_kia",
        "kia": "_nay",
        "hoàn_thành":"_do_dang",
        "dở_dang":"_hoan_thanh",
        "quen":"_la",
        "lạ":"_quen",
        "thích":"_chan",
        "chán":"_thich"
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
        "t_day": "dày",
        "t_gioi": "giỏi",
        "t_dot": "dốt",
        "t_hay": "hay",
        "t_do": "dở",
        "t_dat": "đắt",
        "t_re": "rẻ",
        "t_vui": "vui",
        "t_buon": "buồn",
        "t_dep": "đẹp",
        "t_xau": "xấu",
        "t_luoi": "lười",
        "t_sieng": "siêng",
        "t_lon": "lớn",
        "t_nho": "nhỏ",
        "t_kha": "khá",
        "t_kem": "kém",
        "t_khoe": "khoẻ",
        "t_yeu": "yếu",
        "t_on_ao": "ồn ào",
        "t_im_lang": "im lặng",
        "t_on": "ồn",
        "t_im": "im",
        "t_xui_xeo": "xui xẻo",
        "t_may_man": "may mắn",
        "t_nang": "nắng",
        "t_mua": "mưa",
        "_hen": "hên",
        "_xui": "xui",
        "_nho":"nhớ",
        "_quen":"quên",
        "_dong":"đông",
        "_vang":"vắng",
        "_buoi_toi":"buổi tối",
        "_buoi_sang": "buổi sáng",
        "_nay":"này",
        "_kia":"kia",
        "_hoan_thanh":"hoàn thành",
        "_do_dang":"dở dang",
        "_quen":"quen",
        "_la":"lạ",
        "_thich":"thích",
        "_chan":"chán"
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
df['không cần']
    # Lưu lại kết quả vào file Excel mới
    new_file_path = file_path.replace('.xlsx', '_modified.xlsx')
    df.to_excel(new_file_path, sheet_name=sheet_name, index=False)

    print(f"Kết quả đã được lưu tại {new_file_path}")

# Sử dụng hàm
file_path = 'saito_2.xlsx'
sheet_name = 'sheet1'
swap_phrases_in_column_b(file_path, sheet_name)