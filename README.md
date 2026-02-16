# Help on FAST API

```
pip install "fastapi[all]"

uvicorn main:app --reload
```

# Test with Postman

URL - http://127.0.0.1:80/response
(POST)

``` json

{
  "text": "Who is the hero of the story?"
}

```

# Docker Commands
```
docker build -t chatgpt-project1 .
docker run -d -p 8080:80 chatgpt-project1
docker tag chatgpt-project1 kogtikovnikita/chatgpt-project1
docker push kogtikovnikita/chatgpt-project1
```


# Kubernetes Code

```
kubectl create secret generic openai-secret --from-literal=API_KEY=<api-key>

```