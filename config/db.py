# local testing
db_name = "postgres"
db_host = "127.0.0.1"
db_port = "5432"
db_user = "postgres"
user_password = "postgres"

SQLALCHEMY_DATABASE_URI = 'postgresql://' + db_user + ':' + user_password + '@' + db_host + '/' + db_name
