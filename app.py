from flask import Flask, render_template, make_response, request
import csv

app = Flask(__name__, static_folder='static')


@app.route("/styles")
def styles():
    response = make_response(render_template("/static/styles.css"))
    response.headers["Cache-Control"] = "no-cache"
    return response


@app.route("/script")
def script():
    response = make_response(render_template("/static/script.js"))
    response.headers["Cache-Control"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/courses")
def courses():
    return render_template('courses.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['fullName']
        email = request.form['email']
        message = request.form['message']
        with open('form_data.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, message])
    return render_template('contact.html')


if __name__ == "__main__":
    app.run()
