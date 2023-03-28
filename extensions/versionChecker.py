import contextlib
import requests
import urllib.request
import os
import zipfile
import shutil

def get_version(file_path):
    with open(file_path, 'r') as f:
        return f.read()[9:-1]
    
def get_remote_version(url):
    try:
        info = requests.get(url)
        return int(str(info.content)[11:-3].replace('.', ''))
    except Exception:
        return None

def check_version(url='https://raw.githubusercontent.com/Intofire-Studios/Chronicles-of-Arclight/master/extensions/version.txt', file_path='extensions/version.txt'):
    cur_ver = int(get_version(file_path).replace('.', ''))
    remote_ver = get_remote_version(url)
    if remote_ver and remote_ver > cur_ver:
        return True
    return False

def download_and_extract_zip(url, download_dir, extract_dir):
    with contextlib.suppress(FileExistsError):
        os.mkdir(download_dir)
    urllib.request.urlretrieve(url, f"{download_dir}/update.zip")
    with zipfile.ZipFile(f'{download_dir}/update.zip', 'r') as zip_ref:
        zip_ref.extractall(download_dir)
    os.remove(f'{download_dir}/update.zip')
    for g in os.listdir(f'{download_dir}/Chronicles-of-Arclight-master'):
        os.replace(f'{download_dir}/Chronicles-of-Arclight-master/{g}', f'{download_dir}/{g}')
    shutil.rmtree(f'{extract_dir}')
    os.replace(f'{download_dir}/updater/updater.py', f'{extract_dir}/updater.py')
    os.replace(f'{download_dir}/updater/version.txt', f'{extract_dir}/version.txt')
    shutil.rmtree(f'{download_dir}')
    
def updater():
    url = 'https://raw.githubusercontent.com/Intofire-Studios/Chronicles-of-Arclight/master/updater/version.txt'
    file_path = 'updater/version.txt'
    if check_version(url, file_path):
        download_and_extract_zip('https://github.com/Intofire-Studios/Chronicles-of-Arclight/archive/refs/heads/master.zip', 'updater/download', 'updater')