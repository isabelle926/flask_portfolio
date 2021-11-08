# import "packages" from flask
from flask import Flask, render_template, request
from algorithms.image import image_data
from pathlib import Path

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/about_us/')
def about_us():
    return render_template("about_us.html")

@app.route('/jobs/')
def jobs():
    return render_template("jobs.html")

@app.route('/internships/')
def internships():
    return render_template("internships.html")

@app.route('/summer_programs/')
def summer_programs():
    return render_template("summer_programs.html")

@app.route('/rgb/', methods=["GET", "POST"])
def rgb():
    path = Path(app.root_path) / "static" / "assets" / "images"
    return render_template('rgb.html', images=image_data(path))

@app.route('/questionnaires/')
def questionnaires():
    return render_template("questionnaires.html")

@app.route('/sign_up/')
def sign_up():
    return render_template("sign_up.html")

@app.route("/binary", methods=['GET','POST'])
def binary():
    if request.form:
        try:
            bits = request.form.get("bits")

            if request.form["picture_change"] == "Light Bulbs": # checks which button is pressed; if light bulbs button is pressed, light bulbs are the picture and vice versa
                if len(bits) != 0:
                    return render_template("binary.html", bits=int(bits), image_path_on="/static/assets/bulb_on.gif", image_path_off="/static/assets/bulb_off.png")
            if request.form["picture_change"] == "Dog Bulbs":
                if len(bits) != 0:  # input field has content
                    return render_template("binary.html", bits=int(bits), image_path_on="/static/assets/dog.png", image_path_off="/static/assets/deaddog.png")

            # starting and empty input default
        except:
            return render_template("binary.html", bits=8, image_path_on="/static/assets/bulb_on.gif", image_path_off="/static/assets/bulb_off.png")
    return render_template("binary.html", bits=8, image_path_on="/static/assets/bulb_on.gif", image_path_off="/static/assets/bulb_off.png")

@app.route('/binary_new/')
def binary_new():
    return render_template("unsigned_shift.html")

@app.route('/mini_labs/')
def mini_labs():
    return render_template("mini_labs.html")


@app.route('/colorcodes/')
def colorcodes():
    return render_template("colorcodes.html")

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

@app.route('/logicgates/')
def logicgates():
    return render_template("logicgates.html")

@app.route('/contactus/')
def contact_us():
    return render_template("contact_us.html")

@app.route('/signed_addition/')
def signed_addition():
    return render_template("signed_addition.html")

@app.route('/practice_interview/')
def practice_interview():
    return render_template("practice_interview.html")

@app.route('/registration_form/')
def registration_form():
    return render_template("registration_form.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)