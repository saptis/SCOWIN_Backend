pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Testing..'
                script {
		            withPythonEnv('python'){
		            sh 'pip3 install --no-cache-dir -r requirements.txt'
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
		            sh 'docker-compose build'
		            sh 'docker-compose up'
		        }
                }
            }
        }
    }
}
