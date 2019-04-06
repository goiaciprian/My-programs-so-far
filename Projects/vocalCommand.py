import speech_recognition as sr
import win10toast
from multiprocessing import Process

# constant
NOTIFICATION = win10toast.ToastNotifier()


def getCommand():  # gets input through the mic and convert it to text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Spune ceva :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="ro-RO")
            print("Ai spus : {}".format(text))
            return text
        except:
            print("Scuze, nu am putut intelege ce ai zis.")
            return None


def show(command: str):  # shows different notifications
    if command == "Google":
        NOTIFICATION.show_toast("Vocal Command", "Se deshide Google...")
    elif command == "epic":
        NOTIFICATION.show_toast(
                "Vocal Command", "Se deshide Epic Games...")
    elif command == "ieșire":
        NOTIFICATION.show_toast("Vocal Command", "Programul se inhide ...")


def openGoogle():  # open google
    import webbrowser
    webbrowser.open("www.google.ro")


def openEpic():  # open epic games launcher
    import os
    os.startfile(
                "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe")


def iesire():  # exits
    from sys import exit
    exit(0)


if __name__ == "__main__":  # Only when the sript is runed

    running = True
    runTimes = 0
    while running and runTimes < 5:
        text = getCommand()
        if text == 'Google':
            Process(target=show('Google')).start()
            Process(target=openGoogle()).start()
        elif text == 'epic':
            Process(target=show('epic')).start()
            Process(target=openEpic()).start()
        elif text == "ieșire":
            Process(target=show('ieșire')).start()
            Process(target=iesire()).start()
        else:
            import time
            runTimes += 1
            time.sleep(3)
