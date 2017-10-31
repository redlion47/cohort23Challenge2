import os
import unittest
from app.app import App


class LoginTest(unittest.TestCase):
	"""docstring for LoginTest"""


	def test_mainPage(self):
		resp = App.test_client(self)
		response = resp.get('/', content_type ='html/txt')
		
		self.assertEqual(response.status_code, 200)
		

	def test_showLogin(self):
		resp = App.test_client(self)
		response = resp.get('/showLogin', follow_redirects=True)
		self.assertEqual(response.status_code, 200)
		pass
		
	def test_login(self):
		resp = App.test_client(self)
		response = resp.get('/showLogin', data=dict(username='admin', password='password'), follow_redirects=True)
		self.assertIn(b'YUMMY RECIPES', response.data)


	def test_signUp(self):
		resp = App.test_client(self)
		response = resp.post('/UserReg', data=dict(username='admin', password='password', email ='red@admin.ng', conpassword='password' ), follow_redirects=True)
		self.assertIn(b'WELCOME TO YUMMY admin', response.data)
		pass



if __name__ == '__main__':
    unittest.main()