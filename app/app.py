from flask import flask
import redis
import os
app = Flask(__name__)
cache=redis.Redis(host=os.getenv('REDIS_HOST','redis'),port=6379)
@app.route('/')
def hello():
    count = cache.incr('visits')
    return f'hello,world!you have visited{count}times.'
if __name__=="__main__":
    app.run(host='0.0.0.0')
    