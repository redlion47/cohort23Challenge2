cats = []
class Category:

    def __init__(self, title):
        selt.title = title

    def addCategory(title):
        if title == '':
            return {'status': False, 'message': "Please enter a title. We dont expect an empty String"}

        else:
            category = {}
            category['title'] = title
            cats.append(category)

            return {'status': True, 'categories': cats}

    def getCategories():

        return cats

class recipe(Category):

    def __init__(self,catTitle,recipe, ingredients, instructions):
        self.catTitle = catTitle
        self.recipe = recipe
        self.ingredients = ingredients
        self.instructions = instructions

    def joinRecipeToCategory(catTitle,recipe, ingredients, instructions):
        pickedCategory  = cats[catTitle]
        recipes = {}
        recipes['recipe'] = recipe
        recipes['ingredients'] = ingredients
        recipes['instructions'] = instructions

        for categ in cats:
            if categ[catTitle]:
                return categ




        