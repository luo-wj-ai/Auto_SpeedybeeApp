import openpyxl

def translate_excel(file_path, translations):
    # 加载Excel文件
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    # 遍历第三列，跳过第一行
    for row in sheet.iter_rows(min_row=2, min_col=3, max_col=4):
        keyword = row[0].value  # 第三列的值
        if keyword in translations:
            row[1].value = translations[keyword]  # 在第四列写入对应的中文翻译

    # 保存修改后的文件
    wb.save(file_path)
    print(f"文件已更新: {file_path}")

# 翻译规则
translations = {
    "AUTOCLOSERF": "自动关闭射频",
    "BBL": "黑盒子解析",
    "BEE25_INSTRUCTIONS": "新手指引",
    "BEE35_INSTRUCTIONS": "新手指引",
    "BLE_FIRMWARE": "蓝牙固件更新",
    "BTNANOV3_SETTINGS": "设置页",
    "CHARGING_VIEWER": "Adapter3充电展示",
    "F405WING_SETTINGS": "设置页",
    "FC_FLASHER": "飞控固件烧写",
    "FIXNAMEANDPWD": "修改名称和密码",
    "LED_STRIPS_SETTINGS": "流星灯带设置",
    "MASTER5_INSTRUCTIONS": "新手指引",
    "NAME_EDIT": "名字编辑",
    "PASSWORD_EDIT": "密码编辑",
}

# 输入文件路径
file_path = r"C:\Users\28449\Downloads\工具箱具体分类.xlsx"  # 替换为你的文件路径

# 调用函数
translate_excel(file_path, translations)
