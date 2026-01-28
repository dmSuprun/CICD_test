pipeline {
    agent any

    stages {
        stage('Build Docker image') {
            steps {
                bat 'docker build -t dmsuprun/fastapi-app:latest .'
            }
        }
        stage('Test application'){
            steps{
                bat 'docker run --rm dmsuprun/fastapi-app pytest'

            }
        }

        stage('Run container') {
            steps {

                bat 'docker run -d -p 8000:8000 dmsuprun/fastapi-app:latest'
            }
        }
    }
}