from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from loginform import LoginForm
from user import User



app = Flask(__name__, template_folder="/Users/eppy/Documents/Coding_Projects/Check-In-App/templates")
app.config['SECRET_KEY'] = "nothing"

@app.route("/", methods= ['GET','POST'])
def index():
    return render_template("index.html")


@app.route("/Login", methods = ['GET', 'POST'])
def form():
    form = LoginForm()
    return render_template("form.html", form=form)
@app.route("/CreateAccount", methods= ['GET', 'POST'])
def signup():
    user = User()
    return render_template("signup.html",user=user )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    