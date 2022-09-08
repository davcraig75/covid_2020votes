# Objective

Determine if there is a obvious correlation between voting by county in the Uniited States versus the percentage of people who got covid and died.

Importantly, this is in development.

## Requirements Gathering.

Learned that the data needs to be reshaped: reshape.py

1. I need a UID (Unique Identifier).  I will use lowercase state:county.
2. In table 1, nyt.covid.us-counties.csv, I need to filter by date and I'll pick 2022-05-13
3. In table 2, us-counties.csv, I am going to need to pull out just 2020 election, and reshape the table so that it has uid, vote by party count, and fraction democrat.
4. Create VoteByCounty dictionary, where I can lookup the vote count by county and party. Reading through `countypres_2000-2020.tsv`, line by line, and storing the values in side of this.  

```
VoteByCounty['california:los angeles']['Republican']=
```

5.  Create CovidStatsByCount dictionary, where I can lookup the covid stats by county reading `nyt.covid.us-counties.csv`

```
CovidStatsByCount['california:los angeles']['deaths']
CovidStatsByCount['california:los angeles']['cases']
```

I'm going to call the script join_covid_count.py


* Known issue*

* Puerto rico, Alaska and others are incompatible with the two datasets have.


### Goal to understand data

## Instructions

Get covid data
I downloaded data:

```
wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv
```

I then renamed it:
```
mv us-counties.csv nyt.covid.us-counties.csv
```

