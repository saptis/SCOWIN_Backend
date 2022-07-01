rm -rf /home/scowin-api/
cp -Rf /var/jenkins_home/workspace/scowin-api /home/scowin-api
cd /home/scowin-api


pip3 install --no-cache-dir -r requirements.txt

python3 manage.py test

python3 manage.py makemigrations
python3 manage.py migrate
pkill -f runserver
nohup python3 manage.py runserver 0.0.0.0:8081 &
