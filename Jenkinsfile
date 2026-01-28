pipeline {
    agent any

    stages {
        stage('Build Docker image') {
            steps {
                sh 'docker build -t dmsuprun/fastapi-app:latest .'
            }
        }

        stage('Run container') {
            steps {
                sh 'docker stop fastapi || true'
                sh 'docker rm fastapi || true'
                sh 'docker run -d -p 8000:8000 --name fastapi dmsuprun/fastapi-app:latest'
            }
        }
    }
}