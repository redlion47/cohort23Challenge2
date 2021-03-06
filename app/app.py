"""This file is ensuring the
UIs interract seamlessly"""
from flask import Flask, render_template, request, redirect, url_for, session
#from . import config

from . import category, usersReg

Category = category.Category

Users = usersReg.UsersReg


Category = category.Category
App = Flask(__name__, instance_relative_config=True, static_url_path='', static_folder='static')
App.config.from_object('config')

# App.config.from_object('config')

#start the home page
@App.route('/')
def main_Page():
    """when the base url is queried
    this fumction takes you to the
    index.html"""
    return render_template('index.html')

#take the users to the registration page
@App.route('/showSignUp')
def show_Sign_Up():
    """This takes you to the
    signup page"""

    return render_template('UserReg.html')

#takes the user to the login page
@App.route('/showLogin')
def show_Login():
    """This will take you to the login
    page"""
    return render_template('LoginPage.html')

#a method to enable the use to signup
@App.route('/UserReg', methods=['POST'])
def sign_Up():
    """This controls how the signup
    requirements are executed"""
    #code to get the input entered by the user
    username = request.form['username']
    email = request.form['email']
    pwd = request.form['password']
    conpwd = request.form['conpassword']

    #credentials = {username:pwd, email:pwd}

    #validation of the data received
    if pwd == conpwd:

        response = Users.addUsersReg(username,email,pwd)

        if response['status']:

            session['Users'] = response['UsersReg']

            return redirect(url_for('show_Login'))# return render_template('ViewPage.html', uname=username, result={})

        else:
            return render_template('UserReg.html', errorMessage = response['message'])


    else:
        return render_template('UserReg.html', errorMessage="!!YOUR CONFIRMATION \
        	PASSWORD DOESN'T MATCH YOUR PASSWORD!!")

#handles User logins
@App.route('/userLogin', methods=['POST'])
def user_Login():
    """This controls the requirements
    for login in"""
    #fetching login credentials
    username = request.form['username']
    pwd = request.form['password']


    #test login details
    #credentials = {'redlion':'ericardo47'}

    #validating the user

    if username == "" or pwd == "":
    #credentials.get(username, None) == None or pwd != credentials[username]:
        return render_template('LoginPage.html', errorMessage="username \
        	or password not match")
    
    #return redirect(url_for('viewCategory'))
    return render_template('RecipeCategories.html')
        # return render_template('ViewPage.html', uname=username, result={})

#adding recipe category
@App.route('/addCategory', methods=['GET', 'POST'])
def addCategory():
    if request.method == 'GET':
	    return render_template('addCategory.html')
    else:
        response = Category.addCategory(request.form['title'])

    if response['status']:
        session['categories'] = response['categories']
        return redirect(url_for('viewCategory'))

    else:
        return render_template('addCategory.html', errorMessage = response['message'])
        
#shows all the category list added

@App.route('/recipeCategory')
def viewCategory():

    return render_template('RecipeCategories.html')


# #adds categories to the site
# @app.route('/categoryAdded', methods = ['POST'])
# def addedCategory():

# 	category = list()
# 	category.append(str(request.form['categoryName']))#adds the entered category to a list

# 	return render_template('RecipeCategories.html', result = category)

#adding recipe to the list
@App.route('/addRecipe')
def add_Recipe():
    """This will take you to the
    page for adding recipes"""
    return render_template('addRecipe.html')


#adds recipe to the site
@App.route('/recipeAdded')
@App.route('/recipeAdded', methods=['POST'])
def added_Recipe():
    """This function anables a
    controlled adding of recipes"""


    

    if request.method == 'POST':
        recipe_name = str(request.form['recipeName'])
        ingredients = str(request.form['ingredients'])
        instructions = str(request.form['instructions'])


        category = {}
    
        category['recipeName'] = recipe_name

        category['Ingredients'] = ingredients
        category['Instructions'] = instructions
        category.append(str(request.form['recipeName']))#adds the entered category to a list
        return render_template('ViewPage.html', result=category)

    else:
        title = request.args['title']
        return render_template('ViewPage.html', result={})

    

    

if __name__ == '__main__':


    App.debug = True
    App.run()
    