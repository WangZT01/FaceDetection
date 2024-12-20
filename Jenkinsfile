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
                publishChecks name: env.GITHUB_CHECK_NAME,
                              status: 'COMPLETED',
                              conclusion: 'SUCCESS',
                              summary: 'Build and tests passed successfully!',
                              text: 'All tests passed and the build completed successfully.'
            }
        }
        failure {
            script {
                publishChecks name: env.GITHUB_CHECK_NAME,
                              status: 'COMPLETED',
                              conclusion: 'FAILURE',
                              summary: 'Build or tests failed.',
                              text: 'Some tests failed or the build did not complete successfully.'
            }
        }
    }
}