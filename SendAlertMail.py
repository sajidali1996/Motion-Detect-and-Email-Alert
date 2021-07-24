import smtplib
#this block of code is for time  stamping
from datetime import datetime
stamp=datetime.now();
time_stamp=stamp.strftime("%H:%M:%S")
date_stamp=stamp.strftime("%d/%m/%y")
#print("Date = ",date_stamp)           # for testing of code
#print("Time = ",time_stamp)           # for testing of code

sender_email_address='abc@yahoo.com'       
receiver_email_address='xyz@gmail.com'
subject='Subject: Motion Detected at home \n\n'
content='Mr. Sajid! \nSomeone just entered your apartment at: \n' + time_stamp+ ' on ' + date_stamp +'\n\n'
footer = '- This is your Security System'
passcode = 'jkdukdbewuebsdhjdskj'
conn=smtplib.SMTP_SSL('smtp.mail.yahoo.com',465)
conn.ehlo()
conn.login(email_address,passcode)
conn.sendmail(sender_email_address,receiver_email_address,subject+content+footer)
conn.quit()
print('Email Alert Sent')
