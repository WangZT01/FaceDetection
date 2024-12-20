pipeline {
    agent any
    environment {
        GITHUB_API_URL = 'https://api.github.com'
        REPO = 'WangZT01/FaceDetection'
        GITHUB_TOKEN = credentials('Jenkins-Github-SSH-WangZT01	')
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'git@github.com:WangZT01/FaceDetection.git'
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh """
                    curl -X POST -H "Authorization: token $GITHUB_TOKEN" \
                         -H "Content-Type: application/json" \
                         -d '{
                                "state": "pending",
                                "description": "Tests are running...",
                                "context": "continuous-integration/jenkins"
                             }' \
                         $GITHUB_API_URL/repos/$REPO/statuses/$GIT_COMMIT
                    """
                }

                sh 'echo Running tests...'
            }
        }
    }
    post {
        success {
            script {
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