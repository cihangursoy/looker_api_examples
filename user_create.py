import looker_sdk, csv
from looker_sdk import methods, models, error

sdk = looker_sdk.init31()  # or init40() for v4.0 API

with open('user_list.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  for row in csv_reader:
    created_user = sdk.create_user(models.WriteUser(first_name=row[0], last_name=row[1]))
    user_id = created_user.id
    sdk.create_user_credentials_email(user_id, body=models.WriteCredentialsEmail(email=row[2]))
    sdk.add_group_user(group_id=row[3], body=models.GroupIdForGroupUserInclusion(user_id=user_id))
    line_count += 1
