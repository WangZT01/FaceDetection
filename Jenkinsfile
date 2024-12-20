pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Tests build stage'
            }
        }
        stage('Test') {
            steps {
                echo 'Tests test stage'
            }
        }
    }
    post {
        success {
            echo 'Tests Passed'
        }
        failure {
            echo 'Tests Failed'
        }
    }
}