import looker_sdk

sdk = looker_sdk.init31()  # or init40() for v4.0 API

created_user = sdk.create_user(body={"first_name": "Jane", "last_name": "Doe"})
#print(created_user.id) Use this to print the User ID for troubleshooting purposes
user_id = created_user.id
sdk.create_user_credentials_email(user_id, body={"email":"janedoe@email.com"})
