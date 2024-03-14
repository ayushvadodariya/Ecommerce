from flask import Blueprint, render_template,  redirect, url_for

user= Blueprint('user', __name__, template_folder="templates")

@user.route('/')
def userDetail():
  return "user"


