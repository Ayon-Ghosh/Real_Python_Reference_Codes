from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/<name>')
def home(name):
	return render_template("index.html", content = name)

@app.route('/<name>')
def user(name):
    return f'Hello {name}!'

@app.route('/hello')
def hello():
    return render_template('hello.html')    

@app.route('/list')
def listnames():
	return render_template('list.html', content = ['Ayon', 'Rivan','Koyel'])
# redirecting to a page which takes argument. If I would have typed admin instead of admin!
# i would be redirected to /admin page again which would result in error   
#the difference /admin/ and /admin is in the browser u can either type /admin/ or/admin when u use/admin/ in code
#@app.route('/admin/')
#def admin():
#    return redirect(url_for("user", name = "admin!"))

if __name__ == "__main__":
	app.run()