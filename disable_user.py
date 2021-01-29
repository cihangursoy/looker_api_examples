import looker_sdk
from looker_sdk import methods, models, error
from datetime import datetime

sdk = looker_sdk.init31()  # or init40() for v4.0 API

looker_api_user = sdk.me()
all_users = sdk.all_users()

ids_to_disable = []
days_to_disable = 30

for u in all_users:
  login = None
  uid = u['id']
  login = u.credentials_email.logged_in_at

  if (login == None):
    login_date = datetime(2020,1,1)
  else:
    login_date = datetime.strptime(login[0:9],"%Y-%M-%d")
  print ((datetime.today() - login_date).days)
  print (u != looker_api_user)
  if (datetime.today()-login_date).days > days_to_disable and u != looker_api_user:
    ids_to_disable.append(uid)
print (ids_to_disable)

"""
for u in ids_to_disable:
  user_info_body =  looker.get_user(u)
  user_info_body['is_disabled'] = True
  looker.update_user(u,user_info_body)
"""
