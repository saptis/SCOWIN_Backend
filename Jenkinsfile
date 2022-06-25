pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                withPythonEnv('python') {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'python manage.py runserver'
            }
        }
    }
}
