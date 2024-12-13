import os
import json

# 定义要生成的 JSON 文件名及其结构
file_names = [
    "SetupAct.json",
    "PortAct.json",
    "ConfigureAct.json",
    "MotorAct.json",
    "ReceiverAct.json",
    "OsdAct.json",
    "VtxAct.json",
    "GpsAct.json",
    "ModeAct.json"
]

# JSON 模板内容
template = {
    "某某某Act": {
        "action1": [
            {
                "action": "click",
                "appby": "XPATH",
                "cond": "el",
                "ele": "",
                "comment": "注释"
            },
            {
                "action": "sendkeys",
                "appby": "XPATH",
                "cond": "el",
                "ele": "",
                "keys": "",
                "comment": "注释"
            }
        ]
    }
}

# 定义输出目录
output_dir = "D:\Automation\SpeedybeeApp\Element\Bee25\Android_Ele\Flight_settings"

# 确保目录存在
os.makedirs(output_dir, exist_ok=True)

# 创建 JSON 文件并写入模板内容
for file_name in file_names:
    # 动态更新键名为文件对应的 Act 名称
    act_name = file_name.replace(".json", "")  # 去掉 ".json" 后缀
    content = template.copy()
    content[act_name] = content.pop("某某某Act")  # 替换模板中的 "某某某Act"

    # 写入到文件
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)  # 格式化输出

print(f"JSON 文件已生成在目录: {output_dir}")
