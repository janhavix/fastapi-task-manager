pipeline {
agent any

```
stages {

    stage('Build Docker Image') {
        steps {
            sh 'docker build -t fastapi-app .'
        }
    }

    stage('Deploy Container') {
        steps {
            sh '''
            docker stop fastapi-container || true
            docker rm fastapi-container || true

            docker run -d \
              --name fastapi-container \
              -p 8000:8000 \
              fastapi-app
            '''
        }
    }
}
```

}
