from flask import Flask, request, url_for, render_template, redirect
import os
from flask_mail import Mail, Message

app = Flask(__name__)

app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")

mail = Mail(app)

@app.route("/contact") #이메일보내는 폼이 보이는 기능 구현
def contact():
    return render_template("contact.html")

@app.route("/contact/complete", methods=["GET","POST"] )
def contact_complete():
    if request.method == 'POST': # post, get
        username = request.form["name"] #form에서 이름 정보 가져오기
        email = request.form["email"]
        message = request.form["message"]

        print(username, email, message)

        #이메일 보내기 코드
        send_email(
            email,
            "문의해주셔서 감사합니다.",
            'contact_mail',
            name = username,
            message = message
        )

        return redirect(url_for("contact_complete"))
    
    return render_template("contact_complete.html")

#이메일을 보내기위한 함수 작성
def send_email(to, subject,template, **kwargs):
    msg = Message(subject, recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs) #contact_mail.txt
    msg.html = render_template(template + ".html", **kwargs) #contact_mail.html
    msg.charset = 'utf-8'
    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)

