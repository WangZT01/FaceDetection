pipeline {
    agent any
    environment {
        GITHUB_API_URL = 'https://api.github.com'
        REPO = 'WangZT01/FaceDetection'
        GITHUB_TOKEN = credentials('peter-github-ssh')
        GITHUB_CHECK_NAME = 'Jenkins CI'
        CONTEXT_NAME = 'continuous-integration/jenkins'
        GITHUB_CREDENTIALS = 'peter-github-ssh'
    }
    stages {
        stage('Set Pending Status') {
            steps {
                script {
                    githubPRStatusPublisher(
                        state: 'PENDING',
                        context: 'continuous-integration/jenkins',
                        message: 'Debug',
                    )
                }
            }
        }
        stage('Debug Webhook') {
            steps {
                script {
                    echo "Environment Variables:"
                    sh 'env'
                }
            }
        }
        stage('Set Pending Status - run') {
            steps {
                script {
                    githubPRStatusPublisher(
                        state: 'PENDING',
                        context: 'continuous-integration/jenkins',
                        message: 'run-test',
                    )
                }
            }
        }
        stage('Run Tests') {
            steps {
                echo "Running tests..."
            }
        }
    }
    post {
        success {
            script {
                githubPRStatusPublisher(
                    unstableAs: 'SUCCESS',
                    content: 'continuous-integration/jenkins',
                    buildMessage: 'Build succeeded!',
                )
            }
        }
        failure {
            script {
                githubPRStatusPublisher(
                    unstableAs: 'FAILURE',
                    content: 'continuous-integration/jenkins',
                    buildMessage: 'Build failed!',
                )
            }
        }
    }
}