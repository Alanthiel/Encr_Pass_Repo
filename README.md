# Encr_Pass_Repo V0.4.1p

Encrypted Local Password Manager:

- Content stored and encrypted using PyCryptodome Module.
- Manipulation of Database occurs through loading of database into virtual memory prior to encryption or decryption in order to prevent storage of unlocked Database locally.
- Encryption used is AES 256bit Encryption in GCM mode with MAC Tag Verification to detect tampering of database. 

**Please Note: Due to Password Databases stored Locally as Files, This approach is susceptible to Brute Force Attacks, Man-In-the-Middle attacks or Phishing Attacks**

In Order to Protect against these for any users of this Project for personal use, Please follow the Following Guidelines 

- Use a Strong Password: Use Passwords with Special Characters, Uppercase Lower Case, Numbers (or) follow: [How-To-Geek](https://www.howtogeek.com/195430/how-to-create-a-strong-password-and-remember-it/)
- Check the Strength of your Password using either [Password Strength Meter](http://www.passwordmeter.com/) or [Password Test](https://www.my1login.com/resources/password-strength-test/)
- Make Sure the Software or Code you are using to open your Databases are obtained from a Trusted Source, example the Project Git Page [Encr_Pass_Repo](https://github.com/Alux-Alpha/Encr_Pass_Repo)
- Check the Integrity of the Software Using SHA CheckSums of the files. Refer to the Guide Below

### Checking the Integrity:

**Automated Script Check:**

**Please Note: Remote-Recuse is temporarily down due to critical issues with intregrity module. Will be reimplemented port rework**

- Download the Latest version of `Remote_Rescue.py`
- Copy the script to your Software Folder
- Run the script
```
    $ ./Remote_Rescue.py
```
- Follow the Onscreen Steps to automatically Verify and/or Rectify your copy of the Software

*Please Note: Code_Management.py to be integrated as Software Management Module Next Update*

**Manual Check:**
For Linux/Mac Users:

- Open your preferred Terminal
- Navigate to your Software Folder:
```  
     $ cd /path/to/Encr_Pass_Repo
```    
- Run SHA256 CheckSum:
```
    $ sha256sum *
```
- Verify the SHA256 sum, i.e. Output with the following, esp the provided string of digits and numbers
```
    c3ac5e98f5a5b262c01e802d1466dcf608eed24b632034a043d31db099769dba  Auth.py
    dd54bcb81f660c085eca5018eca8a05c3b86ca65bc6b5e02d75ee24722a899bb  DBMan.py
    3c8cf33c3a264c4e8d9b0f0e389cb7aff2053f3e936fff28f8b6d6df682504a7  Manager.py
    da28467bb1e79ea35360ee9c29eda2417522bd5dc6a72d2f9129ba71cd2d0e64  Remote_Rescue.py
```
- **Please Note**, If you are Running A different Version the Above Hashes will vary, Please Refer the Meta.json or Employ the `Code_Management.py` script.
- **Please Note**, If Remote_Rescue.py doesnt show up in your results, do not worry as `Remote_Rescue.py` is only a `Rescue_Script` and not a dependency of the software.
- Will Update the Above CheckSums with subsequent Commits:
    - Current Commit : `13 December 2020, 00:46 AM (IST)`

- Ensure the Date on the  Commit Date and Time on the Readme.md file and the Version Number of your edition is Same as the [GitHub Page](https://github.com/Alux-Alpha/Encr_Pass_Repo)

### In Progress:

V0.3.2

- [x] ~~Implement Credentials Class~~
- [x] ~~Design Initial Encryption System~~
- [x] ~~Design Data Bundles~~ 
- [x] ~~Software Integrity Check using File Hashes Implemented~~
- [x] ~~Software Management Module Implemented~~

V0.3.3

- [x] ~~Software Management Module Integration~~
- [ ] Design Password Meter   

V0.3.5

- [ ] Implement Json based Pass-store
- [ ] Rework Authentication Module
- [ ] Rework Intregrity Module
- [ ] Implement Initial CLI Interface  

V1:

- [ ] Design GUI

Developed by Alanthiel ( Nehal.GS@protonmail.ch )
