pipeline {
    agent any

    stages {
        stage('Build Docker image') {
            steps {
                sh 'docker build -t dmsuprun/fastapi-app:latest .'
            }
        }
        stage('Test application'){
            steps{
                sh 'docker run --rm dmsuprun/fastapi-app pytest'

            }
        }

        stage('Run container') {
            steps {

                sh 'docker run -d -p 8000:8000 dmsuprun/fastapi-app:latest'
            }
        }
    }
}
