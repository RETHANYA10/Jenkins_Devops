pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull your repo (remove if SCM is already configured in the job)
                git url:'https://github.com/RETHANYA10/Jenkins_Devops.git', branch: 'b3'
            }
        }

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
            // Publish HTML so it’s visible in the Jenkins build page
            publishHTML(
                target: [
                    reportName: 'HTML Report',
                    reportDir: 'html',
                    reportFiles: 'index.html',
                    keepAll: true,
                    alwaysLinkToLastBuild: true
                ]
            )
        }
    }
}
