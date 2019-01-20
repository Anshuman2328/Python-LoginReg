from __future__ import unicode_literals
from django.db import models
import re, bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2 or not postData['fname'].isalpha():
            errors['fname'] = "The first name should be longer than 2 characters and must be letter"
        if len(postData['lname']) < 2 or not postData['lname'].isalpha():
            errors['lname'] = "The first name should be longer than 2 characters and must be letter"
        potential_matches = User.objects.filter(email=postData['email'])
        if len(potential_matches) > 0:
            errors['unique_email'] = "email already exists"

        
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Please enter a valid email"
        if len(postData['pwd']) < 2:
            errors['pwd'] = "Password should be atleast 8 characters long"
        if postData['pwd'] != postData['pwd1']:
            errors['pwds'] = "Passwords do not match"
        return errors


class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
        # if len(postData['fname']) < 2:
        #     errors['fname'] = "First name should be atleast 2 characters long"
        # if not postData['fname'].isalpha():
        #     errors['fname_alpha'] = "First name should be only letters"
        # if len(postData['lname']) < 2:
        #     errors['lname'] = "Last name should be atleast 2 characters long"
        # if not postData['lname'].isalpha():
        #     errors['lname_alpha'] = "Last name should be only letters"
#         # validate the first name       
#         if len(postData['fname']) < 3 or not postData['fname'].isalpha():
#             errors['fname'] = "First name must be at least 3 characters long, and use only alphabetical characters."
#         # if len(postData['fname']) < 2:
#         #     errors['fname'] = 'Firat name should be at least 2 characters'
#         # if not len(postData['fname'].isalpha():
#         #     errors['fname_alpha'] = 'Firat name should only be letters'

#         # validate the last name
#    	    # if len(postData['lname']) < 3 or not postData['lname'].isalpha():
# 		# 	errors['lname'] = "Last name must be at least 3 characters long, and use only alphabetical characters."
#         if len(postData['lname']) < 2:
#             errors['lname'] = 'Firat name should be at least 2 characters'
#         if not len(postData['lname']).isalpha():
#             errors['lname_alpha'] = 'Firat name should only be letters'
        
#         # validate the email now with regex
#         if EMAIL_REGEX.match(postData['email']) == None:
#             errors['email_format'] = "Email must be in valid email format."
#         # if not EMAIL_REGEX.match(postData['email']):
#         #     errors['email'] = "Email must be in valid email format."

#         # validate the password
# 		if len(postData['pwd']) < 8:
# 			errors['pwd'] = "Password must be at least 8 characters long."

#         # make sure passwrds match
#         if not postData['pwd'] == postData['pwd1']:
#             errors['pwconf'] = "Password confirmation must match password."

#         # if postData['pwd'] != postData['pwd1']:
#         #     errors['pwconf'] = "Password confirmation must match password."







    # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    # *************************
    # def __repr__(self):
    #     return f'Name of the User is {self.fname}{self.lname} and the email is {self.email}'
# # class UserManager(models.Manager):
# #     def basic_validator(self, postData):
# #         errors = {}
# #         if len(postData['name']) < 5:
# #             errors["name"] = "Blog name should be at least 5 characters"
# #         if len(postData['desc']) < 10:
# #             errors["desc"] = "Blog description should be at least 10 characters"
# #         return errors



# class UserManager(models.Manager):
#     def reg_Validator(self, postData):
#         errors = {}





        



        
# 		if User.objects.filter(email = postData['email']):
# 		 	errors['email_exists'] = "An account associated with that email address already exists."
		# if len(postData['fname']) < 3 or not postData['fname'].isalpha():
		# 	errors['fname'] = "First name must be at least 3 characters long, and use only alphabetical characters."

		# if len(postData['lname']) < 3 or not postData['lname'].isalpha():
		# 	errors['lname'] = "Last name must be at least 3 characters long, and use only alphabetical characters."
        # if not EMAIL_REGEX.match(postData['email']):
        #     errors['email'] = "Email must be in valid email format."
# 		# print errors
# 		return errors
# 	def loginValidator(self, postData):
# 		user = User.objects.filter(email = postData['lemail'])
# 		errors = {}
# 		if not user:
# 			errors['email'] = "Please enter a valid email address."
# 		if user and not bcrypt.checkpw(postData['lpwd'].encode('utf8'), user[0].password.encode('utf8')):
# 			errors['password'] = "Invalid password."
# 		return errors



# Inside your app's models.py file
# from __future__ import unicode_literals
# from django.db import models
# Our new manager!
# No methods in our new manager should ever catch the whole request object with a parameter!!! 
# (just parts, like request.POST)
# class BlogManager(models.Manager):
#     def basic_validator(self, postData):
#         errors = {}
#         if len(postData['fname']) < 5:
#             errors["fname"] = "User name should be at least 5 characters"
#         if len(postData['desc']) < 10:
#             errors["email"] = "Blog description should be at least 10 characters"
#         return errors










































