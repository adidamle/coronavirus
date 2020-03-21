import pandas as pd

# TODO - Ensure that the file will somehow get updated when johns hopkins adds new data.
csvfile = "C:\Adu\JohnsHopkinsData\COVID-19\csse_covid_19_data\csse_covid_19_daily_reports\\03-20-2020.csv"
coronaDataFrame = pd.read_csv(csvfile, parse_dates=['Last Update'])

# Renamed and dropped certain columns. 
coronaDataFrame = coronaDataFrame.rename(columns={"Country/Region": "Country", "Last Update": "Date"})
coronaDataFrame = coronaDataFrame.drop(columns = {"Latitude", "Longitude", "Province/State"})

# Covert the Date column to the datetime and strip off the 
# time from the timestamp.
coronaDataFrame['Date'] = pd.to_datetime(coronaDataFrame['Date'])
coronaDataFrame['Date']= coronaDataFrame['Date'].map(pd.Timestamp.date)

# Groupby the country and sum over it to get count for each country.
coronaDataFrame = coronaDataFrame.groupby(['Country']).sum()

print(coronaDataFrame.query("Country == 'Italy'"))