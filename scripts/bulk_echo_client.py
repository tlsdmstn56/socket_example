#!/usr/bin/env python
import subprocess as sp
import sys

PORT = 12345
SERVER_ADDR = '127.0.0.1'
CLIENT_EXEC = './build/echo_client/echo_client'

class Command:

    def __init__(self, msg):
        self.cmd = [
            CLIENT_EXEC, SERVER_ADDR, str(msg), str(PORT)
        ]
        self.p = None
        self.run()

    def run(self):
        self.p = sp.Popen(self.cmd, stderr=sp.DEVNULL, stdout=sp.DEVNULL)

    def wait(self) -> int:
        return self.p.wait()

def main():
    num_req = int(sys.argv[1])
    reqs = [Command(i) for i in range(num_req)]
    rets = [int(r.wait() == 0) for r in reqs]
    print(f"{sum(rets)} requests was succeedeed out of {len(rets)} requests")

if __name__ == '__main__':
    main()
        
    


