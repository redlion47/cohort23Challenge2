cats = []
class Category:

    def __init__(self, title):
        selt.title = title

    def addCategory(title):
        if title == '':
            return {'status': False}
        else:
            category = {}
            category['title'] = title
            cats.append(category)

            return {'status': True, 'categories': cats}



    def getCategories():

        return cats
