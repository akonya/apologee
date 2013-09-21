##API routes

####/API/signup
Signup a new user

* consumes GET data for `username`,`password`,`email`
* returns `{"status": 1}` if account successfully created
* returns `{"status": 2}` if username already exists
* returns `{"status": 0}` unknown failure

if status = 1 retuns `token`

EXAMPLE:

`[{"token": "CzswGnCLM4yQi9E7zJcGpPfGq"}, {"status": 1}]`

---

####/API/login
Login/authenticate user + obtain token

* consumes GET data for `username`,`password`
* returns `{"status": 1}` if authentication successfull
* returns `{"status": 2}` if authentication fail
* returns `{"status": 0}` unknown failure

if status = 1 retuns `token`

EXAMPLE:

`[{"token": "DQNNj15xQFpuXSHl8HNFt5Rnc"}, {"status": 1}]`

---

####/API/sorry
Submit an appology

* consumes GET data for `token`,`sendto`
* `sendto` is the name of the person appology is sent to

* returns `{"status": 1}` if authentication successfull & appology sent
* returns `{"status": 2}` if authentication fail
* returns `{"status": 3}` if authentication successfull & appology sent & mutual
* returns `{"status": 0}` unknown failure

---

####/API/accepted
Get list of people who accepted appologies

* consumes GET data for `token`
* returns list of people who accepted appologies
* returns `{"status": 1}` if authentication successfull
* returns `{"status": 2}` if authentication fail
* returns `{"status": 0}` unknown failure

EXAMPLE:

`[{"acceptedby": "obama"}, {"status": 1}]`

---

