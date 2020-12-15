# Encr_Pass_Repo V0.3.2

Encrypted Local Password Manager:

- Content stored in a local SQL Database using sqlite3 encrypted using PyCryptodome Module.
- Manipulation of Database occurs through loading of database into virtual memory prior to encryption or decryption in order to prevent storage of unlocked Database locally.
- 2 Phase Database Commits - Internal Changes to Virtual Memory, Final Commits to Physically Stored Database
- Encryption used is AES 256bit Encryption in GCM mode with MAC Tag Verification to detect tampering of database. 

**Please Note: Due to Password Databases stored Locally as Files, This approach is susceptible to Brute Force Attacks, Man-In-the-Middle attacks or Phishing Attacks**

In Order to Protect against these for any users of this Project for personal use, Please follow the Following Guidelines 

- Use a Strong Password: Use Passwords with Special Characters, Uppercase Lower Case, Numbers (or) follow: [PasswordGuide](https://xkcd.com/936/), [How-To-Geek](https://www.howtogeek.com/195430/how-to-create-a-strong-password-and-remember-it/)
- Check the Strength of your Password using either [Password Strength Meter](http://www.passwordmeter.com/) or [Password Test](https://www.my1login.com/resources/password-strength-test/)
- Make Sure the Software or Code you are using to open your Databases are obtained from a Trusted Source, example the Project Git Page [Encr_Pass_Repo](https://github.com/Alux-Alpha/Encr_Pass_Repo)
- Check the Integrity of the Software Using SHA CheckSums of the files. Refer to the Guide Below

### Checking the Integrity:

**Automated Script Check:**

- Download the Latest version of `Code_Management.py`
- Copy the script to your Software Folder
- Run the script
```
    $ ./Code_Management.py
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
    029aa7bc2733ec9b3b7f9ea377c09ebe6688da677c335480bb41340d325cc7ec  Auth.py
    873636cce8697b9a0605e3ba561c1ba92ed11588978df05476cdccd72d2d55f4  DBMan.py
    a6a07e133ea671efbcbd41736ee028c796f3a10d7a4391a1f5803072b49f373e  Manager.py
    2b720f5bcaa55054fd36e20908f18a0d5571a6e74f652eeba535b96478514d17  Remote_Rescue.py
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

- [ ] Software Management Module Integration
- [ ] Design Password Meter   

V0.3.5

- [ ] Redesign Physical Write / Write Operations around Private Virtual Files with passthroughs to Database for Security
- [ ] Design { Virtual File - Sqlite3 connection } pathway, Refer infile TODOs  
- [ ] Developing SQL Management System
- [ ] Developing Initial CLI Interface  

V1:

- [ ] Design GUI
- [ ] Optimize Encryption / Decryption Pathways
- [ ] Optimize File / DB Management


V2:

- [ ] Design Time Based 2FA Authentication


Developed by Alux-Alpha ( Nehal.GS@protonmail.ch )
