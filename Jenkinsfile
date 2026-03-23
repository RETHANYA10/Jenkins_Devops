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
            // Works without plugins: download from "Artifacts" on the build page
            archiveArtifacts artifacts: 'html/index.html', allowEmptyArchive: true

            // If you install the "HTML Publisher" plugin later, you can use this instead:
            // publishHTML(target: [
            //     reportName: 'HTML Report',
            //     reportDir: 'html',
            //     reportFiles: 'index.html',
            //     keepAll: true,
            //     alwaysLinkToLastBuild: true
            // ])
        }
    }
}
