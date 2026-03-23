pipeline {
    agent any

    stages {

        stage('Run Python') {
            steps {
                sh 'python3 python.py'
            }
        }

        stage('Compile & Run Java') {
            steps {
                sh '''
                    javac javaf.java
                    java javaf
                '''
            }
        }

        stage('Prepare HTML') {
            steps {
                sh '''
                    mkdir -p html
                    cp index.html html/
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'html/index.html', allowEmptyArchive: true
        }
    }
}
