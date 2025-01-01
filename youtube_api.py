from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class YouTubeAPI:
    def __init__(self, api_key: str):
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def get_trending_videos(self, region_code='US', max_results=10, category_id=None):
        """
        Fetch trending videos from YouTube.
        """
        try:
            request = self.youtube.videos().list(
                part='snippet,statistics',
                chart='mostPopular',
                regionCode=region_code,
                maxResults=max_results,
                videoCategoryId=category_id if category_id else None
            )
            response = request.execute()
            return response['items']
        except HttpError as e:
            print(f"Error fetching trending videos: {e}")
            return []