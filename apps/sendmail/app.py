from flask import Flask, request , url_for,make_response, render_template
import urllib.parse

app = Flask(__name__)








if __name__ == "__main__":
    app.run(debug=True)