from flask import Blueprint

missions_blueprint = Blueprint('missions',__name__,url_prefix='/missions',template_folder='templates',static_folder='static')
