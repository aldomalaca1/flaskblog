import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')#'5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') #'sqlite:///site.db'
    
    #Configuracion de mailtrap para hacer testing
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '7026cc78dde213'
    MAIL_PASSWORD = 'f0a31412e5dad6'
    MAIL_USE_TLS = True 
    MAIL_USE_SSL = False

#Configuracion para el mail de google
'''app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
   app.config['MAIL_PORT'] = 587
   app.config['MAIL_USE_TLS'] = True
   app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
   app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')'''
