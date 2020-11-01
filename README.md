# COVID-19 PROBABILITY DETECTOR

INFORMATION ABOUT  COVID-19 PROBABILITY DETECTOR.

-ASSESSMENT OF PROBABILITY OF COVID-19 OF A PERSON BASED ON HIS SYMPTOMS USING MACHINE LEARNING 


## Getting Started

### Prerequisites

- Python version above 3.0
- Python pipenv 
- Python pip



### LOGIN PAGE
--1)User enters his email and password then page is redirected to the Main UI page
--2)If the user forgets his password he can click on forgot password page and the page gets redirected to the forgot password verification page

#### FORGOT PASSWORD PAGE
 --1)The user must enter the email to recieve the Generated OTP code from python
   2)Once he enters the code the page gets redirected to a new page where he can enter his new password and it get saved in the database


### REGISTER PAGE
--1)User must enter valid email,his username,password and phone number(optional).If the mail or password is not correct then it will be dispalyed invalid email_id or invalid password 
  2)The data entered from user is stored in the database

#### MAIN UI PAGE
   --1)On this page the user enters the symptoms he experiences and when he clicks on the submit button the page gets redirected to a new webpage where probability of 
       that person having covid-19 is shown
   --2)He also have an option to click on report button,logout,signup page
   
### REPORT PAGE 
  --1)The report page displays all the reports the user  have generated from day 1 on the app,basically it is a history of all his reports



### Installation

To install application:

1. Clone the repository.

   'git clone https://github.com/sourav980/COVID-19-PROBABILITY-DETECTOR.git'

2. Install pipenv for creating virtual environments.

   `pip install pipenv`

### Execution
 For executing the application.
 1)pipenv run python mytraining.py
2)pipenv run python login_page.py
  Note:mytraining.py must be executed before running login_page.py

