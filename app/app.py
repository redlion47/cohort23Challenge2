"""This file is ensuring the
UIs interract seamlessly"""
from flask import Flask, render_template, request, redirect, url_for, session
#from . import config

from . import category, usersReg

Category = category.Category
Recipe = category.recipe
Users = usersReg.UsersReg
# UserData = usersReg.Users

App = Flask(__name__, instance_relative_config=True, static_url_path='', static_folder='static')
App.config.from_object('config')

# App.config.from_object('config')

################################HOME PAGE##############################################

#start the home page
@App.route('/')
def main_Page():
    """when the base url is queried
    this fumction takes you to the
    index.html"""
    return render_template('index.html')

####################################REGISTER############################################

#take the users to the registration page
@App.route('/showSignUp')
def show_Sign_Up():
    """This takes you to the
    signup page"""

    return render_template('UserReg.html')

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

        if response['status'] == True:

            return render_template('LoginPage.html')# return render_template('ViewPage.html', uname=username, result={})

        else:
            return render_template('UserReg.html', errorMessage = response['message'])


    else:
        return render_template('UserReg.html', errorMessage="!!YOUR CONFIRMATION \
            PASSWORD DOESN'T MATCH YOUR PASSWORD!!")


###################################LOGIN##################################################

#takes the user to the login page
@App.route('/showLogin')
def show_Login():
    """This will take you to the login
    page"""
    return render_template('LoginPage.html')


#handles User logins
@App.route('/userLogin', methods=['POST'])
def user_Login():
    """This controls the requirements
    for login in"""
    #fetching login credentials

    username = request.form['username']
    pwd = request.form['password']

    #validating the user

    if username == "" or pwd == "":
    
        return render_template('LoginPage.html', errorMessage="username \
        	or password not match")
    else:
        userCheck = usersReg.checkUser(username,pwd)
        if userCheck['status'] == True:
            session['uName'] = userCheck['realName']

            return redirect(url_for('viewCategory'))
            # return render_template('RecipeCategories.html')
        else:
            return render_template('LoginPage.html', errorMessage=userCheck['message'])


######################################CATEGORIES###########################################

#shows all the category list added
@App.route('/recipeCategory')
def viewCategory():

    return render_template('RecipeCategories.html')


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
        
# a method to delete categories
@App.route('/recipeCategory/dT', methods = ['GET'])
def delCategory():
    
    if request.args['recipeStatus'] == 'True':
        response = Recipe.deletionFromStore(request.args['title'],request.args['recipe'])
        session['recipeLst'] = response
        session['category'] = request.args['title']
        session['message'] = ""
        # session['recipeStatus'] = request.args['recipeStatus']
        
        return redirect(url_for('newDisplayRecipes'))

    else:
        response = category.recipe.deletionFromStore(request.args['title'])
        session['categories'] = response
        return redirect(url_for('viewCategory'))
    
###########################################RECIPES############################################



# the route taken by the new list after content is deleted
@App.route('/newRecipeList')
def newDisplayRecipes():
    
    return render_template('RecipeList.html')


# this metod is for displaying a list of recipes available per category
@App.route('/recipeList')
def displayRecipes():

    category = request.args['title']
    recipeLst = Recipe.getRecipeList(category)
    session['message'] = ""
    session['recipeLst'] = recipeLst 
    session['category'] = category

    return render_template('RecipeList.html')

    
#adding recipe to the list
@App.route('/addRecipe')
def add_Recipe():
    """This will take you to the
    page for adding recipes"""
    category = request.args['title']
    session['message'] = ""
    session['category'] = category
    return render_template('addRecipe.html')   

#adds recipe to the site
# @App.route('/recipeAdded')
@App.route('/recipeAdded', methods=['POST'])
def added_Recipe():
    """This function anables a
    controlled adding of recipes"""
    recipe_name = str(request.form['recipeName'])
    ingredients = str(request.form['ingredients'])
    instructions = str(request.form['instructions'])
    category = request.args['title']

    response = Recipe.joinRecipeToCategory(category , recipe_name, ingredients, instructions)

    if response['status'] == True:

        session['message'] = response['message']
        session['recipeLst'] = response['categoryRecipes']
        session['category'] = category

        return redirect(url_for('newDisplayRecipes'))

    else:
        session['category'] = category
        session['message'] = response['message']
        return redirect(url_for('add_Recipe'))

    

    

if __name__ == '__main__':


    App.debug = True
    App.run()
    