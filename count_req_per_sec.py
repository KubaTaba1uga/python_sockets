import socket
from threading import Thread
from time import sleep

FIBBONACI_SEQ_N = 20


class Counter:
    i = 0

    @classmethod
    def increment(cls):
        cls.i += 1

    @classmethod
    def reset(cls):
        cls.i = 0


def main():
    addr = ("", 8080)  # all interfaces, port 8080

    Thread(target=monitor).start()

    count_req_per_sec(addr)


def count_req_per_sec(addr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(addr)

    while True:
        s.send(str(FIBBONACI_SEQ_N).encode("ascii"))

        s.recv(100)

        Counter.increment()

    s.close()


def monitor():
    global COUNTER

    while True:
        sleep(1)

        print("Requests per second:", Counter.i)

        Counter.reset()


if __name__ == "__main__":
    main()
