from flask import Flask, render_template
app = Flask(__name__)

sites = ["facebook.com","amazon.co.uk","youtube.com","netflix.com","google.com"]


@app.route("/")
def hello():
    return render_template('home.html', sites=sites)

if __name__ == "__main__":
    app.run(debug=True)
