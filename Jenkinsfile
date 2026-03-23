pipeline {
    agent any

    // Keep default Declarative checkout (do NOT add a custom Checkout stage)
    // If you want a custom stage, uncomment skipDefaultCheckout(true) and add the Checkout stage below.

    // options { skipDefaultCheckout(true) }

    stages {
        // Use this stage ONLY if you enabled skipDefaultCheckout(true) above.
        // stage('Checkout') {
        //     steps {
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
