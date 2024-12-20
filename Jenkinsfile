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
                    setGitHubPullRequestStatus(
                        unstableAs: 'PENDING',
                        content: 'continuous-integration/jenkins',
                        buildMessage: 'Debug',
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
                    setGitHubPullRequestStatus(
                        unstableAs: 'PENDING',
                        content: 'continuous-integration/jenkins',
                        buildMessage: 'Build is starting...',
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
                setGitHubPullRequestStatus(
                    unstableAs: 'SUCCESS',
                    content: 'continuous-integration/jenkins',
                    buildMessage: 'Build succeeded!',
                )
            }
        }
        failure {
            script {
                setGitHubPullRequestStatus(
                    unstableAs: 'FAILURE',
                    content: 'continuous-integration/jenkins',
                    buildMessage: 'Build failed!',
                )
            }
        }
    }
}