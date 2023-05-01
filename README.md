# otp-mail
creating django app for sending otp via gmail
1) create a virtual environment using command 
     "python -m venv "folder name"
2) activate the environment by 
     folder name/Scripts/activate 
      run the activate command by cmd
3) install needed packaged by
     " pip install -r requirements.txt"
4) after that open views.py 
 there you can add your receiver email id in to string
5) then open settings.py in auth folder
   In line 129 and 130 you can add your sender Gmail and app password respectively
To create app password goto manage your Google account and goto security section and there add a new app and password
You can only see the app password section of you enabled two step verification for your account
6) to run the sever 
  "python manage.py runserver
   @ browser direct to /mail and there you go
