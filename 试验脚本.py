import os, requests, subprocess, urllib.parse, re
from bs4 import BeautifulSoup

class APKHandler:
    def __init__(self, save_directory): self.save_directory = save_directory
    def is_device_connected(self):
        adb_command = ['adb', 'devices']
        try:
            result = subprocess.run(adb_command, capture_output=True, text=True, check=True)
            devices = [line.split('\t')[0] for line in result.stdout.splitlines()[1:] if 'device' in line]
            if len(devices) != 1:
                print("检测到的设备数不为1: ", devices if devices else "无设备"); return False
            print(f"检测到设备：{devices[0]}"); return True
        except subprocess.CalledProcessError as e: print(f"ADB 检查设备失败: {e.stderr}"); return False
    def get_apk_version_and_build_number(self, apk_filename):
        apk_filename = urllib.parse.unquote(apk_filename)
        version_match = re.search(r'(\d+\.\d+\.\d+)', apk_filename)
        build_number_match = re.search(r'\((\d+)\)', apk_filename)
        version = version_match.group(1) if version_match else None
        build_number = int(build_number_match.group(1)) if build_number_match else -1
        return version, build_number
    def parse_version(self, version): return tuple(map(int, version.split('.')))
    def find_and_download_apk(self, base_url):
        try:
            response = requests.get(base_url)
            if response.status_code == 200:
                soup, links, apk_files = BeautifulSoup(response.text, 'html.parser'), [], []
                for link in soup.find_all('a', href=True):
                    if link['href'].endswith('.apk'):
                        version, build_number = self.get_apk_version_and_build_number(link['href'])
                        if version: apk_files.append((link['href'], version, build_number))
                if apk_files:
                    apk_files.sort(key=lambda x: (self.parse_version(x[1]), x[2]), reverse=True)
                    latest_apk_url = urllib.parse.urljoin(base_url, apk_files[0][0])
                    save_path = os.path.join(self.save_directory, apk_files[0][0].split('/')[-1])
                    self.download_apk(latest_apk_url, save_path); return save_path
                print("未找到 APK 文件")
            else: print(f"请求失败，状态码：{response.status_code}")
        except requests.exceptions.RequestException as e: print(f"请求发生异常：{e}")
        return None
    def download_apk(self, apk_url, save_path):
        try:
            print(f"{'文件已存在，正在覆盖' if os.path.exists(save_path) else '正在下载新文件'}: {save_path}")
            response = requests.get(apk_url)
            if response.status_code == 200:
                with open(save_path, 'wb') as f: f.write(response.content)
                print(f"APK 文件已成功下载到：{save_path}")
            else: print(f"下载失败，状态码：{response.status_code}")
        except requests.exceptions.RequestException as e: print(f"下载发生异常：{e}")
    def adb_install(self, apk_path):
        try:
            result = subprocess.run(['adb', 'install', apk_path], capture_output=True, check=True, text=True)
            print("安装成功:", result.stdout)
        except subprocess.CalledProcessError as e: print("安装失败:", e.stderr)
    def find_apk_in_directory(self, directory, version):
        for filename in os.listdir(directory):
            if filename.endswith('.apk') and version in filename: return os.path.join(directory, filename)
        return None

def main():
    save_directory = "./downloads"; os.makedirs(save_directory, exist_ok=True)
    handler = APKHandler(save_directory)
    if not handler.is_device_connected(): return
    print("请选择要执行的操作：\n0: 从 http://172.16.13.188:9090/download/apk/3.0.0/debug/ 下载并安装最新 APK\n1: 从 http://172.16.13.188:9090/download/apk/test/debug/ 下载并安装最新 APK\n3: 安装本地 APK 文件 C:\\Users\\28449\\Documents\\Speedybee\\安装包\\9.0.0\\9.0.0.apk\n999: 从目录 C:\\Users\\28449\\Documents\\Speedybee\\安装包\\线上 ——选择线上版本安装")
    choice = input("请输入选项 (0, 1, 3, 999): ")
    if choice == "0":
        url = "http://172.16.13.188:9090/download/apk/3.0.0/debug/"
        apk_path = handler.find_and_download_apk(url)
        if apk_path: handler.adb_install(apk_path)
    elif choice == "1":
        url = "http://172.16.13.188:9090/download/apk/test/debug/"
        apk_path = handler.find_and_download_apk(url)
        if apk_path: handler.adb_install(apk_path)
    elif choice == "3":
        apk_path = r"C:\Users\28449\Documents\Speedybee\安装包\9.0.0\9.0.0.apk"
        if os.path.exists(apk_path): handler.adb_install(apk_path)
        else: print(f"本地 APK 文件不存在：{apk_path}")
    elif choice == "999":
        directory = r"C:\Users\28449\Documents\Speedybee\安装包\线上"
        apk_files = [f for f in os.listdir(directory) if f.endswith('.apk')]
        print("可用的 APK 文件：\n" + "\n".join(apk_files))
        version = input("请输入要安装的版本号 (如 2.2.2): ")
        apk_path = handler.find_apk_in_directory(directory, version)
        if apk_path:
            print(f"找到版本号 {version} 的 APK 文件：{apk_path}")
            handler.adb_install(apk_path)
        else: print(f"未找到版本号 {version} 的 APK 文件，请检查输入或文件是否存在。")
    else: print("无效选项，请重新运行程序。")

if __name__ == "__main__": main()
