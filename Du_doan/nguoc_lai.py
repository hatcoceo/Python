import pandas as pd
import re

# Định nghĩa các cặp từ cần thay thế
swap_dict = {
    "có": "TMP_khong",
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
    "chán":"_thich",
    "chưa":"_da",
    "đã":"_chua",
    "ở_nhà":"_o_ngoai",
    "ở_ngoài":"_o_nha",
    "cũ":"_moi",
    "mới":"_cu",
    "trái":"_phai",
    "phải":"_trai",
    "nhiều_lần":"_it_lan",
    "ít_lần":"_nhieu_lan",
    "bị":"_khong_bi",
    "không_bị":"_bi",
    "thông_minh":"_ngu_dot",
    "ngu_dốt":"_thong_minh",
    "ổn_định":"_bat_dinh",
    "bất_định":"_on_dinh",
    "tiết_kiệm":"_hoang_phi",
    "hoang_phí":"_tiet_kiem",
    "bổ_ích":"_doc_hai",
    "độc_hại":"_bo_ich",
    "khái_quát":"_chi_tiet",
    "chi_tiết":"_khai_quat",
    "tắt":"_mo",
    "mở":"_tat",
     "liền_mạch":"_ngat_quang",
     "ngắt_quãng":"_lien_mach"
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
    "t_on_ao": "ồn_ào",
    "t_im_lang": "im_lặng",
    "t_on": "ồn",
    "t_im": "im",
    "t_xui_xeo": "xui_xẻo",
    "t_may_man": "may_mắn",
    "t_nang": "nắng",
    "t_mua": "mưa",
    "_hen": "hên",
    "_xui": "xui",
    "_nho":"nhớ",
    "_quen":"quên",
    "_dong":"đông",
    "_vang":"vắng",
    "_buoi_toi":"buổi_tối",
    "_buoi_sang": "buổi_sáng",
    "_nay":"này",
    "_kia":"kia",
    "_hoan_thanh":"hoàn_thành",
    "_do_dang":"dở_dang",
    "_la":"lạ",
    "_thich":"thích",
    "_chan":"chán",
    "_chua":"chưa",
    "_da":"đã",
    "_o_nha":"ở_nhà",
    "_o_ngoai":"ở_ngoài",
    "_moi":"mới",
    "_cu":"cũ",
    "_trai":"trái",
    "_phai":"phải",
    "_nhieu_lan":"nhiều_lần",
    "_it_lan":"ít_lần",
    "_khong_bi":"không_bị",
    "_bi":"bị",
    "_thong_minh":"thông_minh",
    "_ngu_dot":"ngu_dốt",
    "_on_dinh":"ổn_định",
    "_bat_dinh":"bất_định",
    "_tiet_kiem":"tiết_kiệm",
    "_hoang_phi":"hoang_phí",
    "_bo_ich":"bổ_ích",
    "_doc_hai":"độc_hại",
    "_khai_quat":"khái_quát",
    "_chi_tiet":"chi_tiết",
    "_tat":"tắt",
    "_mo":"mở",
    "_lien_mach":"liền mạch",
    "_ngat_quang":"ngắt quãng"
 
}

def swap_phrases_in_column_b(file_path, sheet_name):
    # Đọc dữ liệu từ file Excel
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Định nghĩa hàm chuyển đổi sử dụng biểu thức chính quy
    def swap_phrase(val, dictionary):
        pattern = re.compile(r'\b(' + '|'.join(map(re.escape, dictionary.keys())) + r')\b')
        return pattern.sub(lambda x: dictionary[x.group()], val)
    
    # Áp dụng bước 1: Thay thế từ bằng từ tạm thời
    df['ngược lại'] = df['thành phần'].apply(lambda x: swap_phrase(x, swap_dict))
    
    # Áp dụng bước 2: Thay thế từ tạm thời bằng từ cuối cùng
    df['ngược lại'] = df['ngược lại'].apply(lambda x: swap_phrase(x, final_dict))
    
    # Lưu lại kết quả vào file Excel mới
    new_file_path = file_path.replace('.xlsx', '_modified.xlsx')
    df.to_excel(new_file_path, sheet_name=sheet_name, index=False)
    print(f"Kết quả đã được lưu tại {new_file_path}")
    
    # Gọi hàm lưu từ điển vào file Excel khác
  #  output_dict_file = 'dicts_output.xlsx'
  #  save_dicts_to_excel(swap_dict, final_dict, output_dict_file)
  #  print(f"Từ điển đã được lưu tại {output_dict_file}")
    
    # Gọi hàm tạo bảng 4 cột
    combined_dict_file = 'combined_dicts.xlsx'
    save_combined_dict_to_excel(swap_dict, final_dict, combined_dict_file)
    print(f"Bảng tổng hợp đã được lưu tại {combined_dict_file}")

def save_dicts_to_excel(swap_dict, final_dict, output_file):
    # Chuyển đổi swap_dict và final_dict thành DataFrames
    swap_df = pd.DataFrame(list(swap_dict.items()), columns=['Original', 'Temporary'])
    final_df = pd.DataFrame(list(final_dict.items()), columns=['Temporary', 'Final'])
    
    # Ghi các DataFrames vào file Excel
    with pd.ExcelWriter(output_file) as writer:
        swap_df.to_excel(writer, sheet_name='Swap Dict', index=False)
        final_df.to_excel(writer, sheet_name='Final Dict', index=False)

def save_combined_dict_to_excel(swap_dict, final_dict, output_file):
    # Tạo danh sách các bản ghi
    records = []
    for original, temporary in swap_dict.items():
        final = final_dict.get(temporary, None)
        records.append({
            'Original': original,
            'Temporary': temporary,
            'Final': final
        })
    
    # Tạo DataFrame
    combined_df = pd.DataFrame(records)
    
    # Ghi DataFrame vào file Excel
    combined_df.to_excel(output_file, sheet_name='Combined Dict', index=False)

# Sử dụng hàm
file_path = 'nguoc_lai_2.xlsx'
sheet_name = 'sheet1'
swap_phrases_in_column_b(file_path, sheet_name)
