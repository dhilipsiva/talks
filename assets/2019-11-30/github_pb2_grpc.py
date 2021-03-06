# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import github_pb2 as github__pb2


class AccountStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetUserName = channel.unary_unary(
        '/Account/GetUserName',
        request_serializer=github__pb2.Request.SerializeToString,
        response_deserializer=github__pb2.Reply.FromString,
        )
    self.SetUserPassword = channel.unary_unary(
        '/Account/SetUserPassword',
        request_serializer=github__pb2.Request.SerializeToString,
        response_deserializer=github__pb2.Reply.FromString,
        )


class AccountServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetUserName(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetUserPassword(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AccountServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetUserName': grpc.unary_unary_rpc_method_handler(
          servicer.GetUserName,
          request_deserializer=github__pb2.Request.FromString,
          response_serializer=github__pb2.Reply.SerializeToString,
      ),
      'SetUserPassword': grpc.unary_unary_rpc_method_handler(
          servicer.SetUserPassword,
          request_deserializer=github__pb2.Request.FromString,
          response_serializer=github__pb2.Reply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Account', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class GistStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetPublicGist = channel.unary_unary(
        '/Gist/GetPublicGist',
        request_serializer=github__pb2.Request.SerializeToString,
        response_deserializer=github__pb2.Reply.FromString,
        )


class GistServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetPublicGist(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GistServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetPublicGist': grpc.unary_unary_rpc_method_handler(
          servicer.GetPublicGist,
          request_deserializer=github__pb2.Request.FromString,
          response_serializer=github__pb2.Reply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Gist', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class RepoStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetLatestCommit = channel.unary_unary(
        '/Repo/GetLatestCommit',
        request_serializer=github__pb2.Request.SerializeToString,
        response_deserializer=github__pb2.Reply.FromString,
        )


class RepoServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetLatestCommit(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RepoServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetLatestCommit': grpc.unary_unary_rpc_method_handler(
          servicer.GetLatestCommit,
          request_deserializer=github__pb2.Request.FromString,
          response_serializer=github__pb2.Reply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Repo', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class CommonDBStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetCommonData = channel.unary_unary(
        '/CommonDB/GetCommonData',
        request_serializer=github__pb2.Request.SerializeToString,
        response_deserializer=github__pb2.Reply.FromString,
        )


class CommonDBServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetCommonData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CommonDBServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetCommonData': grpc.unary_unary_rpc_method_handler(
          servicer.GetCommonData,
          request_deserializer=github__pb2.Request.FromString,
          response_serializer=github__pb2.Reply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'CommonDB', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class CodeDBStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetCodeData = channel.unary_unary(
        '/CodeDB/GetCodeData',
        request_serializer=github__pb2.Request.SerializeToString,
        response_deserializer=github__pb2.Reply.FromString,
        )


class CodeDBServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetCodeData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CodeDBServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetCodeData': grpc.unary_unary_rpc_method_handler(
          servicer.GetCodeData,
          request_deserializer=github__pb2.Request.FromString,
          response_serializer=github__pb2.Reply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'CodeDB', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
