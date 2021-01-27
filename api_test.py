import looker_sdk


sdk = looker_sdk.init31()  # or init40() for v4.0 API
my_user = sdk.me()

# output can be treated like a dictionary
print(my_user["first_name"])
# or a model instance (User in this case)
print(my_user.first_name)
