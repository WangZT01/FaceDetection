pipeline {
    agent any
    environment {
        GITHUB_API_URL = 'https://api.github.com'
        REPO = 'WangZT01/FaceDetection'
        GITHUB_TOKEN = credentials('peter-github-ssh')
    }
    stages {
        stage('Parse PR Review Event') {
            steps {
                script {
                    // 解析 Webhook Payload，检查是否为 PR Review 创建事件
                    if (env.GITHUB_PAYLOAD) {
                        def payload = readJSON text: env.GITHUB_PAYLOAD
                        if (payload.action == 'submitted' && payload.review) {
                            echo "Pull Request Review Created: Starting tests..."
                        } else {
                            echo "Not a PR Review creation event. Skipping build."
                            currentBuild.result = 'NOT_BUILT'
                            return
                        }
                    } else {
                        error "No Webhook Payload found."
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