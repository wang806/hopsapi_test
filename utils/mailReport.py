# coding:utf-8
import os
import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import configparser as cparser
from utils.logger import Log
logger = Log(logger='mail').get_log()

# 读取配置
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + '/config.ini'
cf = cparser.ConfigParser()
cf.read(file_path, encoding='utf-8')



class MailReport:
    def __init__(self):
        # 从config.ini文件读取邮件参数
        self.smtpserver = cf.get('email', 'smtpserver')
        self.port = cf.get('email', 'port')
        self.sender = cf.get('email', 'sender')
        self.psw = cf.get('email', 'psw')
        self.receivers = cf.get('email', 'receiver')
        self.receiver = json.loads(self.receivers)
        print(self.smtpserver, self.port, self.sender, self.psw, self.receiver)

    def sendReport(self):
        # ----------发送邮件 - 编辑邮件内容------
        report_dir = './report/'
        lists = os.listdir(report_dir)
        # lists.sort(key=lambda filename: os.path.getctime(report_dir+filename))
        lists.sort(key=lambda fn: os.path.getmtime(report_dir + fn))
        report_file_path = os.path.join(report_dir, lists[-1])

        with open(report_file_path, "rb") as fp:
            mail_body = fp.read()
        msg = MIMEMultipart()
        msg["from"] = self.sender  # 发件人
        msg["to"] = ";".join(self.receiver)  # 多个收件人list转str
        msg["subject"] = "cms_api-测试报告"  # 主题
        # 正文
        body = MIMEText(mail_body, "html", "utf-8")
        msg.attach(body)

        # 附件
        # att = MIMEText(mail_body, "base64", "utf-8")
        # att["Content-Type"] = "application/octet-stream"
        # att["Content-Disposition"] = 'attachment; filename="test_report.html"'
        att = MIMEApplication(open(report_file_path, 'rb').read())
        att.add_header('Content-Disposition', 'attachment', filename=os.path.basename(report_file_path))
        msg.attach(att)
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtpserver)                      # 连服务器
            smtp.login(self.smtpserver, self.psw)
        except:
            smtp = smtplib.SMTP_SSL(self.smtpserver, self.port)
            smtp.login(self.sender, self.psw)                       # 登录
        smtp.sendmail(self.sender, self.receiver, msg.as_string())  # 发送
        logger.info('report mail send ok')
        smtp.quit()                                       # 关闭连接
