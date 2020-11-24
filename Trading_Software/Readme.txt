REQUIREMENTS--------------------------------------------------------------------------------------

Libraries to be Installed:
1.Tkinter
2.Aplha Vantage 
3.Numpy
4.Pandas
5.MatplotLib
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 ONLY INSTALL IF YOU WANT TO RUN PREICTION PROGRAM TOO(Machine Learning):
1.Sklearn
2.Keras
 ***there is a limitation of prediction program that it is not connected with GUI because it is
still in development.
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
API Limitations:
for Free it can only give 5 requests per minute and 500 requests a day and there is no LIVE DATA
AVAILABLE FOR FREE. it costs around Rs.20,000 for  live data for a week.
so if you  have premium API then just change the Code in the file Named: Select_company.py
GOTO ALPHA VANTAGE FOR YOUR FREE API.

----------------------------HOW TO USE----------------------------------------------------------
1. Open any editor and Run the file Named :prototype.py
2. A GUI will open click on "Click to make a new Analysis" to Open another window or click "close" button to end the program but this will close any child window too.
3.A new GUI will get opened asking for user inputs 
in the Box named:'Enter company name '- Tesla,Apple(these 2 are valid as of now but others can be 							added too).
	Enter Time:'60min','30min','5min','1min' (these are only valid for the API and do write 			'MIN' after the digits)
	Enter Type: high,low,close,open (these are trading terms).
	Enter Date: 22-10-2020,26-10-2020 (Becareful with the dates because trading on intradays 					works on diffrent dates so every date is not a valid date 					so make sure it is an intraday date of trading).
in SHORT SAMPLE INPUT IS:
Tesla
60min
high
22-10-2020

Apple 
60min
high
26-10-2020

* Click "Get stocks graph button"*
A graph will be show to you in the new window where you can make your next strategy .

USER DATA NOTICE:
this program collects user data and save it in  SQL data base in the future it will be connected to a cloud SQL database to disable this function gotoline:66 of Prototype.py and remove it so it wont call that function.Right now make script to make your own database for collection is provided here.

create database whatever_your_DB_name_is

use whatever_your_DB_name_is

create table user_data(id bigint auto_increment,Company_name varchar(32) not null,duration varchar(32),primary key(id));
**this will create your database and table. Make corrections to the credentials.py file to change your database name
-------------------------------------LIMITATIONS--------------------------------------------------
1. i havenot programmed Try catch block yet due to testing my program.
2. it only has intraday trading due to api restrictions and mostly trader are looking for intraday   intervals so i chose intraday but you can change  it in the program :select_company.py
3. Other buttons such as SMA,EMA ,WMA are not working that exceeds my quota of 5 calls per minute 
 and program might crash.
--------------------------------------------------------------------------------------------------
for any other queries email me @ : manas.vishnoi@gmail.com or my github profile RaidenKnights

thanks for using and bearing this miracle of technology :)
