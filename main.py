from fastapi import FastAPI
from openai import OpenAI
import config
from pydantic import BaseModel
import time
import uvicorn
import os

assistant_id = config.assistant_id
api_key = os.environ['OPENAI_API']

client = OpenAI(api_key=api_key)


app = FastAPI()


class Body(BaseModel):
    text: str

@app.get("/")
def welcome():
    return{"message":"Welcome to ChatGPT AI Application V3"}


@app.get("/home")
def welcome():
    return {"message" : "Welcome Home"}

@app.post("/dummy")
def demo_function(data):
    return {"message" : data}

@app.post("/response")
def generate(body: Body):
    prompt = body.text
    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(
        thread_id = thread.id,
        role="user",
        content=prompt
    )

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id = assistant_id,
        instructions="Answer the question using the uploaded file. You MUST search the file before answering."
    )

    while True:
        run_retrieve = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        if run_retrieve.status == "completed":
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            return messages.data[0].content[0].text.value
            break
        elif run_retrieve.status == "failed":
            raise Exception("Run failed")
        time.sleep(1)

if __name__ == "__main__":
    print("Running application")
    uvicorn.run(app,host="0.0.0.0",port=80)




