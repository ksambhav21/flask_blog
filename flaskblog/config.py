import os

# os.environ.get('SECRET_KEY')
# os.environ.get('SQLALCHEMY_DATABASE_URI')
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    # postgres://flask_blog_ftv6_user:jfzHhpJxCIPWg77Kr8hSpOKb6b4hF6Wi@dpg-cj4bkm5gkuvsl082to6g-a.oregon-postgres.render.com/flask_blog_ftv6
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'ksambhav21@gmail.com'
    MAIL_PASSWORD = 'neesjnruxwayibma'