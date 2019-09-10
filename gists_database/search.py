from .models import Gist
from datetime import datetime 

def search_gists(db_connection, **kwargs):
    if kwargs:
        if kwargs.get('github_id'):
            cursor = db_connection.execute('SELECT * FROM gists WHERE github_id = :github_id', kwargs)
            return [Gist(gist) for gist in cursor]
        elif kwargs.get('created_at'):
            cursor = db_connection.execute('SELECT * FROM gists WHERE datetime(created_at) = datetime(:created_at)', kwargs)
            return [Gist(gist) for gist in cursor]
    else:
        cursor = db_connection.execute('SELECT * FROM gists')
        return [Gist(gist) for gist in cursor]
            
            
            
            
#     if kwargs:
#         for param, value in kwargs.items():
#             query = 'SELECT * FROM gists WHERE'
#             if param == 'github_id':
#                 query += ' {} = :{}'.format(param,param)
#                 cursor = db_connection.execute(query,kwargs)
#             if param == 'created_at':
#                 query += ' {} = :{}'.format(param,param)
#                 cursor = db_connection.execute(query,kwargs)
# #             result = []
# #             result.append(Gist(gist) for gist in cursor)
#         return [Gist(gist) for gist in cursor]
#     else:
#         cursor = db_connection.execute('SELECT * FROM gists')
#         result = []
#         for gist in cursor:
#             result.append(Gist(gist))
#         return result
