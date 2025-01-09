pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                python -m venv myvenv
                source myvenv/bin/activate
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '''
                source myvenv/bin/activate
                pytest
                '''
            }
        }

        stage('Run Application') {
            steps {
                echo 'Starting FastAPI application...'
                sh '''
                source myvenv/bin/activate
                uvicorn main:app --host 0.0.0.0 --port 8000
                '''
            }
        }
    }
}
