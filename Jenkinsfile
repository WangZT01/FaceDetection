pipeline {
    agent any
    environment {
        GITHUB_API_URL = 'https://api.github.com'
        REPO = 'WangZT01/FaceDetection'
        GITHUB_TOKEN = credentials('peter-github-ssh')
    }
    stages {
        stage('Checkout') {
            steps {
                script {
                    // 检查是否为 Pull Request 构建
                    if (env.CHANGE_ID) {
                        echo "Building Pull Request: ${env.CHANGE_ID}"
                    } else {
                        echo "Building branch: ${env.BRANCH_NAME}"
                    }
                }
                // 拉取代码
                checkout scm
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