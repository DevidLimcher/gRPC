# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import social_network_pb2 as social__network__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in social_network_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class SocialNetworkStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreatePost = channel.unary_unary(
                '/social_network.SocialNetwork/CreatePost',
                request_serializer=social__network__pb2.CreatePostRequest.SerializeToString,
                response_deserializer=social__network__pb2.CreatePostResponse.FromString,
                _registered_method=True)
        self.GetFeed = channel.unary_unary(
                '/social_network.SocialNetwork/GetFeed',
                request_serializer=social__network__pb2.GetFeedRequest.SerializeToString,
                response_deserializer=social__network__pb2.GetFeedResponse.FromString,
                _registered_method=True)
        self.LikePost = channel.unary_unary(
                '/social_network.SocialNetwork/LikePost',
                request_serializer=social__network__pb2.LikePostRequest.SerializeToString,
                response_deserializer=social__network__pb2.LikePostResponse.FromString,
                _registered_method=True)
        self.CommentPost = channel.unary_unary(
                '/social_network.SocialNetwork/CommentPost',
                request_serializer=social__network__pb2.CommentPostRequest.SerializeToString,
                response_deserializer=social__network__pb2.CommentPostResponse.FromString,
                _registered_method=True)


class SocialNetworkServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreatePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFeed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LikePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CommentPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SocialNetworkServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreatePost': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePost,
                    request_deserializer=social__network__pb2.CreatePostRequest.FromString,
                    response_serializer=social__network__pb2.CreatePostResponse.SerializeToString,
            ),
            'GetFeed': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFeed,
                    request_deserializer=social__network__pb2.GetFeedRequest.FromString,
                    response_serializer=social__network__pb2.GetFeedResponse.SerializeToString,
            ),
            'LikePost': grpc.unary_unary_rpc_method_handler(
                    servicer.LikePost,
                    request_deserializer=social__network__pb2.LikePostRequest.FromString,
                    response_serializer=social__network__pb2.LikePostResponse.SerializeToString,
            ),
            'CommentPost': grpc.unary_unary_rpc_method_handler(
                    servicer.CommentPost,
                    request_deserializer=social__network__pb2.CommentPostRequest.FromString,
                    response_serializer=social__network__pb2.CommentPostResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'social_network.SocialNetwork', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SocialNetwork(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreatePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/social_network.SocialNetwork/CreatePost',
            social__network__pb2.CreatePostRequest.SerializeToString,
            social__network__pb2.CreatePostResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetFeed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/social_network.SocialNetwork/GetFeed',
            social__network__pb2.GetFeedRequest.SerializeToString,
            social__network__pb2.GetFeedResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def LikePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/social_network.SocialNetwork/LikePost',
            social__network__pb2.LikePostRequest.SerializeToString,
            social__network__pb2.LikePostResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CommentPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/social_network.SocialNetwork/CommentPost',
            social__network__pb2.CommentPostRequest.SerializeToString,
            social__network__pb2.CommentPostResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
