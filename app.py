import os
import json
import collections
import bcrypt
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myrecipedb'
app.config["MONGO_URI"] = 'mongodb://root:r00tp4ss...@ds219832.mlab.com:19832/myrecipedb'

mongo = PyMongo(app)


#------------------------------------HOME---------------------------------------


@app.route('/')
def index():
    if 'username' in session:
        
        username = session['username']
        _recipes = mongo.db.recipes.find()
        recipe_list = [recipe for recipe in _recipes]
        return render_template('home.html', recipes=recipe_list, username=username)

    return render_template('login.html')


#-----------------------------USER LOGIN/LOGOUT---------------------------------


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


#-------------------------------RECIPE STUFF------------------------------------


@app.route('/create_recipe', methods=['POST', 'GET'])
def create_recipe():
    if 'username' in session:
        
        username = session['username']
        
        if request.method == 'POST':
            ingredients_arr = {}
            instructions_arr = {}
            recipe = mongo.db.recipes
            form_data = request.form.to_dict(flat=True)

            for key, value in form_data.items():
                if key.startswith('instruction'):
                    instructions_arr[key.replace("instruction","")] = value.encode('utf-8')
                if key.startswith('ingredient'):
                    ingredients_arr[key.replace("ingredient","")] = value.encode('utf-8')

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

            return redirect(url_for('index')) #redirect after successful recipe creation

        return render_template('create_recipe.html', categories=mongo.db.categories.find().sort("category_name", 1), username=username)

    return render_template('login.html')

@app.route('/delete/<recipe_id>')
def delete(recipe_id):
    username = session['username']
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for('index'))
    
@app.route('/recipe/<recipe_id>') # Page to view a Recipe
def recipe(recipe_id):
    if 'username' in session:
        
        username = session['username']
        show_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        instructions_list = show_recipe['instructions']
        ingredients_list = show_recipe['ingredients_list']
        return render_template('recipe.html', recipe=show_recipe, categories=mongo.db.categories.find(), 
                                ingredients_list=ingredients_list, instructions_list=sorted(instructions_list.items()))

    return render_template('login.html')
    
@app.route('/recipes')
def recipes():
    if 'username' in session:
        
        username = session['username']
        _recipes = mongo.db.recipes.find().sort("name", 1)
        recipe_list = list(_recipes)
        return render_template('recipes.html', recipes=recipe_list, username=username)

    return render_template('login.html')

@app.route('/category/<category>')
def category(category):
    if 'username' in session:
        
        username = session['username']
        category = mongo.db.categories.find({"category_name": category}) #search categories in categories db
        cat_list = list(category) #create list out of above answer
        fancy = cat_list[0]['fancy_name'] #target fancy cat name
        _recipes = mongo.db.recipes.find({"category": fancy}) #category=fancy name
        recipe_list = list(_recipes)
        return render_template('category.html', username=username, recipes=recipe_list, cat=fancy)
    
    return render_template('login.html')


#--------------------------------OTHER PAGES------------------------------------


@app.route('/user/<username>')
def user(username):
    if 'username' in session:
        
        username = session['username']
        find_user = mongo.db.users.find_one({"username": username})
        find_recipes = mongo.db.recipes.find({"author": username})
        recipe_list = list(find_recipes)
        return render_template('user.html', username=username, user=find_user, recipes=recipe_list)
        
    return render_template('login.html')
    
@app.route('/about')
def about():
    if 'username' in session:
        username = session['username']
        return render_template('about.html', username=username)
    return render_template('about.html')


#-------------------------------------------------------------------------------


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(
        host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True
        )