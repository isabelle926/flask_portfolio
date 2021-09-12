# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home/')
def home():
    return render_template("home.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/about_us/')
def about_us():
    return render_template("about_us.html")

@app.route('/jobs/')
def jobs():
    return render_template("jobs.html")


@app.route('/questionnaires/')
def questionnaires():
    return render_template("questionnaires.html")

@app.route('/sign_up/')
def sign_up():
    return render_template("sign_up.html")

@app.route('/binary/')
def binary():
    return render_template("binary.html")


@app.route('/mini_labs/')
def mini_labs():
    return render_template("mini_labs.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")




@app.route('/vidhi', methods=['GET', 'POST'])
def vidhi():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("vidhi.html", name1=name)
    # starting and empty input default
    return render_template("vidhi.html", name1="World")

@app.route('/kamya', methods=['GET', 'POST'])
def kamya():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("kamya.html", name2=name)
    # starting and empty input default
    return render_template("kamya.html", name2="World")

@app.route('/kaavya', methods=['GET', 'POST'])
def kaavya():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("kaavya.html", name1=name)
    # starting and empty input default
    return render_template("kaavya.html", name1="World")

@app.route('/isabelle', methods=['GET', 'POST'])
def isabelle():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("isabelle.html", name1=name)
    # starting and empty input default
    return render_template("isabelle.html", name1="World")

@app.route('/video/')
def video():
    return render_template("video.html")






# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)


