# Starbucks Capstone Challenge
Project in Data Scientist Nanodegree of Udacity

## Installation <a name="installation"></a>

Python Anaconda distribution  
Streamlit version 0.62  

## Project Motivation<a name="motivation"></a>

It is the Starbuck's Capstone Challenge of the Data Scientist Nanodegree in Udacity. We get the dataset from the program that creates the data simulates how people make purchasing decisions and how those decisions are influenced by promotional offers. We want to make a recommendation engine that recommends Starbucks which offer should be sent to a particular customer.

Our area of interest.

Understanding what offers could be successful for different demographics
and create an app that provides a list with the offers that were more likely to produce a higher monetary benefit.  

## Strategy for solving the problem

1.Our data first need to be cleaned and transformed into a dataset that can be analysed.  
2. Our data then will be used into creating a simple recommendation
system  
3. The output of the data will be presented in an app that will allow the user to see the most succesful offers for the different demographics

## Metrics

To generate the most succcesful offer we will use net_expense as a metric to maximise.


## File Descriptions <a name="files"></a>

The notebook available here showcases work related to the above questions.  

This data set is a simplified version of the real Starbucks app because the underlying simulator only has one product whereas Starbucks actually sells dozens of products.

The data is contained in three files:
- `portfolio.json` - containing offer ids and meta data about each offer (duration, type, etc.)
- `profile.json` - demographic data for each customer
- `transcript.json` - records for transactions, offers received, offers viewed, and offers completed

Here is the schema and explanation of each variable in the files:

`portfolio.json`
- id (string) - offer id
- offer_type (string) - the type of offer ie BOGO, discount, informational
- difficulty (int) - the minimum required to spend to complete an offer
- reward (int) - the reward is given for completing an offer
- duration (int) - time for the offer to be open, in days
- channels (list of strings)

`profile.json`
- age (int) - age of the customer
- became_member_on (int) - the date when customer created an app account
- gender (str) - gender of the customer (note some entries contain 'O' for other rather than M or F)
- id (str) - customer id
- income (float) - customer's income

`transcript.json`
- event (str) - record description (ie transaction, offer received, offer viewed, etc.)
- person (str) - customer id
- time (int) - time in hours since the start of the test. The data begins at time t=0
- value - (dict of strings) - either an offer id or transaction amount depending on the record


## Results<a name="results"></a>

The result of the project is a simple app that recommends offers that maximaze customer expense based on the selected demographics and has been deployed on heroku here:

 https://starbucksprojectapp.herokuapp.com/

## Steps on how to use the app

In the app environment on the above link change the different filters into the audience that you want to target and the table will show you the recommendation for the offers that would maximise net expense for this demographic.

To recreate the app environment you would need to dowload Streamlit   

> pip install streamlit

Then run the clean_data_2.py inside the directory
> python clean_data_2.py

Final Step
in the terminal inside the directory run the app file  

> streamlit run app.oy

## Conclusions and way forward

Based on my initial findings, demographics play a big role in how successful an
offer will be. With our simple recommendation system we are able to see which offers would
generate higher value for starbucks based on the characteristics of the audience.

As a next step and how we could go about improving this app, I would love to
create some graphs in the app so that we can understand potential gain from
targeting a certain audience with some selected offers and as a step even further
I would like to create different filters for offer details so that someone in marketing
creating the characteristics of an offer can understand the effects of an offer to the
audience they are aiming to send their offer on.


## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Special thanks to the udacity community for helping out with parts of the code

MIT Licence
