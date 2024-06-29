#일반 Plain Text로 보내기
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, ID, PWD, receiver_list):
    """
    subject: 메일 제목
    body: 메일 본문
    ID: 보내는 사람의 이메일 주소
    PWD: 보내는 사람의 이메일 비밀번호
    receiver_list: 받는 사람들의 이메일 주소
    """

    msg = MIMEText(body)
    msg['From'] = ID
    msg['To'] = ', '.join(receiver_list)
    msg['Subject'] = subject

    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # 465는 포트넘버 (수정필요없음)
    smtp_server.login(ID, PWD)
    smtp_server.sendmail(ID, receiver_list, msg.as_string())
    smtp_server.quit()


ID = '보내는사람@gmail.com'                     # 발신자 지메일 주소
PWD = 'ABCDEFGHIJKLMNOP'                      # 발신자 비밀번호
receiver_list = ['보내는사람@gmail.com']        # 수신자 리스트
subject = "자동 이메일 발송 테스트"             # 이메일 제목
body = "Python으로 이메일 보내기. 성공!"        # 이메일 본문

send_email(subject, body, ID, PWD, receiver_list)