import smtplib
from email.mime.text import MIMEText

body = """ullam at sagittis leo, a vulputate neque. Sed vehicula maximus mi et varius. Nullam vitae libero dolor. Duis pretium odio tempus elit placerat aliquam. Phasellus eu porta magna, et dictum neque. Mauris scelerisque tristique ex maximus consequat. Nullam leo est, tincidunt ut mauris egestas, efficitur dictum mauris. Aenean eu rhoncus dolor, nec posuere libero. Mauris auctor posuere ligula dignissim semper. Nam molestie eget nisi ac suscipit. Quisque iaculis elit euismod aliquet luctus.

Donec euismod vehicula rutrum. Suspendisse tristique nibh nec justo varius, non laoreet nulla semper. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vestibulum luctus luctus mauris, in scelerisque felis laoreet eget. Ut sed lacinia eros. Ut viverra, mi non luctus aliquam, turpis lorem blandit ex, nec consectetur metus sem ac lorem. Vestibulum velit sapien, lacinia in risus sed, laoreet aliquam neque. Fusce nisi neque, viverra et ipsum a, convallis euismod est. Phasellus in enim sem. Proin imperdiet facilisis nisl sit amet placerat. Mauris lacinia tortor ut ipsum blandit ultricies. Ut tempor leo non lorem semper, ac convallis nulla scelerisque. Pellentesque a placerat velit, non dictum erat.
"""
msg=MIMEText(body)
msg['From']="email123address@gmail.com"
msg['To']="friendsemail123@gmail.com"
msg['Subject']="Email client test! Lorem Ipsum sent."

server=smtplib.SMTP("smtp.gmail.com",587)

server.starttls()

server.login("email123address@gmail.com", "password")

server.send_message(msg)
print("Email sent")

server.quit()
