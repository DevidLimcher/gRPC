import os
from concurrent import futures
import grpc
import social_network_pb2
import social_network_pb2_grpc

class SocialNetworkServicer(social_network_pb2_grpc.SocialNetworkServicer):
    def __init__(self):
        self.posts = []

    def CreatePost(self, request, context):
        post = social_network_pb2.Post(
            id=str(len(self.posts) + 1),
            user=request.user,
            content=request.content,
            likes=0,
            comments=[]
        )
        self.posts.append(post)
        return social_network_pb2.CreatePostResponse(post=post)

    def GetFeed(self, request, context):
        return social_network_pb2.GetFeedResponse(posts=self.posts)

    def LikePost(self, request, context):
        for post in self.posts:
            if post.id == request.post_id:
                post.likes += 1
                return social_network_pb2.LikePostResponse(post=post)
        context.abort(grpc.StatusCode.NOT_FOUND, "Post not found")

    def CommentPost(self, request, context):
        for post in self.posts:
            if post.id == request.post_id:
                comment = social_network_pb2.Comment(user=request.user, content=request.content)
                post.comments.append(comment)
                return social_network_pb2.CommentPostResponse(post=post)
        context.abort(grpc.StatusCode.NOT_FOUND, "Post not found")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    social_network_pb2_grpc.add_SocialNetworkServicer_to_server(SocialNetworkServicer(), server)
    port = os.environ.get('PORT', '4000')
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
