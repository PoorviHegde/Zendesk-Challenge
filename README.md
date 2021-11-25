# Zendesk-Challenge
 Zendesk Coding Challenge

TICKET VIEWER APPLICATION

It is an application that connects with Zendesk organization account to fetch all the tickets for an agent and display them. This application is built using python 
Django framework. 

To use the application:

Step1:
You need to have all the dependencies installed to run this app. Firstly, make sure you have python 3 installed. Then run the following command from inside 
Zendesk app directory to install the remaining dependencies:

"pip install -r requirements.txt"

This will install all the dependencies mentioned in 'requirements.txt'

Step2:
You need to make sure that you can connect to your account without any issue. Navigate to 'zendesk_ticket_viewer' inside the 'Zendesk Challenge' directory. 
There is a file named 'auth.py'. Open this in the text editor of your choice (ex-sublime text,VS Code, Notepad++). Between the "" for each variable, add the 
value corresponding to your account.

For example if your username is 'User', password is 'pass' and subdomain is 'zcczendeskintern', edit as-
USERNAME = 'User'
PASSWORD = 'pass'
SUB_DOMAIN = 'zcczendeskintern'

Step3:
Open a terminal and make sure you are still in the 'zendesk_ticket_viewer' directory. Run the following command-

"python manage.py runserver"

This will launch the aplication on your localhost. Default port is 8000

Step4:
Open a browser of your choice and copy-paste the following url-

"http://127.0.0.1:8000/"


You are all set! You should be able to view all the tickets created for your account in a table. To view the details of a particular ticket, just click on the id 
number of that ticket.

Hope you enjoyed using the application!

