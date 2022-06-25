pipeline {
    agent any

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
                    withPythonEnv('/usr/bin/python3.7'){
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
                    withPythonEnv('/usr/bin/python3.7'){
		            sh 'pip3 install --no-cache-dir -r requirements.txt'
		            sh 'python3 manage.py runserver'
			        }
		        }
            }
        }
    }
}
