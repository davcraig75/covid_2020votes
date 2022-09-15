import sys
import fileinput
import re
Lookup_CountyState={}
covid_data_file="data/nyt.covid.us-counties.csv"
# Line by Line storing deathrate into an associate array/dictionary by uid, called Lookup_CountyState
for each_line_of_text in fileinput.input(covid_data_file):
    each_line_text=each_line_of_text.strip()
    if not fileinput.isfirstline():
        splitcolumn_array = re.split(',',each_line_of_text.replace( '"' ,'').replace('\n',''))
        uid=splitcolumn_array[1].lower()+":"+splitcolumn_array[2].lower() 
        if splitcolumn_array[1]!="Unknown" and splitcolumn_array[5] and splitcolumn_array[0]=='2022-05-13':
            if int(splitcolumn_array[4])>=0:
                deathrate=int(splitcolumn_array[5])/int(splitcolumn_array[4])
                Lookup_CountyState[uid]=deathrate

# Going through our second file, and simply plugging in based on uid.                
vote_data_file="data/countypres_2000-2020.tsv"
lookup_republicans={}
lookup_democrat={}
lookup_green={}
lookup_other={}
lookup_libertarian={}

for each_line_of_text in fileinput.input(vote_data_file):
    each_line_of_text=each_line_of_text.strip()
    if not fileinput.isfirstline():
        splitcolumn_array = re.split('\t',each_line_of_text.replace( '"' ,'').replace('\n',''))
        uid=splitcolumn_array[3].lower()+":"+splitcolumn_array[1].lower()
        if uid in Lookup_CountyState:
            if splitcolumn_array[7] == 'REPUBLICAN':
                lookup_republicans[uid]=splitcolumn_array[8]
            elif splitcolumn_array[7] == 'DEMOCRAT':
                lookup_democrat[uid]=splitcolumn_array[8]
            elif splitcolumn_array[7] == 'GREEN':     
                lookup_green[uid]=splitcolumn_array[8]                
            elif splitcolumn_array[7] == 'OTHER':     
                lookup_other[uid]=splitcolumn_array[8]
            elif splitcolumn_array[7] == 'LIBERTARIAN':     
                lookup_other[uid]=splitcolumn_array[8]                
            else: 
                print("I shouldn't be here",splitcolumn_array[7])
                

print('uid'+'\t'+'deathrate'+'\t'+'republicans'+'\t'+'democrats'+'\t'+'perc_repub')
for uid in Lookup_CountyState:
    if lookup_republicans[uid]:
        if lookup_democrat[uid]:
            perc_rep=int(lookup_republicans[uid])/(int(lookup_republicans[uid])+int(lookup_democrat[uid]))
            print(uid+'\t'+str(Lookup_CountyState[uid])+"\t"+str(lookup_republicans[uid])+'\t'+str(lookup_democrat[uid])+'\t'+str(perc_rep))
            
