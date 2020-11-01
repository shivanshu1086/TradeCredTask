# django-tradecred
You can able to upload data in this application and view the uploaded data. There are constraints with them too: like duplicates entries, no data inserted, etc.

# Installation:

# Activate the virtual envirenment first,
Install virtualenv
virtualenv is a virtual environment where you can install software and Python packages in a contained development space, which isolates the installed software and packages from the rest of your machine’s global environment. This convenient isolation prevents conflicting packages or software from interacting with each other.

To install virtualenv, we will use the pip3 command, as shown below:
```
pip3 install virtualenv
```
While inside the root directory, create your virtual environment. Let’s call it env.
```
virtualenv env
```
Now, activate the virtual environment with the following command:
```
. env/bin/activate
```

* Install the latest version of django by using:
```
pip install django
```
* Run the command to install the additional packages
```
pip install -r requirements.txt
```


# After doing everything run the following commands:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py runserver
```
and now open any browser and go to the link:
```
http://127.0.0.1:8000/
```
your website will be running at this link if everything went right!


&copy; Shivanshu Bajpai
