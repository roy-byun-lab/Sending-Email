#HTML로 보내기
def send_email(subject, html_path, ID, PWD, receiver_list):
    """
    subject: 메일 제목
    body: 메일 본문
    ID: 보내는 사람의 이메일 주소
    PWD: 보내는 사람의 이메일 비밀번호
    receiver_list: 받는 사람들의 이메일 주소
    """
    html = open(html_path, 'r', encoding='utf-8')
    msg = MIMEMultipart("related")
    msg['From'] = ID
    msg['To'] = ', '.join(receiver_list)
    msg['Subject'] = subject

    msg.attach(MIMEText(html.read(), "html"))

    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(ID, PWD)
    smtp_server.sendmail(ID, receiver_list, msg.as_string())
    smtp_server.quit()


ID = '보내는사람@gmail.com'
PWD = 'ABCDEFGHIJKLMNOP'
receiver_list = ['보내는사람@gmail.com']
subject = "Happy Birthday!!"
html_path = './Cake.html'