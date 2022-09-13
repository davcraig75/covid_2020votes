import sys
import fileinput
import re
Lookup_CountyState={}
covid_data_file="data/nyt.covid.us-counties.csv"
for each_line_of_text in fileinput.input(covid_data_file):
    each_line_of_text.rstrip()
    if not fileinput.isfirstline():
        splitcolumn_array = re.split(',',each_line_of_text.replace( '"' ,'').replace('\n',''))
        uid=splitcolumn_array[1].lower()+":"+splitcolumn_array[2].lower() 
        if splitcolumn_array[1]!="Unknown" and splitcolumn_array[5] and splitcolumn_array[0]=='2022-05-13':
            if int(splitcolumn_array[4])>=0:
                deathrate=int(splitcolumn_array[5])/int(splitcolumn_array[4])
                Lookup_CountyState[uid]=deathrate

vote_data_file="data/countypres_2000-2020.tsv"
for each_line_of_text in fileinput.input(vote_data_file):
    if not fileinput.isfirstline():
        each_line_of_text.rstrip()
        splitcolumn_array = re.split('\t',each_line_of_text.replace( '"' ,'').replace('\n',''))
        uid=splitcolumn_array[3].lower()+":"+splitcolumn_array[1].lower()
        if uid in Lookup_CountyState:
            print (uid,each_line_of_text,Lookup_CountyState[uid])

