import os
from time import sleep
from extensions.cmdClear import consoleClear
import webbrowser

def saveCheatCheck(pathsave, path):
    if os.path.exists(path):
        realtime = os.path.getmtime(path)
        if not os.path.exists(pathsave):
            with open(pathsave, "w+") as newsave:
                newsave.write(str(realtime))
        with open (pathsave) as f:
            lasttime = f.read()
        if float(realtime) != float(lasttime):
            consoleClear()
            print("Heh, don't try to modify your saves...")
            sleep(4)
            try:
                os.system("extensions\secret.gif")
            except:
                webbrowser.open_new_tab('https://youareanidiot.cc')
            os.remove(path)
            exit()
            