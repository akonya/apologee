##API routes

####/API/signup

* consumes GET data for `username`,`password`,`email`
* returns `{"status": 1}` if account successfully created
* returns `{"status": 2}` if username already exists
* returns `{"status": 0}` unknown failure

if status = 1 retuns `token`

EXAMPLE:

`[{"token": "CzswGnCLM4yQi9E7zJcGpPfGq"}, {"status": 1}]`

---

####/API/login

* consumes GET data for `username`,`password`
* returns `{"status": 1}` if authentication successfull
* returns `{"status": 2}` if authentication fail
* returns `{"status": 0}` unknown failure

if status = 1 retuns `token`

EXAMPLE:

`[{"token": "DQNNj15xQFpuXSHl8HNFt5Rnc"}, {"status": 1}]`

