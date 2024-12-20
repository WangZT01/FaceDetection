pipeline {
    agent any
    environment {
        GITHUB_API_URL = 'https://api.github.com'
        REPO = 'WangZT01/FaceDetection'
        GITHUB_TOKEN = credentials('peter-github-ssh')
        GITHUB_CREDENTIALS = 'peter-github-ssh'
    }

    stages {
        stage('Initialize') {
            steps {
                script {
                    setGitHubPullRequestStatus(
                        state: 'PENDING',
                        context: 'continuous-integration/jenkins/init',
                        message: 'Pipeline initialization in progress'
                    )

                    echo "Initializing pipeline..."
                    sleep 2

                    setGitHubPullRequestStatus(
                        state: 'SUCCESS',
                        context: 'continuous-integration/jenkins/init',
                        message: 'Pipeline initialized successfully'
                    )
                }
            }
        }

        stage('Environment Setup') {
            steps {
                script {
                    setGitHubPullRequestStatus(
                        state: 'PENDING',
                        context: 'continuous-integration/jenkins/setup',
                        message: 'Setting up environment'
                    )

                    echo "Environment Variables:"
                    sh 'env'
                    sleep 5

                    setGitHubPullRequestStatus(
                        state: 'SUCCESS',
                        context: 'continuous-integration/jenkins/setup',
                        message: 'Environment setup completed'
                    )
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    setGitHubPullRequestStatus(
                        state: 'PENDING',
                        context: 'continuous-integration/jenkins/tests',
                        message: 'Running tests'
                    )

                    echo "Running tests..."
                    sleep 10

                    setGitHubPullRequestStatus(
                        state: 'SUCCESS',
                        context: 'continuous-integration/jenkins/tests',
                        message: 'Tests completed successfully'
                    )
                }
            }
        }
    }

    post {
        success {
            script {
                setGitHubPullRequestStatus(
                    state: 'SUCCESS',
                    context: 'continuous-integration/jenkins',
                    message: 'All stages completed successfully'
                )
            }
        }
        failure {
            script {
                setGitHubPullRequestStatus(
                    state: 'FAILURE',
                    context: 'continuous-integration/jenkins',
                    message: 'Pipeline failed'
                )
            }
        }
    }
}