import smtplib

s = smtplib.SMTP('smtp.gmail.com',587)
toList = ['nat.tiutiunnyk@gmail.com']
msg = 'Hello, this is test'

s.sendmail('nat.tiutiunnyk@gmail.com',toList,msg)