from flask import Flask, render_template
app = Flask(__name__)

sites = ["facebook.com","amazon.co.uk","youtube.com","netflix.com","google.com","w3schools.com", "github.com","getbootstrap.com","webflow.com","asos.com","taobao.com","qq.com","reddit.com","yahoo.com","wikipedia.org","baidu.com"]


@app.route("/")
def hello():
    return render_template('home.html', sites=sites)

@app.route("/float")
def floatleft():
    return render_template('floatleft.html', sites=sites)

if __name__ == "__main__":
    app.run(debug=True)
