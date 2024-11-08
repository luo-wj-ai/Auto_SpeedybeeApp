from SpeedybeeApp.AP.get_version import get_apk_version
from SpeedybeeApp.AP.get_version import get_ios_version
import time
import os


# 专家模式页面
class PAGENAME:
    setting = 'setting'
    port = 'port'
    congigure = 'congigure'
    batterypower = 'batterypower'
    failsafe = 'failsafe'
    preset = 'preset'
    pid = 'pid'
    receiver = 'receiver'
    mode = 'mode'
    adjustion = 'adjustion'
    elemachin = 'elemachin'
    osd = 'OSD'
    vtx = 'VTX'
    led = 'LED'
    sensor = 'sensor'
    log = 'log'
    blackbox = 'blackbox'


# 项目运行文件路径管理
class Filepath:

    # 需要修改你整个文件的绝对路径
    testpath = r"/Users/speedybee/Desktop/iOS_App_Test/SpeedybeeApp/"


    # cli模式运行命令结果存储路径
    apkresult_path = testpath + r'Result\\detail_result\\Android\\'
    iparesult_path = testpath + r'Result\\detail_result\\IOS\\'
    winresult_path = testpath + r'Result\\detail_result\\WIN\\'
    testresult_path = testpath + r'Result\\test_result\\'
    reportresult_path = testpath + r'Result/report_record'

    # 创建目录
    # os.makedirs(apkresult_path, exist_ok=True)
    # os.makedirs(iparesult_path, exist_ok=True)
    # os.makedirs(winresult_path, exist_ok=True)
    # os.makedirs(testresult_path, exist_ok=True)
    # os.makedirs(reportresult_path, exist_ok=True)


def packagepath(packname):
    # 本次测试版本的安装包
    testpath = r"D:\Project\pycode\pythonProject\SpeedybeeApp"

    if ".apk" in packname:
        apath = testpath + r"\\package\\" + str(packname)
        return apath
    elif ".ipa" in packname:
        ipapath = testpath + r"\\package\\" + str(packname)
        return ipapath
    else:
        return None


# android testcast 文件名称组成
def apkfilename(package):
    # 文件生成日期时间
    now = time.strftime("%H_%M_%S", time.localtime(time.time()))
    # your apkname
    apk_path = packagepath(package)
    apk_version = get_apk_version(apk_path)
    # 未携带文件路径
    if apk_version is None:
        # 如果没有获取到版本号，可以设置一个默认值或抛出异常
        apk_version = '_unknown_version_'
    print("apk_version:",apk_version)
    filename = 'Android' + apk_version + '_' + now + '_' + r"cli.txt"
    filename = str(filename)
    return filename


# IOS testcast 文件名称组成
def ipafilename(packname):
    # 文件生成日期时间
    now = time.strftime("%H_%M_%S", time.localtime(time.time()))
    # your ipaname
    ipa_path = packagepath(packname)
    ipa_version = get_ios_version(ipa_path)
    # 未携带文件路径
    filename = 'IOS' + ipa_version + '_' + now + '_' + r"cli.txt"
    filename = str(filename)
    return filename


# Win testcast 文件名称组成
def winfilename():
    # 文件生成日期时间
    now = time.strftime("%H_%M_%S", time.localtime(time.time()))
    # # path to your file
    # paste_win_path = filepath.winresult_path
    # 未携带文件路径
    paste_win_filename = "win_result" + '_' + now + ".txt"
    filename = str(paste_win_filename)
    return filename


# 测试报告生成文件名称
def reportfile_name():
    # 文件生成日期时间
    now = time.strftime("%H_%M_%S", time.localtime(time.time()))
    trname = 'UIautotest_report' + '_' + now + '.html'
    trname = str(trname)
    return trname
