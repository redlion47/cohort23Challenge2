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

    def __init__(self,title,recipe, ingredients, instructions):
        pass
        