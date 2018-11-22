from flask import Flask
from flask import render_template
from database import *
from flask import Flask, render_template, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'


app = Flask(__name__)

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)

@app.route('/cats/<int:id>')
def catbook_profile(id):
	cat = get_cat(id)
	return render_template('cat.html',cat = cat)


@app.route('/addcat', methods=['GET', 'POST'])
def homepage():
    print("###" * 100)
    if request.method == 'GET':
        return render_template("addcat.html")
    else:
    	create_cat(request.form['firstname'])
    	return render_template("new_cat.html")


@app.route('/new_cat')
def newcat():
	new_cat = create_cat()
	return render_template("new_cat.html")

if __name__ == '__main__':
   app.run(debug = True)
