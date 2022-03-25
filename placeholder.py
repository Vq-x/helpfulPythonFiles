from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, GiftEvent, ShareEvent, LikeEvent, FollowEvent, ViewerCountUpdateEvent

# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(
    unique_id="username", **(
        {
            "enable_extended_gift_info": True
        }
    )
)

# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)


@client.on("comment")
async def on_connect(event: CommentEvent):
    print(f"{event.user.uniqueId} -> {event.comment}")

@client.on("gift")
async def on_gift(event: GiftEvent):
    print(f"{event.user.uniqueId} sent a {event.gift.extended_gift.name} with a diamond amount of {event.gift.extended_gift.diamond_count}!")

@client.on("like")
async def on_like(event: LikeEvent):
    print(f"{event.user.uniqueId} has liked the stream {event.likeCount} times, there is now {event.totalLikeCount} total likes!")

@client.on("follow")
async def on_follow(event: FollowEvent):
    print(f"{event.user.uniqueId} followed the streamer")
    

@client.on("share")
async def on_share(event: ShareEvent):
    print(f"{event.user.uniqueId} shared the streamer!")
    
@client.on("viewer_count_update")
async def on_connect(event: ViewerCountUpdateEvent):
    print("Received a new viewer count:", event.viewerCount)

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    
    client.run()
