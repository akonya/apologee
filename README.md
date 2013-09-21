##API routes

####/API/signup
Signup a new user

EXAMPLE REQUEST:

`http://apologee.herokuapp.com/API/signup?username=jake%20tobin&password=password&email=jake@tob.in`

* consumes GET data for `username`,`password`,`email`
* returns `{"status": 1}` if account successfully created
* returns `{"status": 2}` if username already exists
* returns `{"status": 0}` unknown failure

if status = 1 retuns `token`

EXAMPLE RESPONSE:

`[{"token": "CzswGnCLM4yQi9E7zJcGpPfGq"}, {"status": 1}]`

---

####/API/login
Login/authenticate user + obtain token

EXAMPLE REQUEST:

`http://apologee.herokuapp.com/API/login?username=jake%20tobin&password=password`

* consumes GET data for `username`,`password`
* returns `{"status": 1}` if authentication successfull
* returns `{"status": 2}` if authentication fail
* returns `{"status": 0}` unknown failure

if status = 1 retuns `token`

EXAMPLE RESPONSE:

`[{"token": "DQNNj15xQFpuXSHl8HNFt5Rnc"}, {"status": 1}]`

---

####/API/sorry
Submit an appology

EXAMPLE REQUEST:

`http://apologee.herokuapp.com/API/sorry?token=andrew konyaKO1N7PTPfyZA7UtD1d78iUcrf&sendto=jake tobin&message=Lets be friends!`

* consumes GET data for `token`,`sendto`,`message`
* `sendto` is the name of the person appology is sent to
* returns `{"status": 1}` if authentication successfull & appology sent
* returns `{"status": 2}` if authentication fail
* returns `{"status": 3}` if authentication successfull & appology sent & mutual
* returns `{"status": 4}` if appology `message` has overly negative sentiment
* returns `{"status": 0}` unknown failure

---

####/API/accepted
Get list of people who accepted appologies

EXAMPLE REQUEST:

`http://apologee.herokuapp.com/API/accepted?token=andrew konyaKO1N7PTPfyZA7UtD1d78iUcrf`

* consumes GET data for `token`
* returns list of accepted appologees

Each apologee in list has:

`message` --> appology message
`from` --> who sent the apologee

* returns `{"status": 1}` if authentication successfull
* returns `{"status": 2}` if authentication fail
* returns `{"status": 0}` unknown failure

EXAMPLE RESPONSE:

`[{"message": "\"I love you Obama\"", "from": "putin"}, {"status": 1}]`

---

