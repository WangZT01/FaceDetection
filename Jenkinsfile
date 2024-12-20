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
                        context: 'continuous-integration/jenkins-1',
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
                        context: 'continuous-integration/jenkins-2',
                        message: 'run-test',
                    )
                }
            }
        }
        stage('Run Tests') {
            steps {
                echo "Running tests..."
                sh 'sleep 10'
            }
        }
    }
    post {
        success {
            script {
                setGitHubPullRequestStatus(
                    state: 'SUCCESS',
                    context: 'continuous-integration/jenkins-success',
                    message: 'Build succeeded!',
                )
            }
        }
        failure {
            script {
                setGitHubPullRequestStatus(
                    state: 'FAILURE',
                    context: 'continuous-integration/jenkins-failed',
                    message: 'Build failed!',
                )
            }
        }
    }
}