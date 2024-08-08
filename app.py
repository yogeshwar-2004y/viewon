from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/launch')
def launch():
    return render_template('launch.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/offers')
def offers():
    return render_template('offers.html')

@app.route('/singles')
def singles():
    return render_template('singles.html')

@app.route('/couples')
def couples():
    return render_template('couples.html')

@app.route('/midnight')
def midnight():
    return render_template('midnight.html')

@app.route('/pubs')
def pubs():
    return render_template('pubs.html')

if __name__ == "__main__":
    app.run(debug=True)
