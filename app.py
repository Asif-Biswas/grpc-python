from flask import Flask, render_template, request
import grpc
import helloworld_pb2
import helloworld_pb2_grpc

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form.get('name')
        channel = grpc.insecure_channel('localhost:50051')
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name=name))
        return render_template('index.html', message=response.message)
    return render_template('index.html', message='')

if __name__ == '__main__':
    app.run()





