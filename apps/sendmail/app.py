from flask import Flask, request , url_for,make_response, render_template, redirect
import urllib.parse

app = Flask(__name__)

@app.route('/contact') #이메일보내는 폼이 보이는 기능 구현
def contact():
    return render_template('contact.html')

@app.route('/contact/complete')
def contact_complete():
    if request.method == 'POST': #(방금 들어온 요청에) 너 POST야?
        #이메일 보내기 코드 작성

        return redirect('contact_complete') #강제로 특정 위치로 보내버리기 , 엔드포인트
    return render_template('contact_complete.html') #메일 접수 완료한 화면 구성 html 파일 보여줄게 
 






if __name__ == "__main__":
    app.run(debug=True)