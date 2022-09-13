import sys
import fileinput
import re
Lookup_CountyState={}
# known issue - get rid of first line"
covid_data_file="data/nyt.covid.us-counties.csv"
for each_line_of_text in fileinput.input(covid_data_file):
    if not fileinput.isfirstline():
        splitcolumn_array = re.split(',',each_line_of_text.replace( '"' ,'').replace('\n',''))
        uid=splitcolumn_array[1].lower()+":"+splitcolumn_array[2].lower() 
        if splitcolumn_array[1]!="Unknown" and splitcolumn_array[5]:
            print (splitcolumn_array[4],splitcolumn_array[5])
        # fails with divide by zero afer graham county in arizona
            if int(splitcolumn_array[4])>=0:
                print(each_line_of_text,splitcolumn_array[3])
                deathrate=int(splitcolumn_array[5])/int(splitcolumn_array[4])
                Lookup_CountyState[uid]=deathrate


print("end successful")

