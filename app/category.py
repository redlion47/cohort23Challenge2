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

        if recipe != "" and (ingredients != "" or instructions != ""):
            recipeLst = []
            recipes = {}
            recipes['recipe'] = recipe
            recipes['ingredients'] = ingredients
            recipes['instructions'] = instructions

            for categ in cats:
                for key, value in categ.items():
                    if value == catTitle:
                        temp = cats.index(categ)
                        # categ[recipe] = recipes
                        if key != 'title':
                            recipeLst.append(key)
                            pass

                    else:
                        break

            

            cats[temp][recipe] = recipes

            # cats.append(categ)
            message = "Recipe successfully added!!!!"

            return {'status' : True, 'message': message, 'categoryRecipes' : recipeLst }

        else:
            message = "You can't leave a recipe empty. Can you cook water??"
            return {'status' : False, 'message' : message}



    def deletionFromStore(category, recipe=None):
        """This method is for enabling deletion
        of both categories and recipes from our
        storage point"""

        if recipe == None:
            # categorylst =[]
            for eachCategory in cats:
                for key, value in eachCategory.items():
                    if value == category:

                        cats.remove(eachCategory)

                    else:
                        break
                # categorylst.append(eachCategory['title'])
            # return categorylst
            return cats

        else:
            recipelst = []
            for eachCategory in cats:
                for key, value in eachCategory.items():
                    if value == category:

                        del eachCategory[recipe]
                        if key != 'title':
                            recipelst.append(key)

                    else:
                        break

            return recipelst

        

    def getRecipeList(category):
        """This method will be used to get a 
        list of all the recipes associated 
        with a category"""
        recipeList = []
        for eachCategory in cats:
            for key,value in eachCategory.items():
                if value == category:
                    if key != "title" :
                        recipeList.append(key)

                else:
                    break

        return recipeList
        