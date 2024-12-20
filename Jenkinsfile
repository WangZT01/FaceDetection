pipeline {
    agent any
    environment {
        GITHUB_API_URL = 'https://api.github.com'
        REPO = 'WangZT01/FaceDetection'
        GITHUB_TOKEN = credentials('peter-github-ssh')
        GITHUB_CHECK_NAME = 'Jenkins CI'
        GITHUB_CONTEXT = 'continuous-integration/jenkins'
    }
    stages {
        stage('Start Build') {
            steps {
                script {
                    githubNotify context: "${GITHUB_CONTEXT}",
                                 status: 'PENDING',
                                 description: 'Build is starting'
                }
                echo 'Building...'
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    githubNotify context: "${GITHUB_CONTEXT}",
                                 status: 'PENDING',
                                 description: 'Tests are running'
                }
                echo 'Running tests...'
            }
        }
    }
    post {
        success {
            script {
                githubNotify context: "${GITHUB_CONTEXT}",
                             status: 'SUCCESS',
                             description: 'Build succeeded'
            }
        }
        failure {
            script {
                githubNotify context: "${GITHUB_CONTEXT}",
                             status: 'FAILURE',
                             description: 'Build failed'
            }
        }
    }
}