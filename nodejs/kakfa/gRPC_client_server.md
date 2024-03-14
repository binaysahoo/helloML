Sure! Below is a simple example demonstrating how to use gRPC (Google Remote Procedure Call) in Node.js:

First, you need to define a gRPC service in a `.proto` file. Let's create a file named `calculator.proto`:

```protobuf
syntax = "proto3";

service Calculator {
  rpc Add (AddRequest) returns (AddResponse) {}
}

message AddRequest {
  int32 operand1 = 1;
  int32 operand2 = 2;
}

message AddResponse {
  int32 result = 1;
}
```

Next, compile this `.proto` file into JavaScript using the Protocol Buffers compiler (`protoc`) with the gRPC plugin:

```bash
protoc --proto_path=. --js_out=import_style=commonjs,binary:. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_tools_node_protoc_plugin` calculator.proto
```

This will generate two JavaScript files: `calculator_pb.js` and `calculator_grpc_pb.js`.

Now, let's implement a gRPC server in Node.js:

```javascript
const grpc = require('grpc');
const { Calculator } = require('./calculator_grpc_pb');
const { AddResponse } = require('./calculator_pb');

function add(call, callback) {
  const operand1 = call.request.getOperand1();
  const operand2 = call.request.getOperand2();
  const result = operand1 + operand2;

  const response = new AddResponse();
  response.setResult(result);

  callback(null, response);
}

const server = new grpc.Server();
server.addService(Calculator.service, { add });
server.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
server.start();
console.log('Server started');
```

Now, let's implement a gRPC client in Node.js:

```javascript
const grpc = require('grpc');
const { CalculatorClient } = require('./calculator_grpc_pb');
const { AddRequest } = require('./calculator_pb');

const client = new CalculatorClient('localhost:50051', grpc.credentials.createInsecure());

const request = new AddRequest();
request.setOperand1(10);
request.setOperand2(20);

client.add(request, (error, response) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('Response:', response.getResult());
  }
});
```

Ensure that your gRPC server is running before running the client code. You can start the server with the following command:

```bash
node server.js
```

Then, you can run the client code:

```bash
node client.js
```

This will send a request to the gRPC server, and the server will respond with the result of adding the two operands (10 and 20).
