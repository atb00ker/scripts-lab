#!/bin/python3
# Application for getting early US visa interview:
# The tool will Scrape the CGI website and check
# available date before the current appointment date,
# if a date is available, the program will beep.

# NOTE: SET THESE GLOBAL VARIABLES BEFORE USE
# COOKIE: After you login, there is a `cookie`
#         header send in your request, paste
#         the value of that variable here.
# CURRENT_APPOINTMENT_DATE: Date you've currently have for embassy.
# CURRENT_VAC_DATE: Date you current have for VAC appointment.

import subprocess
import time
import os


# For users to change
CURRENT_APPOINTMENT_DATE = "March 22, 2019"
CURRENT_VAC_DATE = "March 11, 2019"
COOKIE = ""

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
