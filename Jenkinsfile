pipeline {
    agent any
    environment {
        GITHUB_API_URL = 'https://api.github.com'
        REPO = 'WangZT01/FaceDetection'
        GITHUB_TOKEN = credentials('peter-github-ssh')
        GITHUB_CHECK_NAME = 'Jenkins CI'

    }
    stages {
        stage('Debug Webhook') {
            steps {
                script {
                    echo "Environment Variables:"
                    sh 'env' // 打印所有环境变量

                    // 检查 Webhook Payload
                    if (env.GITHUB_PAYLOAD) {
                        def payload = readJSON text: env.GITHUB_PAYLOAD
                        echo "Webhook Payload: ${payload}"
                    } else {
                        echo "No Webhook Payload found."
                    }
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
                setGitHubPullRequestStatus state: 'SUCCESS',
                                           context: 'continuous-integration/jenkins',
                                           message: 'Build succeeded!'
            }
        }
        failure {
            script {
                setGitHubPullRequestStatus state: 'FAILURE',
                                           context: 'continuous-integration/jenkins',
                                           message: 'Build failed!'
            }
        }
    }
}