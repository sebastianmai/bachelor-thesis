#!/usr/bin/env python3
import zmq


class FakeZmq:
    def __init__(self) -> None:
        pass

    def close(self):
        pass

    def term(self):
        pass


class ZMQ_Publisher:
    def __init__(self, address="localhost"):
        self.socket = FakeZmq()
        self.context = FakeZmq()

    # function for sending a custom multipart message
    # refer to readme for more information
    def publish(self, header, additionalSensors, payload, flags=0):
        pass
