# Test App
task link: https://gist.github.com/martinOpply/c0b496ae1c52ec24899b58bea6b4708d

# Install 
>> pip install -r requirements.txt

>> python manage.py makemigrations

>> python manage.py migrate 

Make sure you, that products was created by admin panel
>> python manage.py runserver 

# Heroku deploy
>> heroku create -a test-app

Add a remote to your local repository with the heroku git:remote command.
>> heroku git:remote -a test-app

Deploy heroku app
>> git push heroku main


