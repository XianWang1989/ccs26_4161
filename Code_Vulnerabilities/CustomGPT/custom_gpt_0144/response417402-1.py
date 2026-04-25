from your_file_pb2 import PlayerResponse

# Assuming you have a binary protobuf response (e.g., from YouTube API)
with open('response.bin', 'rb') as f:
    response_data = f.read()

# Parse the data using the generated class
player_response = PlayerResponse()
player_response.ParseFromString(response_data)

# Access fields in the parsed data
print(player_response.yt_ad1)
print(player_response.video_ids)
print(player_response.timestamp)
