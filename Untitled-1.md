PS C:\codes\minimum-websocket> npm start
Debugger listening on ws://127.0.0.1:60242/6669cf68-d9fb-4b8c-ad6a-9c3e09a3cac4
For help, see: https://nodejs.org/en/docs/inspector
Debugger attached.
Waiting for the debugger to disconnect...
Debugger listening on ws://127.0.0.1:60245/7e1168a6-5674-49e5-b38b-2825e24f12ef
For help, see: https://nodejs.org/en/docs/inspector
Debugger attached.

> start
> node server.js

Debugger listening on ws://127.0.0.1:60247/113f3c18-1a30-4db9-bafb-6da6f7a824eb
For help, see: https://nodejs.org/en/docs/inspector
Debugger attached.
Waiting for the debugger to disconnect...
node:events:497
      throw er; // Unhandled 'error' event
      ^

Error: listen EADDRINUSE: address already in use :::3000
    at Server.setupListenHandle [as _listen2] (node:net:1898:16)
    at listenInCluster (node:net:1946:12)
    at Server.listen (node:net:2044:7)
    at Object.<anonymous> (C:\codes\minimum-websocket\server.js:71:8)
    at Module._compile (node:internal/modules/cjs/loader:1358:14)
    at Module._extensions..js (node:internal/modules/cjs/loader:1416:10)
    at Module.load (node:internal/modules/cjs/loader:1208:32)
    at Module._load (node:internal/modules/cjs/loader:1024:12)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:174:12)
    at node:internal/main/run_main_module:28:49
Emitted 'error' event on Server instance at:
    at emitErrorNT (node:net:1925:8)
    at process.processTicksAndRejections (node:internal/process/task_queues:82:21) {
  code: 'EADDRINUSE',
  errno: -4091,
  syscall: 'listen',
  address: '::',
  port: 3000
}

Node.js v20.14.0
Waiting for the debugger to disconnect...