pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/janhavix/fastapi-task-manager.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t fastapi-app .'
            }
        }

    }
}