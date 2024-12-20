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

                    setGitHubPullRequestStatus state: 'PENDING',
                                               context: "${CONTEXT_NAME}",
                                               message: 'Checking out code...'
                }
                script {
                    echo "Environment Variables:"
                    sh 'env'
                    // Webhook Payload
                    if (env.GITHUB_PAYLOAD) {
                        def payload = readJSON text: env.GITHUB_PAYLOAD
                        echo "Webhook Payload: ${payload}"
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    setGitHubPullRequestStatus state: 'PENDING',
                                               context: "${CONTEXT_NAME}",
                                               message: 'Building the project...'
                }
                echo "Running tests..."
            }
        }
    }
    post {
        success {
            script {
                setGitHubPullRequestStatus state: 'SUCCESS',
                                           context: "${CONTEXT_NAME}",
                                           message: 'Build succeeded!'
            }
        }
        failure {
            script {
                setGitHubPullRequestStatus state: 'FAILURE',
                                           context: "${CONTEXT_NAME}",
                                           message: 'Build failed!'
            }
        }
    }
}