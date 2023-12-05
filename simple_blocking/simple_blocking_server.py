import socket

import __init__ as _
from fibbonaci import count_fibbonaci


def main():
    addr = ("", 8080)  # all interfaces, port 8080

    blocking_server(addr)


def blocking_server(addr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)

    while True:
        client, addr = s.accept()

        print("Connection", addr)

        try:
            fib_handler(client)
        except Exception as err:
            print("Error:", str(err))

    print("Closed")


def fib_handler(client):
    while True:
        req = client.recv(100)

        if not req:
            break

        n = int(req)

        resp = str(count_fibbonaci(n)).encode("ascii") + b"\n"

        client.send(resp)


if __name__ == "__main__":
    main()
