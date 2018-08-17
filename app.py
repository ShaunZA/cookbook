import os
import json
import collections
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myrecipedb'
app.config["MONGO_URI"] = 'mongodb://root:r00tp4ss...@ds219832.mlab.com:19832/myrecipedb'

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        _recipes = mongo.db.recipes.find()
        recipe_list = [recipe for recipe in _recipes]
        return render_template('home.html', recipes=recipe_list)

    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'username' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid Username or Password'

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        active_user = users.find_one({'name' : request.form['username']})

        if active_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({
                'username' : request.form['username'], 
                'first_name' : request.form['first_name'], 
                'last_name' : request.form['last_name'], 
                'email' : request.form['email'], 
                'password' : hashpass, 
                'created_recipes' : []
            })
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')

@app.route('/create_recipe', methods=['POST', 'GET'])
def create_recipe():
    if 'username' in session:
        
        if request.method == 'POST':
            ingredients_arr = {}
            instructions_arr = {}
            recipe = mongo.db.recipes
            form_data = request.form.to_dict(flat=True)
            
            for key, value in form_data.items():
                if key.startswith('instruction'):
                    instructions_arr[key.replace("instruction","")] =  str(value)
                if key.startswith('ingredient'):
                    ingredients_arr[key.replace("ingredient","")] =  str(value)
            
            recipe.insert({
                'name' : request.form['recipename'],
                'desc' : request.form['recipedesc'],
                'category' : request.form.get('cat_select'),
                'ingredients_list' : ingredients_arr,
                'instructions' : instructions_arr,
                'prep_time' : request.form['prep_time'],
                'cook_time' : request.form['cook_time'],
                'img_url' : request.form['img_url'],
                'author' : session['username']
            })
            
            return 'Done!'
        
        return render_template('create_recipe.html', categories=mongo.db.categories.find())
    
    return render_template('login.html')

@app.route('/recipe')
def recipe():
    return render_template('recipe.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True
        )