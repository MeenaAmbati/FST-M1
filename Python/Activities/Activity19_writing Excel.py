
import pandas
from pandas import ExcelWriter

data = {
	'FirstName':["Meena", "Lakshmi", "Pavani"],
	'LastName':["Ambati", "Sakhi", "Gadi"],
	'Email':["meena@example.com", "lakshmi@example.com", "pavani@example.com"],
	'PhoneNumber':["8877669966", "8877669977", "8877669988"]
}


dataframe = pandas.DataFrame(data)


print(dataframe)


writer = ExcelWriter('sample.xlsx')
dataframe.to_excel(writer, 'Sheet1', index = False)

writer.save()