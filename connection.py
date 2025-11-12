class Connection:
    def __init__(self, sql_type, user, password, server, post = None, **args):
        self.user = user
        self.password = password
        self.server = server
        self.sql_type = sql_type
        self.post = post
        self.args = args
    @property
    def engine(self):
        if self.sql_type == "MSSQL":
            return f'mssql+pymssql://{self.user}:{self.password}@{self.server}/{self.args['db_name']}'
        if self.sql_type == "POSTGRESQL":
            return f'postgresql://{self.user}:{self.password}@{self.server}:{str(self.post)}/{self.args['db_name']}'
        else:
            print ('Соединение не поддерживается')
    @property
    def async_engine(self):
        if self.sql_type == "MSSQL":
            return f"mssql+aioodbc://{self.user}:{self.password}@{self.server}/{self.args['db_name']}"
        if self.sql_type == "POSTGRESQL":
            return f"postgresql://{self.user}:{self.password}@{self.server}:{str(self.post)}/{self.args['db_name']}"
        else:
            print ('Соединение не поддерживается')