import subprocess
import time
import os


# For users to change
CURRENT_APPOINTMENT_DATE = "March 11, 2019"
CURRENT_VAC_DATE = "February 25, 2019"
COOKIE = "BrowserId=q8fiO_ccSrKRAE7E7e33xg; __utmc=1; oinfo=c3RhdHVzPUFDVElWRSZ0eXBlPTYmb2lkPTAwREMwMDAwMDAwUGh1UA==; autocomplete=1; lloopch_loid=00DC0000000PhuP; lloopch_lpid=060C0000000QwL9; oid=00DC0000000PhuP; apex__aa-time=Yfy4isvgW4Z8lOc8c5XgkA_3D_3D; sid_Client=h00000GQDFK0000000PhuP; clientSrc=103.204.169.224; inst=APP_0h; __utma=1.210204694.1550206513.1550670395.1550683582.17; __utmz=1.1550683582.17.13.utmcsr=ustraveldocs.com|utmccn=(referral)|utmcmd=referral|utmcct=/in/in-niv-typeb1b2.asp; __utmt=1; sid=00DC0000000PhuP!ARwAQOi.bFB5.9KF9vho6mNHd2lRUGwPNVvNDu5_0wykH6g_gW8gga.r5_jaj2YrOyt2McXB3CcNst1AXg_pwsBFOtEyNH5E; __utmb=1.2.10.1550683582"

# For developer usage only
AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36"
SED_COMMAND = "'s/First Available Appointment Is \w* //p'"


def reqModprobe():
    reqCmd = "sudo modprobe pcspkr;"
    subprocess.Popen(reqCmd,
                     shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT).stdout.read()
    time.sleep(15)


def awesomeBeep():
    while True:
        beepCmd = "beep -f 659 -l 460 -n -f 784 -l 340 -n -f 659 -l 230 -n -f 659 -l 110 -n -f 880 -l 230 -n -f 659 -l 230 -n -f 587 -l 230 -n -f 659 -l 460 -n -f 988 -l 340 -n -f 659 -l 230 -n -f 659 -l 110 -n -f 1047-l 230 -n -f 988 -l 230 -n -f 784 -l 230 -n -f 659 -l 230 -n -f 988 -l 230 -n -f 1318 -l 230 -n -f 659 -l 110 -n -f 587 -l 230 -n -f 587 -l 110 -n -f 494 -l 230 -n -f 740 -l 230 -n -f 659 -l 460"
        subprocess.Popen(beepCmd,
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT).stdout.read()
        time.sleep(15)


def checkAppointmentTime():
    print("Started...")
    while True:
        time.sleep(60)
        cmd = "curl -X GET -H 'Cookie: " + COOKIE + \
            "' -H 'Host: cgifederal.secure.force.com' -H 'Referer: https://cgifederal.secure.force.com/apex/LoginLandingPage' -H 'User-Agent: " + \
            AGENT + "' -s -i 'https://cgifederal.secure.force.com/applicanthome' | sed -n -e" + SED_COMMAND
        date = subprocess.Popen(cmd,
                                shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT).stdout.read()
        try:
            strDate = date.strip().decode("utf-8")
            availableDate = time.strptime(strDate, "%B %d, %Y.")
            # print(availableDate)
        except:
            print(
                "Getting incorrect date format: %s, please check the cookie variable" % date)
            awesomeBeep()

        currentDate = time.strptime(
            CURRENT_APPOINTMENT_DATE, "%B %d, %Y")
        vacDate = time.strptime(
            CURRENT_VAC_DATE, "%B %d, %Y")

        if currentDate > availableDate and vacDate < availableDate:
            print(date.strip())
            awesomeBeep()


if __name__ == "__main__":
    reqModprobe()
    checkAppointmentTime()
