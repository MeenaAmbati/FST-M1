
import pandas

data = {
  "Usernames": ["Meena", "Lakshmi", "Pavani"],
  "Passwords": ["Analyst", "Developer", "Admin"]
}

dataframe = pandas.DataFrame(data)


print(dataframe)

dataframe.to_csv("sample.csv", index=False)