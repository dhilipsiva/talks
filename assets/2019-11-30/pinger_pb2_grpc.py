# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import pinger_pb2 as pinger__pb2


class PingerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.LevelOne = channel.unary_unary(
        '/Pinger/LevelOne',
        request_serializer=pinger__pb2.Request.SerializeToString,
        response_deserializer=pinger__pb2.Reply.FromString,
        )
    self.LevelTwo = channel.unary_unary(
        '/Pinger/LevelTwo',
        request_serializer=pinger__pb2.Request.SerializeToString,
        response_deserializer=pinger__pb2.Reply.FromString,
        )
    self.Ping = channel.unary_unary(
        '/Pinger/Ping',
        request_serializer=pinger__pb2.Request.SerializeToString,
        response_deserializer=pinger__pb2.Reply.FromString,
        )


class PingerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def LevelOne(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def LevelTwo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Ping(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PingerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'LevelOne': grpc.unary_unary_rpc_method_handler(
          servicer.LevelOne,
          request_deserializer=pinger__pb2.Request.FromString,
          response_serializer=pinger__pb2.Reply.SerializeToString,
      ),
      'LevelTwo': grpc.unary_unary_rpc_method_handler(
          servicer.LevelTwo,
          request_deserializer=pinger__pb2.Request.FromString,
          response_serializer=pinger__pb2.Reply.SerializeToString,
      ),
      'Ping': grpc.unary_unary_rpc_method_handler(
          servicer.Ping,
          request_deserializer=pinger__pb2.Request.FromString,
          response_serializer=pinger__pb2.Reply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Pinger', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
