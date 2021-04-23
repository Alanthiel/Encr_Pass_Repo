#!/usr/bin/python3

import requests
from requests.exceptions import ConnectionError

if __name__ == "__main__":
    print("Downloading Software Management Module from GitHub.....  ", end='')
    try:
        manager = requests.get("https://raw.githubusercontent.com/Alanthiel/Encr_Pass_Repo/master/Manager.py")
        if manager.status_code == 200:
            with open("Manager.py", 'w') as man:
                man.write(manager.text)
                man.close()
        elif manager.status_code % 500 > 0:
            print('\033[1;31;49m✗\n\033[0;0mServerside Error Please Try again later, Aborting')
            exit()
        elif manager.status_code % 400 > 0:
            print('\033[1;31;49m✗\n\033[0;0mClient Error, Ensure Remote_Rescue.py is at the latest version. Else '
                  'Please raise an Issue at "https://github.com/Alanthiel/Encr_Pass_Repo/issues"')
            exit()

    except ConnectionError:
        print("\033[1;31;49m✗\n\033[0;0mConnection Error, Please Check your Internet Connection.....   Exiting")
        exit()
    print("\033[1;32;49m ✓")

    import Manager

    print('\033[0;0mVerifying Software Intregrity..... ', end='')

    verify_result = Manager.verify_integrity(remote_priority=True, fallback=False)

    if verify_result is Manager.Errors.Con_Fail:
        print("\033[1;31;49m✗\n\033[0;0mConnection Error, Please Check your Internet Connection.....   Exiting")
        exit()

    if verify_result is True:
        print("\033[1;32;49m ✓\n Software Intregrity Verified from Remote Metadata. Software is Safe to use")
        exit()

    if verify_result == KeyboardInterrupt:
        print("\033[1;31;49m✗\n\033[0;0mKeyboard Interrupt Signal Received...... Exiting")
        exit()

    if verify_result is False:
        print("\033[1;33;49m ✓\n\033[1;31;49mSoftware Corrupted or Tampered with.")

        if input("Rescue by Update? (y?)").lower() == 'y':
            print("Updating Software...... ", end='')
            rescue = Manager.update()

            if rescue == Manager.Errors.Con_Fail:
                print("\033[1;31;49m✗\n\033[0;0mConnection Error, Please Check your Internet Connection.....   Exiting")
                exit()

            else:
                print("\033[1;32;49m ✓\n\033[0;0mSoftware Successfully Updated. Software Safe To Use")
