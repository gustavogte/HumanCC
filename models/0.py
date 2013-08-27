from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'HumanCap3 Simple'
settings.subtitle = 'powered by DataWork'
settings.author = 'Gustavo Matias Gutierrez Leon'
settings.author_email = 'gustavogte@datawork.mx'
settings.keywords = 'Recursos Humanos'
settings.description = 'Administraci\xc3\xb3n y desarrollo de Recursos Humanos.'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '568ea311-6ff6-4f55-8069-606aef1fafb6'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
