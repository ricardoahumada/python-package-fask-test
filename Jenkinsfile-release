pipeline {
    agent any
    
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',url: 'https://github.com/ricardoahumada/python-package-flask-test' 
                bat 'rd /s /q "dist"'
                bat 'dir'
	        }
        }        
        stage('Unit/Integration tests') {
            steps {
                echo 'Unit/Integration...'
            }
        }
        stage('Package') {
            steps {
                echo 'Packaging...'
                // bat 'c:/Users/Administrator/AppData/Local/Programs/Python/Python39/python.exe -m build'
            }
        }
        stage('Acceptance tests') {
            steps {
                echo 'Acceptance...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                //withCredentials([usernamePassword(credentialsId: 'nexus_credentials', usernameVariable: 'USER', passwordVariable: 'USERPASS')]) {
                //    echo "$USER $USERPASS"
                //    bat "twine upload  --repository-url http://localhost:8081/repository/hosted-python/ dist/* -u${USER} -p${USERPASS}"
                //}
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
