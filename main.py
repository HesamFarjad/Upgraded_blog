from flask import Flask, render_template
import requests

response = requests.get(url='https://api.npoint.io/674f5423f73deab1e9a7')
data = response.json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", data=data)


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/post/<int:andis>')
def show_post(andis):
    requested_post = None
    for j in data:
        if j['id'] == andis:
            requested_post = j
    return render_template('post.html', requested_post=requested_post)


if __name__ == '__main__':
    app.run(debug=True)











