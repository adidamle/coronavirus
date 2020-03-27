import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

filePath = './covid_19_data.csv'
covid_19_data = pd.read_csv(filePath)

# Renamed columns and also dropped the ones which I wont be using.
covid_19_data.rename(columns={"Country/Region": "Country", "Province/State": "State", "ObservationDate" : "Date"}, inplace=True)
covid_19_data.drop(columns={'SNo'}, inplace = True)
covid_19_data.replace(to_replace={'Mainland China':'China'}, inplace=True)

# Get the latest data.
latest_data = covid_19_data[covid_19_data['Date'] == max(covid_19_data['Date'])]

#################################################################
####################### TASK 1 ##################################
#################################################################

# GOAL - Display the global count for Confimed, Deaths and recovered.
total_world = latest_data.groupby(['Date']).sum().reset_index()

labels = ["Current as of","Confirmed","Deaths","Recovered"]
fig = go.Figure(data=[go.Table(header=dict(values=labels),
                 cells=dict(values=total_world.loc[0,["Date","Confirmed","Deaths","Recovered"]]))
                     ])
fig.update_layout(title='Global counts for Coronavirus : ')
fig.update_layout(width=600, height=350)
### need to figure a way to save this graph as well.
#fig.savefig("GlobalCount.png")


#################################################################
####################### TASK 2 ##################################
#################################################################

# GOAL - To display the counts for the top 8 countries using bar graphs.

latest_data1 = latest_data.groupby(['Country']).sum()

f1 = plt.figure(figsize=(20,5));
f1.add_subplot(121)

plt.barh(latest_data1.sort_values('Confirmed')["Confirmed"].index[-8:],latest_data1.sort_values('Confirmed')["Confirmed"].values[-8:],color='Pink')
plt.tick_params(size=6,labelsize = 13);
plt.xlabel("Confirmed",fontsize=18);
plt.title("Top 8 Countries (Confirmed Cases)",fontsize=16);
#plt.savefig('Top 10 Countries (Confirmed Cases).png')
plt.grid(alpha=0.23)

f1.add_subplot(122)

plt.barh(latest_data1.sort_values('Deaths')["Deaths"].index[-8:],latest_data1.sort_values('Deaths')["Deaths"].values[-8:],color='Pink')
plt.tick_params(size=6,labelsize = 13);
plt.xlabel("Deaths",fontsize=18);
plt.title("Top 8 Countries (Deaths Cases)",fontsize=16);
plt.savefig('Top 8 Countries (Confirmed and Death Cases).png')
plt.grid(alpha=0.23)

f2 = plt.figure(figsize=(8.5, 5));
f2.add_subplot(111)

plt.barh(latest_data1.sort_values('Recovered')["Recovered"].index[-8:],latest_data1.sort_values('Recovered')["Recovered"].values[-8:],color='Pink')
plt.tick_params(size=6,labelsize = 13);
plt.xlabel("Recovered",fontsize=18);
plt.title("Top 8 Countries (Recovered Cases)",fontsize=16);
plt.savefig('Top 8 Countries (Recovered Cases).png')
plt.grid(alpha=0.23)

#################################################################
####################### TASK 3 ##################################
#################################################################

# GOAL - To display the statewise counts for Confimed, Deaths 
# and recovered for China using pie charts.

# Get the data for China and agrregate for each state.
china = latest_data[latest_data.Country == 'China'][['State', 'Confirmed', 'Deaths', 'Recovered']]
china = china.groupby(['State']).sum().reset_index()

# Pie chart for Confirmed
chinaC = px.pie(china, values='Confirmed', names='State', title = "Statewise Confirmed in China")
chinaC.update_traces(hoverinfo='label+percent+value', textinfo='percent+value', textposition = 'inside')
chinaC.show()

# Pie chart for Confirmed
chinaD = px.pie(china, values='Deaths', names='State', title = "Statewise Deaths in China")
chinaD.update_traces(hoverinfo='label+percent+value', textinfo='percent+value', textposition = 'inside')
chinaD.show()

# Pie chart for Confirmed
chinaR = px.pie(china, values='Recovered', names='State', title = "Statewise Recovered in China")
chinaR.update_traces(hoverinfo='label+percent+value', textinfo='percent+value', textposition = 'inside')
chinaR.show()

#################################################################
####################### TASK 4 ##################################
#################################################################

# GOAL - To make a grouped bar graph for the statewise counts in US.
us = latest_data[latest_data.Country == 'US'][['State', 'Confirmed', 'Deaths', 'Recovered']]
us = us.groupby(['State']).sum().reset_index()

fig1 = go.Figure(data=[
    go.Bar(name='Confirmed', x=us['State'], y=us['Confirmed']),
    go.Bar(name='Deaths', x=us['State'], y=us['Deaths']),
    go.Bar(name='Recovered', x=us['State'], y=us['Recovered'])
])
# Change the bar mode - can change to stack in future if necessary.
fig1.update_layout(barmode='group')
fig1.show();


#################################################################
####################### TASK 5 ##################################
#################################################################

# GOAL - To make a time series for the counts for Italy
italy = covid_19_data[covid_19_data.Country == 'Italy'][['Date', 'Confirmed', 'Deaths', 'Recovered']]
italy = italy.groupby(['Date']).sum().reset_index()

italyGraph = go.Figure()

italyGraph.add_trace(go.Scatter(x=italy.Date, y=italy['Confirmed'], name="Confirmed Cases",
                         line_color='blue'))

italyGraph.add_trace(go.Scatter(x=italy.Date, y=italy['Deaths'], name="Deaths Cases",
                         line_color='red'))

italyGraph.add_trace(go.Scatter(x=italy.Date, y=italy['Recovered'], name="Recovered Cases",
                         line_color='green'))

italyGraph.update_layout(
    title={
        'text': "Time Series for Italy",
        'y':0.9,
        'x':0.45,
        'xanchor': 'center',
        'yanchor': 'top'})

italyGraph.show()