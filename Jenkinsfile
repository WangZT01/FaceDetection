pipeline {
    agent any
    environment {
        GITHUB_API_URL = 'https://api.github.com'
        REPO = 'WangZT01/FaceDetection'
        GITHUB_TOKEN = credentials('peter-github-ssh')
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
                // 通知 GitHub 状态为成功
                sh """
                curl -X POST -H "Authorization: token $GITHUB_TOKEN" \
                     -H "Content-Type: application/json" \
                     -d '{
                            "state": "success",
                            "description": "All tests passed",
                            "context": "continuous-integration/jenkins"
                         }' \
                     $GITHUB_API_URL/repos/$REPO/statuses/$GIT_COMMIT
                """
            }
        }
        failure {
            script {
                // 通知 GitHub 状态为失败
                sh """
                curl -X POST -H "Authorization: token $GITHUB_TOKEN" \
                     -H "Content-Type: application/json" \
                     -d '{
                            "state": "failure",
                            "description": "Tests failed",
                            "context": "continuous-integration/jenkins"
                         }' \
                     $GITHUB_API_URL/repos/$REPO/statuses/$GIT_COMMIT
                """
            }
        }
    }
}