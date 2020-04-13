Instruction
------------

python 3.7 does't work
so i have used 3.6.5
https://stackoverflow.com/questions/51726203/installing-python3-6-alongside-python3-7-on-mac
brew install pyenv
pyenv install 3.6.9
pyenv install 3.7.4
pyenv versions
pyenv global 3.7.4 3.6.9

/Users/cdh/.pyenv/versions/3.6.5/bin//python


followed instruction from : https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html

In Mac you kept venv outside the project
/Users/cdh/DJANGO/virtualenvs/cri

to install venv and to activate
>>>>> virtualenv cri -p python3
>>>>> source cri/bin/activate


Install django now
>>>>> pip install django

Create project now
>>>>> django-admin startproject project_cri

Create app cri
>>>>>  django-admin startapp cri

For this project we are using existing mysql DB  instead of sqllite built it DB provided by Django
So
step 1 : modify the settings.py to read from customDB.(https://docs.djangoproject.com/en/3.0/ref/settings/)
step 2 : It demands MySQLdb module.
        Once you install mysqlclient (read mysql_on_mac.txt)
        as first step : pip install mysqlclient.
        and python3 does't support MySQLdb as alternative.
            pip install pymysql
        then
            go to project_cri/__innit__.py
            place below lines

            -------------------
            import pymysql
            pymysql.version_info = (1, 3, 13, "final", 0)
            pymysql.install_as_MySQLdb()
            -------------------
           refer : https://stackoverflow.com/questions/55657752/django-installing-mysqlclient-error-mysqlclient-1-3-13-or-newer-is-required

step 3 : generate models.py from existing tables of existing DB using below command
        python manage.py inspectdb CRI_PROJECT CRI_BRANCH CRI_SERVER CRI_REFINEMENT_TYPE CRI_REFINEMENT_STATE CRI_PROJECT_CONFIG CRI_BRANCH_CONFIG CRI_REQUEST CRI_STATUS  > cri/models.py

        then try migrations
        python manage.py makemigrations
        >>> faced some issues.
           SystemCheckError: System check identified some issues:

        ERRORS:
        cri.CriStatus.patch_status: (fields.E304) Reverse accessor for 'CriStatus.patch_status' clashes with reverse accessor for 'CriStatus.refinement_state'.
	    HINT: Add or change a related_name argument to the definition for 'CriStatus.patch_status' or 'CriStatus.refinement_state'.
        cri.CriStatus.refinement_state: (fields.E304) Reverse accessor for 'CriStatus.refinement_state' clashes with reverse accessor for 'CriStatus.patch_status'.
	    HINT: Add or change a related_name argument to the definition for 'CriStatus.refinement_state' or 'CriStatus.patch_status'.

	    >>> to fix this we have disabled reversing (https://stackoverflow.com/questions/41595364/fields-e304-reverse-accessor-clashes-in-django)
	        https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ForeignKey.related_name

	    and modified CriStatus model with below content
        refinement_state = models.ForeignKey(CriRefinementState, models.DO_NOTHING, db_column='REFINEMENT_STATE_ID', related_name='+' )
        patch_status = models.ForeignKey(CriRefinementState, models.DO_NOTHING, db_column='PATCH_STATUS', related_name='+' )

        Then
        python manage.py makemigrations

         went fine this time.

setting up multiple DBs refer below link 
#https://www.protechtraining.com/blog/post/tutorial-using-djangos-multiple-database-support-477

#Note once yousetup dbrouter and setting.py you need to do python manage.py makemigration and python manage.py  migrate to take effect.
