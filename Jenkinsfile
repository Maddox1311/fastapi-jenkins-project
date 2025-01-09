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
                python -m venv /mnt/d/MyCode/myvenv
                source mnt/d/MyCode/myvenv/Scripts/activate
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '''
                source mnt/d/MyCode/myvenv/Scripts/activate
                pytest
                '''
            }
        }

        stage('Run Application') {
            steps {
                echo 'Starting FastAPI application...'
                sh '''
                source mnt/d/MyCode/myvenv/Scripts/activate
                uvicorn main:app --host 0.0.0.0 --port 8000
                '''
            }
        }
    }
}
