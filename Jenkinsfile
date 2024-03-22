pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                // Replace this with your build steps
                sh 'echo "Building..."'
            }
        }
        stage('Test') {
            steps {
                // Replace this with your test steps
                sh 'echo "Testing..."'
            }
        }
        stage('Deploy') {
            steps {
                // Replace this with your deployment steps
                sh 'echo "Deploying..."'
            }
        }
    }
    
    post {
        success {
            // This block will execute if the pipeline runs successfully
            echo 'Pipeline succeeded! Congratulations!'
        }
        failure {
            // This block will execute if the pipeline fails
            echo 'Pipeline failed! Check the logs for details.'
        }
    }
}
