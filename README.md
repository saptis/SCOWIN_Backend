# SCOWIN_Backend

1) Fork out the repository from GIT
2) Clone the web app repository into local system using following command
```
git clone https://github.com/saptis/ SCOWIN_backEnd.git
```
3) Enter into the directory created
```
cd SCOWN_backEnd
```
4) Create a virtual environment
```
virtualenv < virtual_env_name_of_your_choice>
```
For example, virtualenv scowin_venv

5) Activate the virtual environment
```
cd <virtual_env_name_of_your_choice>/scripts
activate
```
6) Go back to SCOWIN_backEnd directory
```
cd../..
```
7) Run pip install command
```
pip install -r requirements.txt
```
8) Run following python scripts
```
python manage.py makemigrations
python manage.py migrate
```
9) Need to create superuser. Run the following command and follow the instruction on screen
```
python manage.py createsuperuser
```
10) Run Django server
```
python manage.py runserver
```
