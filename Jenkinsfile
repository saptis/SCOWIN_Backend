pipeline {
    agent {
      docker {
        image 'python:3'
        label 'python-env'
      }
    }

    stages {
        // stage('Build') {
        //     steps {
        //         echo 'Building..'
        //         withPythonEnv('python') {
        //             sh 'pip install -r requirements.txt'
        //         }
        //     }
        // }
        stage('Test') {
            steps {
                echo 'Testing..'
                script {
		            sh 'pip3 install --no-cache-dir -r requirements.txt'
		            sh 'python3 manage.py test'
		        }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                script {
		            sh 'pip3 install --no-cache-dir -r requirements.txt'
		            sh 'python3 manage.py runserver'
		        }
            }
        }
    }
}
