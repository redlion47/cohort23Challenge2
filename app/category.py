cats = []
class Category:

    def __init__(self, title):
        selt.title = title

    def addCategory(title):
        """The method is for creating and
        storing a category"""

        if title == '':
            return {'status': False, 'message': "Please enter a title. We dont expect an empty String"}

        else:
            category = {}
            category['title'] = title
            cats.append(category)

            return {'status': True, 'categories': cats}

    def getCategories():
        """The method to get a list of all
        the categories availabe"""

        categoryList = []

        for category in cats:
            categoryList.append(category['title'])

        return categoryList #a list of categories

class recipe(Category):

    def __init__(self,catTitle,recipe, ingredients, instructions):
        self.catTitle = catTitle
        self.recipe = recipe
        self.ingredients = ingredients
        self.instructions = instructions

    def joinRecipeToCategory(catTitle,recipe, ingredients, instructions):
        """This category associates 
        the recipes the user adds
        with the category selected"""

        if catTitle != "":
            if recipe != "" and (ingredients != "" or instructions != ""):
                
                recipes = {}
                recipes['recipe'] = recipe
                recipes['ingredients'] = ingredients
                recipes['instructions'] = instructions

                for categ in cats:
                    for key, value in categ.items():
                        if value == catTitle:
                            categ[recipe] = recipes

                        else:
                            break

                cats.append(categ)
                message = "Recipe successfully added!!!!"

                return {'status' : True, 'message': message, 'categoryRecipes' : cats }

            else:
                message = "You can't leave a recipe empty. Can you cook water??"
                return {'status' : False, 'message' : message}

        else:
            return {'status': False, 'message' : "Please provide a category!"}


    def deletionFromStore(self):
        """This method is for enabling deletion
        of both categories and recipes from our
        storage point"""
        
        pass

    def getRecipeList(self):
        """This method will be used to get a 
        list of all the recipes associated 
        with a category"""
        pass