import contextlib
import urllib.request
import os
import zipfile
import shutil
import time

os.system("cls||clear")
try:
    with contextlib.suppress(FileExistsError):
        os.mkdir('updater/download')
    urllib.request.urlretrieve("https://github.com/Intofire-Studios/Chronicles-of-Archlight/archive/refs/heads/master.zip", "updater/download/update.zip")
    with zipfile.ZipFile('updater/download/update.zip', 'r') as zip_ref:
        zip_ref.extractall('updater/download/')
    os.remove('updater/download/update.zip')
    for g in os.listdir('updater/download/Chronicles-of-Archlight-master'):
        os.replace(f'updater/download/Chronicles-of-Archlight-master/{g}', f'updater/download/{g}')
    shutil.rmtree('updater/download/Chronicles-of-Archlight-master')
    shutil.rmtree('updater/download/updater')
    shutil.rmtree('extensions')
    shutil.rmtree('modules')
    os.remove('.gitignore')
    os.remove('main.py')
    os.remove('README.md')
    os.remove('requirements.txt')
    os.remove('start.bat')
    os.remove('start.sh')
    for g in os.listdir('updater/download'):
        os.replace(f'updater/download/{g}', g)

    for percent in range(100):
        s = f"[{(percent // 10) * '■'}"
        s += f"{(10 - (percent // 10)) * '○'}] "
        s += f"{percent}"
        print('Downloading the update... ', s, end="\r")
        time.sleep(0.1)

    os.system("cls||clear")
    print('Update completed. Launching the game...')
except Exception as e:
    print(f"The game cannot be updated.\nError: {e}\n\nLaunching tha game...")
time.sleep(3)
os.system('python main.py')