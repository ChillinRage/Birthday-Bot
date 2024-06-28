# Birthday Bot
 An automated bot to send wishes to your contacts on their birthday.

An executable file for the birthday bot is now available to download.
The zip file comes with `Birthday Bot.exe` main file, and `data` folder with the relevant data files.
<br>
**Note**: this app only works with gmail accounts (only for the bot account) as it uses the gmail server to login and send emails. Your main email need not be a gmail account as its role is to only receive emails (reminder of your contacts' birthday).

### Set-up
1. Download and unzip the folder (to somewhere on your device)
2. Open the folder and go to `_internal`.
3. Check the `data` folder if it contains 3 files: `account.txt`, `data.csv`, and `logbook.txt`. (If any of them isn't there, you can download the specific files from this repository)
![image](https://github.com/ChillinRage/Birthday-Bot/assets/73763719/66e8464f-669e-49a1-b655-578971c245a8)

4. Open `account.txt` file and replace the 3 lines inside with `YOUR_EMAIL`, `BOT_EMAIL`, and `PASSWORD`* respectively. (Ensure that they are separated by a line like in the sample pic)
![image](https://github.com/ChillinRage/Birthday-Bot/assets/73763719/bb80e6c8-0d7b-476f-b710-9c3090e2131c)

5. Close the file and open `data.csv` (via notepad if you do not have other csv file viewer). The first line contains the header fields.
6. Enter all the relevant contact details in that folder in the format specified by the headers. Ensure that there is an empty line at the end of the file (Sample pic shown below for 2 contacts)<br>
![image](https://github.com/ChillinRage/Birthday-Bot/assets/73763719/374d3764-c670-4c9e-bb97-9888c1c6b416)
Note: `date` is in the following format `DAY/MONTH/YEAR`.
7. Add the exe executable file to task scheduler in your system and set the trigger to daily or "at Log on".7
8. You're set (probably).

### NOTE ABOUT PASSWORD
The password you should use is NOT the password you used to conventionally login to the google account. You should use its **App Password** instead [see link here for more information](https://stackoverflow.com/questions/70261815/smtplib-smtpauthenticationerror-534-b5-7-9-application-specific-password-req).