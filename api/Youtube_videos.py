from apiclient.discovery import build


# from apiclient.errors import HttpError
# from oauth2client.tools import argparser

# DEVELOPER_KEY = "AIzaSyDT_tDZOPpjBOuUv5jusATc98ep0Gzjgvc"
DEVELOPER_KEY = "AIzaSyB4klg5itSHIb8Q7JL3CXGJ665b-aTh1o4"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(q, max_results=20, order="relevance", token=None, location=None, location_radius=None):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=q,
        type="video",
        pageToken=token,
        order=order,
        part="id,snippet",
        maxResults=max_results

    ).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append(search_result)
    try:
        nexttok = search_response["nextPageToken"]
        return (nexttok, videos)
    except Exception as e:
        nexttok = "last_page"
        return (nexttok, videos)

def comments_search(q, max_results=20, order="relevance", token=None, location=None, location_radius=None):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    results = youtube.commentThreads().list(
        part="snippet",
        videoId=q,
        textFormat="plainText"
    ).execute()

    for item in results["items"]:
        # comment = item["snippet"]["textDisplay"]
        # author = comment["snippet"]["authorDisplayName"]
        comment = item["snippet"]["topLevelComment"]
        author = comment["snippet"]["authorDisplayName"]
        text = comment["snippet"]["textDisplay"]

    return results["items"]

# def geo_query(video_id):
#     youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
#
#     video_response = youtube.videos().list(
#         id=video_id,
#         part='snippet, recordingDetails, statistics'
#
#     ).execute()
#
#     return video_response
