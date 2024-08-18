import pandas as pd 
import numpy as np 

def replace_first_g_with_h(lst):
    new_lst = []
    for item in lst:
        # Tách chuỗi thành các phần tử dựa trên khoảng trắng
        parts = item.split()
        # Nếu chuỗi có 3 phần tử trở lên, thay thế 'g' đầu tiên bằng 'h'
        if len(parts) >= 3:
            new_item = item.replace('g', 'h', 1)
        else:
            new_item = item  # Giữ nguyên chuỗi nếu có ít hơn 3 phần tử
        new_lst.append(new_item)
    return new_lst

# Ví dụ sử dụng
#input_list = ['15p 12g', '25g 30p 13g', '30g', '45g', '60p']

#output_list = replace_first_g_with_h(input_list)
#print(output_list)

def convert_to_seconds(lst):
    new_lst = []
    for item in lst:
        total_seconds = 0
        parts = item.split()
        for part in parts:
            if part.endswith('h'):
                total_seconds += int(part[:-1]) * 3600  # Giờ chuyển thành giây
            elif part.endswith('p'):
                total_seconds += int(part[:-1]) * 60  # Phút chuyển thành giây
            elif part.endswith('g'):
                total_seconds += int(part[:-1])  # Giây giữ nguyên
        new_lst.append(total_seconds)
    return new_lst

# Ví dụ sử dụng
#input_list = ['15p 12g', '25g 30p 13g', '30g', '1h 30p', '2h 45p 10g']
#output_list_2= convert_to_seconds(output_list)
#print(output_list_2)