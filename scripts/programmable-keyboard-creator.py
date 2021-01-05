from sh import xinput
from subprocess import Popen

try:
    macro_keyboard = int(xinput("list", "--id-only", "SEM HCT Keyboard"))
except:
    # keyboard not connected
    pass
else:
    xinput("float", macro_keyboard)
    for line in xinput("test", macro_keyboard, _iter=True):
        try:
            key = int(line.split()[2])
            status = line.split()[1]
        except:
            # keyboard not connected
            pass
        else:
            print(key, status)
            if key == 42 and status == 'press':
                Popen('nemo .'.split())

