""" Multiple connections possible, but it is still blocking.
Seperate thread is handling establishing connections.
Main thread is handling requests.

If you do on multiple terminals:
    python3 count_req_per_sec.py

It will look like multiple connections are handled in parallel
but try to connect and do not send anything:
    nc 127.0.0.1 8080

All other terminals will show sth like:
    Requests per second: 0
"""

import socket
from collections import deque
from threading import Thread
from time import sleep

import __init__ as _
from fibbonaci import count_fibbonaci

connections = deque()
tasks = deque()


def main():
    addr = ("", 8080)  # all interfaces, port 8080

    blocking_server(addr)


def blocking_server(addr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)

    Thread(target=create_connections, args=[s]).start()

    while True:
        for __ in range(len(connections)):
            process_connection(s)

        process_tasks()

    print("Closed")


def create_connections(s):
    while True:
        client, addr = s.accept()

        print("Connection", addr)

        connections.append(client)


def process_connection(s):
    try:
        client = connections.popleft()
    except IndexError:
        return

    handle_request(client)


def handle_request(client):
    tasks.append((_recv_req_task, [client]))


def _recv_req_task(client):
    req = client.recv(100)

    if not req:
        client.close()

    n = int(req)

    tasks.append((_anws_req_task, [client, n]))


def _anws_req_task(client, n):
    resp = str(count_fibbonaci(n)).encode("ascii") + b"\n"

    client.send(resp)

    connections.append(client)


def process_tasks():
    while True:
        try:
            task = tasks.popleft()
        except IndexError:
            break

        func, args = task

        try:
            func(*args)
        except Exception as err:
            print(err)


if __name__ == "__main__":
    main()
