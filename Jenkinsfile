pipeline {
    agent any
    
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',url: 'https://github.com/ricardoahumada/python-package-flask-test'
	        }
        }        
        stage('Unit/Integration tests') {
            steps {
                echo 'Unit/Integration...'
            }
        }        
        stage('Acceptance tests') {
            steps {
                echo 'Acceptance...'
            }
        }        
    }
    post {
        always {
            echo 'post do this always...'
        }
        success{
            echo 'post do this when success...'
        }
        failure {
            echo 'post do this when failure...'
        }
        cleanup{
            echo 'post do this when cleanup...'
            deleteDir()
        }
    }
}
