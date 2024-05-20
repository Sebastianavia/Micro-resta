pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = 'docker.io'
        DOCKER_CREDENTIALS_ID = 'dockerhub-sebastiannavia'
        IMAGE_NAME = 'sebastiannavia/micro-calculadora-resta'
    }

    stages {
        stage('Checkout') {
            steps {
                // Clonar el repositorio
                git branch: 'main', url: 'https://github.com/Sebastianavia/Micro-resta.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Construir la imagen Docker
                    def app = docker.build("${IMAGE_NAME}:0.0.2")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry("https://${DOCKER_REGISTRY}", "${DOCKER_CREDENTIALS_ID}") {
                        def app = docker.image("${IMAGE_NAME}:0.0.2")
                        app.push()
                    }
                }
            }
        }
    }

    post {
        always {
            // Limpiar el entorno
            cleanWs()
        }
        success {
            echo 'Pipeline completado exitosamente.'
        }
        failure {
            echo 'El pipeline ha fallado.'
        }
    }
}

