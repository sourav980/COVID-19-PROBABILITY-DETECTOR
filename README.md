# COVID-19 PROBABILITY DETECTOR

Assessment of user for Covid-19 based on symptoms using Machine Learning approach.

## Getting Started

### Prerequisites

- Python version above 3.0
- Python pip
- Please enable the less secure app access on your Gmail
- Please do enter your mail id and email-password in line no 203 in login_page.py file

### Summary
#### LOGIN PAGE
- User enters his email and password and is redirected to the Main page.
- If the user forgets his password he can click on forgot password and is redirected to the forgot password verification page.

#### FORGOT PASSWORD PAGE
- The user enters the registered email to recieve the Generated OTP code. 
- The user is then redirected to a new page where user can enter the new password.

#### REGISTER PAGE
- User must enter valid email, username, password and phone number(optional).

#### MAIN PAGE
- The user enters the symptoms experienced and gets a probability data of being infected.
   
#### REPORT PAGE 
- Provides user with feature of producing historical report.

### Installation

To install application:

1. Clone the repository.

   `git clone https://github.com/sourav980/COVID-19-PROBABILITY-DETECTOR.git`

2. Install pipenv for creating virtual environments.

   `pip install pipenv`

### Execution
For executing the application.

#### Note: mytraining.py must be executed before running login_page.py
 
- `pipenv run python mytraining.py`
- `pipenv run python login_page.py`