from flask import Flask, render_template, make_response
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
    
@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run()
