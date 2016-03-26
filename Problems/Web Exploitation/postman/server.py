from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def index():
    if not "Google Ultron" in request.headers.get('User-Agent'):
        return "<h1>Error: Unauthorized browser " + request.headers.get('User-Agent') + " detected. Only users of \"Google Ultron\" may access this page."
    elif not request.headers.get('SpecialAuth'):
        return "<h1>Error: \"SpecialAuth\" header not set to my name </h1>"
    elif not "Kyle" in request.headers.get('SpecialAuth'):
        return "<h1>Error: \"SpecialAuth\" header not set to my name </h1>"
    elif not request.headers.get('referer'):
        return "<h1>Error: This site must be accessed from \"kyleisacoolguy.org\"</h1>"
    elif not "kyleisacoolguy.org" in request.headers.get('referer'):
        return "<h1>Error: This site must be accessed from \"kyleisacoolguy.org\"</h1>"
    else:
        return "<h1>Sucesfully Authenticated! Your flag is:lasactf{h3aders_ar3_c00l}</h1>"
if __name__ == '__main__':
    app.run(host='0.0.0.0')
