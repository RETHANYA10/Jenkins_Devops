pipeline {
    agent any

    // If you keep Declarative auto-checkout, do NOT add a custom Checkout stage.
    // If you want to control checkout explicitly, uncomment skipDefaultCheckout(true)
    // and the Checkout stage below.
    // options { skipDefaultCheckout(true) }

    stages {
        // Uncomment this stage ONLY if you enabled skipDefaultCheckout(true) above.
        // stage('Checkout') {
        //     steps {
        //         // Reuses the job's SCM configuration (correct repo/branch/credentials)
        //         checkout scm
        //     }
        // }

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
            when {
                // Only run if index.html exists in the repo
                expression { fileExists('index.html') }
            }
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
            // Only publish if the html file exists to avoid failures
            script {
                if (fileExists('html/index.html')) {
                    publishHTML(target: [
                        reportName: 'HTML Report',
                        reportDir: 'html',
                        reportFiles: 'index.html',
                        keepAll: true,
                        alwaysLinkToLastBuild: true
                    ])
                } else {
                    echo 'No html/index.html found — skipping publishHTML.'
                }
            }
        }
    }
}
