import webapp2
from rotx import *

rot13_page="""
<!DOCTYPE HTML>
<html>
  <head> 
    <title> ROT13 HW </title> 
  </head>

  <body>
    <h2> Enter some schtuff: </h2>
    <form method="post">
      <textarea name="text"
                style="height: 100px; width: 400px;" 
                value="%(field)s">%(field)s</textarea>
      <br>
      <input type="submit">
    </form>
  </body>
<html>
"""


class Rot13(webapp2.RequestHandler):
  def write_form(self, field=""):
      self.response.out.write(rot13_page % {"field": field})

  def get(self):
      self.write_form()

  def post(self):
      field = self.request.get("text")
      # Run field through rot13
      field = rotx(field, 13)
      # Now post the new page
      self.write_form(field)

signup_page="""
<!DOCTYPE HTML>
<html>
  <head> 
    <title> Signup page </title> 
  </head>

  <body>
    <h2> Sign up </h2>
    <br>
    <form method="post">

      <label> Username:
        <input type="text" name="username" value="%(sub_username)s">
      </label>
      %(sub_err_username)s
      <br>

      <label> Password:
        <input type="password" name="password" value="%(sub_password)s">
      </label>
      <br>

      <label> Verify password:
        <input type="password" name="verify" value="%(sub_verify)s"> 
      </label>
      %(sub_err_password)s
      <br>

      <label> Email (optional):
        <input type="text" name="email" value="%(sub_email)s">
      </label>
      %(sub_err_email)s
      <br>
        
      <br>
      <input type="submit">
    </form>
  </body>
<html>
"""


import re

USER_RE    = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
USER_PASS  = re.compile(r"^.{3,20}$")
USER_EMAIL = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):
  return USER_RE.match(username)

def valid_password(password):
  return USER_PASS.match(password)

def valid_email(email):
  return USER_EMAIL.match(email)


class Signup(webapp2.RequestHandler):
  def write_form(self, username="", password="", verify="", email="",
                 err_username="", err_password="", err_email=""):
      self.response.out.write(signup_page % {"sub_username": username,
                                             "sub_password": password,
                                             "sub_verify": verify,
                                             "sub_email": email,
                                             "sub_err_username": err_username,
                                             "sub_err_password": err_password,
                                             "sub_err_email": err_email} )

  def get(self):
      self.write_form()

  def post(self):
      # Get all the input
      user_username = self.request.get("username")
      user_password = self.request.get("password")
      user_verify = self.request.get("verify")
      user_email    = self.request.get("email")

      # Validate variables
      err_username = ""
      err_password = ""
      err_email = ""
      if not valid_username(user_username):
        err_username = "Invalid username."
      if not user_password == user_verify:
        err_password = "Passwords do not match."
        user_password = ""
        user_verify = ""
      elif not valid_password(user_password):
        err_password = "Invalid password."
        user_password = ""
        user_verify = ""
      if user_email != "":
        # Email can be blank b/c optional
        if not valid_email(user_email):
          err_email = "Invalid email."

      if not (err_username == "" and err_password == "" and err_email ==""):
        # Render page again with error messages
        self.write_form(user_username, user_password, user_verify, user_email,
                        err_username, err_password, err_email)
      else:
        # Redirect to happy welcome page
        self.redirect("/unit2/welcome?username=%(username)s" % {"username": user_username})

page_welcome="""
<!DOCTYPE HTML>
<html>
  <head> 
    <title> Welcome! </title> 
  </head>

  <body>
    <h2> Welcome, %(username)s!</h2>
  </body>
<html>
"""


class Welcome(webapp2.RequestHandler):
  def get(self):
      username = self.request.get("username")
      self.response.out.write(page_welcome % {"username": username})


class Main(webapp2.RequestHandler):
  def get(self):
      self.response.out.write("The main page.")

app = webapp2.WSGIApplication([('/', Main),
                               ('/unit2/rot13', Rot13),
                               ('/unit2/welcome', Welcome),
                               ('/unit2/signup', Signup)
                              ], 
                              debug=True)
