import os

#basedir = os.path.abspath(os.path.dirname(__file__))
DEV_DATABASE_URL = 'mysql+pymysql://root:bqRZhPEUk5?#@localhost/fan'
TEST_DATABASE_URL = 'mysql+pymysql://root:bqRZhPEUk5?#@localhost/fan'
DATABASE_URL = 'mysql+pymysql://root:bqRZhPEUk5?#@localhost/fan'


class Config:
	'''基类 Config 中包含通用配置，子类分别定义专用的配置。如果需要，你还可添加其他配置类。'''
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'pw_abc'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASKY_MAIL_SENDER = '554155355@qq.com'
	FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

	@staticmethod
	def init_app(app):
		pass


class DevelopmentConfig(Config):
	'''适合开发测试，如本地测试环境。'''
	DEBUG = True
	MAIL_SERVER = 'smtp.qq.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	SQLALCHEMY_DATABASE_URI = DEV_DATABASE_URL


class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = TEST_DATABASE_URL


class ProductionConfig(Config):
	'''拥有较高的安全性设定，适合服务器上线运营当产品。'''
	SQLALCHEMY_DATABASE_URI = DATABASE_URL


config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production':ProductionConfig,
	'default': DevelopmentConfig
	}
