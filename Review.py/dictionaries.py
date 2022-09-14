#dictionary syntax

months = {
   "Jan": "January",
   "Feb": "February",
   "Mar": "March"
   }

#syntax for getting the value with the key as reference
print(months["Mar"])

print(months.get("Jan"))

#use get to display none if ever the entered key is non-existent

print(months.get("3-gatsu","Invalid Key"))