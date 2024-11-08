"""
需要测试机环境安装andorid build环境，并运行aapt工具进行解析包名
appt dump badging       需要添加到系统环境变量
从结果中获取对应的app 版本号，这里获取 versionName+versionCode
"""
# encoding = 'utf-8'

import re
import subprocess as sbp
import zipfile
import plistlib

#!!!!!!!!!!!!!!!有问题
def get_apk_version(apk_path):      # apk_path = path to your apk package

    try:
        command = r'aapt'
        args = ['dump', 'badging', apk_path]
        cresult = sbp.run([command] + args, capture_output=True, text=True, shell=True)
        output = cresult.stdout
        # print(output)
        version_name = re.search(r"versionName='([^']+)'", output)
        build_date = re.search(r"versionCode='([^']+)'", output)

        if 'versionName' and 'versionCode':
            versionname = version_name.group(1)
            builddate = build_date.group(1)
            version = str(versionname) + '_' + str(builddate)
            # print(version)
            return version
        else:
            return None
    except sbp.CalledProcessError as e:
        print("error:", e.output)
        return None
    except Exception as e:
        print("Error:", e)
        return None


# 获取IPA包版本号
def get_ios_version(ipa_path):      # ipa_path = path to your ipa package
    # 解压 IPA 文件
    with zipfile.ZipFile(ipa_path, 'r') as ipa_zip:
        for file_name in ipa_zip.namelist():
            if file_name.endswith('Info.plist'):

                # 提取 Info.plist 文件内容
                with ipa_zip.open(file_name) as plist_file:
                    plist_data = plist_file.read()

                    # 解析 plist 数据
                    info_plist = plistlib.loads(plist_data)
                    # print(info_plist)
                    version = info_plist['CFBundleShortVersionString']
                    return version



