pipeline {
    agent {label 'Agent'}
    
    stages {
        stage('Build') {
            steps {
                // Example: Checkout source code from version control
                git 'https://github.com/yourusername/yourrepository.git'
                // Example: Build your application (replace with your build commands)
                sh 'mvn clean install'
            }
        }
        stage('Test') {
            steps {
                // Example: Run tests for your application (replace with your test commands)
                sh 'mvn test'
            }
        }
        stage('Deploy') {
            steps {
                // Example: Deploy your application (replace with your deployment commands)
                sh 'kubectl apply -f deployment.yaml'
            }
        }
    }
    
    post {
        success {
            // Actions to perform if the pipeline succeeds
            echo 'Pipeline succeeded! Congratulations!'
        }
        failure {
            // Actions to perform if the pipeline fails
            echo 'Pipeline failed! Please check the logs for details.'
        }
        always {
            // Actions to perform regardless of success or failure
            echo 'Pipeline finished.'
        }
    }
}
