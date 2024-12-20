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
                        state: 'PENDING',
                        context: 'continuous-integration/jenkins',
                        message: 'Debug',
                        credentialsId: "${GITHUB_CREDENTIALS}"
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
                        state: 'PENDING',
                        context: 'continuous-integration/jenkins',
                        message: 'Build is starting...',
                        credentialsId: "${GITHUB_CREDENTIALS}"
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
                    state: 'SUCCESS',
                    context: 'continuous-integration/jenkins',
                    message: 'Build succeeded!',
                    credentialsId: "${GITHUB_CREDENTIALS}"
                )
            }
        }
        failure {
            script {
                setGitHubPullRequestStatus(
                    state: 'FAILURE',
                    context: 'continuous-integration/jenkins',
                    message: 'Build failed!',
                    credentialsId: "${GITHUB_CREDENTIALS}"
                )
            }
        }
    }
}