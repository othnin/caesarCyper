
pipeline {
    agent any
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
