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
                bat 'docker stop fastapi || true'
                bat 'docker rm fastapi || true'
                bat 'docker run -d -p 8000:8000 --name fastapi dmsuprun/fastapi-app:latest'
            }
        }
    }
}