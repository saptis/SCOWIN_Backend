pipeline {
    agent any

    stages {
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