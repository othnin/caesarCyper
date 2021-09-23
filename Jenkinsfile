
pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python src/main.py'
            }
        }
        stage('test') {
            steps {
                sh 'python test/test_caesarCyper.py'
            }
        }
    }
}
