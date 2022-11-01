# Socket Programming Example

## Build

```bash
mkdir -p build
cd build
cmake ..
```

## Run

### bulk echo client requests + single echo epoll server

```bash
# run server on terminal #1
./build/echo_epoll_server/echo_epoll_server
```

```bash
# run server on terminal #2
# usage: ./scripts/bulk_echo_client.py <num_requests>
./scripts/bulk_echo_client.py 2000
```

Exampel output

```
2000 requests was succeedeed out of 2000 requests
```

## TODO:

- epoll server with 1 req per process
- epoll server with thread pool(or green thread) with a dumb scheduler

