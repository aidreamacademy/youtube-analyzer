from typing import List, Dict

def analyze_trends(trending_videos: List[Dict], categories: Dict) -> Dict:
    """
    Analyze trends from the fetched videos and categorize them.
    """
    if not trending_videos:
        return {}

    # Aggregate trend data
    category_count = {}
    tags_frequency = {}
    total_views = 0

    for video in trending_videos:
        # Track categories
        category = video['snippet'].get('categoryId', 'Unknown')
        category_count[category] = category_count.get(category, 0) + 1

        # Track tags
        for tag in video['snippet'].get('tags', []):
            tags_frequency[tag.lower()] = tags_frequency.get(tag.lower(), 0) + 1

        total_views += int(video['statistics'].get('viewCount', 0))

    # Sort and get top tags
    top_tags = sorted(tags_frequency.items(), key=lambda x: x[1], reverse=True)[:10]

    return {
        'top_categories': {categories.get(cat, f'Category {cat}'): count for cat, count in category_count.items()},
        'top_tags': dict(top_tags),
        'average_views': total_views / len(trending_videos)
    }
