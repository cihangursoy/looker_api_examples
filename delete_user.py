import looker_sdk

sdk = looker_sdk.init31()  # or init40() for v4.0 API

x = 92
while  x < 167:
  sdk.delete_user(x)
  print("Deleted User",x)
  x+=1
