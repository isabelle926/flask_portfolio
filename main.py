# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


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
            return render_template("kamya.html", name1=name)
    # starting and empty input default
    return render_template("kamya.html", name1="World")

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

@app.route('/Videos/')
def Videos():
    return render_template("Videos.html")




# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)


