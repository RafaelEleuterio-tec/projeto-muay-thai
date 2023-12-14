from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])

@app.route('/index')
def index():
    return render_template("/index.html")

@app.route("/")
def homepage():
    return render_template("/homepage.html")

# coloca site no ar
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
    
    