pipeline {
    agent any

    stages {
        stage('Copy to server') {
            steps {
                echo 'Building..'
                withPythonEnv('python') {
                    sh 'rm -rf /home/scowin-api/'
                    sh 'cp -Rf /var/jenkins_home/workspace/scowin-api /home/scowin-api'
                    sh 'cd /home/scowin-api'
                }
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
                withPythonEnv('python') {
                    sh 'pip3 install --no-cache-dir -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                script {
                    withPythonEnv('python'){
		            sh 'python3 manage.py test'
			        }
		        }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                script {
                    withPythonEnv('python'){
                sh 'python3 manage.py makemigrations'
			    sh 'python3 manage.py migrate'
			    sh 'pkill -f runserver'
			    sh 'python3 manage.py runserver 0.0.0.0:8000'
			   }
		        }
            }
        }
    }
}