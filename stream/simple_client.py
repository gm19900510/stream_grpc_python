#! /usr/bin/env python
# -*- coding: utf-8 -*-
import grpc
from stream import stream_pb2, stream_pb2_grpc

_HOST = 'localhost'
_PORT = '8883'

def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = stream_pb2_grpc.StreamServiceStub(channel=conn)
    response = client.SimpleFun(stream_pb2.RequestData(text='hello,world!'))
    print("received: " + response.text)

if __name__ == '__main__':
    run()