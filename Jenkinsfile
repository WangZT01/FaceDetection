pipeline {
    agent any
    environment {
        GITHUB_API_URL = 'https://api.github.com'
        REPO = 'WangZT01/FaceDetection'
        GITHUB_TOKEN = credentials('peter-github-ssh')
        GITHUB_CHECK_NAME = 'Jenkins CI'
        CONTEXT_NAME = 'continuous-integration/jenkins'
    }
    stages {
        stage('Debug Webhook') {
            steps {
                script {

                    githubPRStatusPublisher state: 'PENDING',
                                               context: "${CONTEXT_NAME}",
                                               message: 'Checking out code...'
                    echo "Environment Variables:"
                    sh 'env'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    githubPRStatusPublisher state: 'PENDING',
                                               context: "${CONTEXT_NAME}",
                                               message: 'Building the project...'
                    echo "Running tests..."
                }
            }
        }
    }
    post {
        success {
            script {
                githubPRStatusPublisher state: 'SUCCESS',
                                           context: "${CONTEXT_NAME}",
                                           message: 'Build succeeded!'
            }
        }
        failure {
            script {
                githubPRStatusPublisher state: 'FAILURE',
                                           context: "${CONTEXT_NAME}",
                                           message: 'Build failed!'
            }
        }
    }
}