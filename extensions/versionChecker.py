import contextlib
import requests
import urllib.request
import os
import zipfile
import shutil
import time

def versionChecker():
    try:
        info = requests.get('https://raw.githubusercontent.com/Intofire-Studios/Chronicles-of-Archlight/master/extensions/version.txt')
        with open('extensions/version.txt', 'r') as f:
            curver = f.read()[9:-1]
        ver = int(str(info.content)[11:-3].replace('.', ''))
        curver = int(curver.replace('.', ''))
        if ver > curver:
            return 1
        elif ver < curver:
            return 2
        else:
            return 0
    except Exception:
        return 0

def updaterChecker():
    try:
        info = requests.get('https://raw.githubusercontent.com/Intofire-Studios/Chronicles-of-Archlight/master/updater/version.txt')
        with open('updater/version.txt', 'r') as f:
            curver = f.read()[9:-1]
        ver = int(str(info.content)[11:-3].replace('.', ''))
        curver = int(curver.replace('.', ''))
        if ver > curver:
            updater()
    except Exception:
        return 0

def updater():
    try:
        with contextlib.suppress(FileExistsError):
            os.mkdir('updater/download')
        urllib.request.urlretrieve("https://github.com/Intofire-Studios/Chronicles-of-Archlight/archive/refs/heads/master.zip", "updater/download/update.zip")
        with zipfile.ZipFile('updater/download/update.zip', 'r') as zip_ref:
            zip_ref.extractall('updater/download/')
        os.remove('updater/download/update.zip')
        for g in os.listdir('updater/download/Chronicles-of-Archlight-master'):
            os.replace(f'updater/download/Chronicles-of-Archlight-master/{g}', f'updater/download/{g}')
        os.remove('updater/updater.py')
        os.replace('updater/download/updater/updater.py', 'updater/updater.py')
        os.replace('updater/download/updater/version.txt', 'updater/version.txt')
        shutil.rmtree('updater/download')
    except Exception as e:
        with contextlib.suppress(Exception):
            shutil.rmtree('updater/download')
updaterChecker()