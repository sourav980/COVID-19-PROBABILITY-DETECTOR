# COVID-19 PROBABILITY DETECTOR

Assessment of probability of Covid-19 of a person based on his symptoms using machine learning approach.

## Getting Started

### Prerequisites

- Python version above 3.0
- Python pip

### Summary
#### LOGIN PAGE
- User enters his email and password and is redirected to the Main page.
- If the user forgets his password he can click on forgot password and is redirected to the forgot password verification page.

#### FORGOT PASSWORD PAGE
- The user must enter the email to recieve the Generated OTP code. The page gets redirected to a new page where user can enter the new password.

#### REGISTER PAGE
- User must enter valid email, username, password and phone number(optional).

#### MAIN UI PAGE
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