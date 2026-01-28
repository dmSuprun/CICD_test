pipeline {
    agent any

    stages {
        stage('Build Docker image') {
            steps {
                bat 'docker build -t dmsuprun/fastapi-app:latest .'
            }
        }

        stage('Run container') {
            steps {

                bat 'docker run -p 8888:8888 dmsuprun/fastapi-app:latest'
            }
        }
    }
}