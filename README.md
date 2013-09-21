##API routes

####/API/signup

* consumes GET data for `username`,`password`,`username`
* returns `{"status": 1}` if account successfully created
* returns `{"status": 2}` if username already exists
* returns `{"status": 0}` unknown failure

if status = 1 retuns `token`

EXAMPLE:

`[{"token": "CzswGnCLM4yQi9E7zJcGpPfGq"}, {"status": 1}]`


