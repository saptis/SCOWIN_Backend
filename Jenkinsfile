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
                sh 'virtualenv env -p python3.5'
                sh '. env/bin/activate'
                sh 'env/bin/pip install -r requirements.txt'
                sh 'env/bin/python3.5 manage.py test'
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
