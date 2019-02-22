from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        email_match = User.objects.filter(email = postData['email'])
        #validations for first name//////////
        if len(postData['first_name']) == 0:
            errors['first_name'] = "First Name cannot be blank"
        elif len(postData['first_name']) < 2:
            errors["first_name"] = "First Name needs to be atleast 2 characters!"
        elif postData['first_name'].isalpha() == False:
            errors['first_name'] = "First Name must contian only letters"
        #validations for last name//////////////////////
        if len(postData['last_name']) == 0:
            errors['last_name'] = "Last Name cannot be blank"
        elif len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name needs to be atleast 2 characters!"
        elif postData['last_name'].isalpha() == False:
            errors['last_name'] = "Last Name must contian only letters"
        #validations for email//////////////////
        if len(postData['email']) == 0:
            errors['email'] = "Email cannot be blank"
        elif len(email_match) > 0:
            errors['email_invalid'] = 'That email exists in the database already'
        #validations for password//////////
        if postData['password'] != postData['confirmpw']:
            errors["confirmpw"] = "Passwords does not match"
        elif len(postData['password']) < 8:
            errors["leng_password"] = "Password should be at least 8 characters"
        return errors

    def login_validator(self,postData):
        errors = {}
        user = User.objects.filter(email = postData['login_email'])
        if len(postData['login_password']) == 0:
            errors['pword_blank'] = 'The password field cannot be blank'
        if len(postData['login_email']) == 0:
            errors['email_blank'] = "Please enter email"
        elif len(user) == 0:
            errors['invalid'] = "Invalid login credentials."
        else:
            user = User.objects.get(email=postData['login_email'])
            if user.password != postData["login_password"]:
                errors['password'] = "Password does not match"
        return errors

    def editprofile_validator(self, postData):
        errors = {}
        email_match = User.objects.filter(email = postData['email'])
        if len(postData['first_name']) == 0:
            errors['no_firstname'] = "You Must Enter New First Name!"
        if len(postData['last_name']) == 0:
            errors['no_lastname'] = "You Must Enter New Last Name!"
        if len(postData['email']) == 0:
            errors['no_lastname'] = "You Must Enter Email!"
        elif len(email_match) > 0:
            errors['email_invalid'] = 'That email exists in the database already'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    objects = UserManager()

    def __repr__(self):
        return f"name={self.first_name}{self.last_name}, email:{self.email}"
