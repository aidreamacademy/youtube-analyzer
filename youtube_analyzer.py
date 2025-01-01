import os
from youtube_api import YouTubeAPI
from anthropic_api import AnthropicAPI
from trend_analysis import analyze_trends
from idea_generation import generate_video_ideas, evaluate_video_idea
from constants import CATEGORIES

def main():
    youtube_api_key = os.getenv("YOUTUBE_API_KEY")
    anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

    if not youtube_api_key or not anthropic_api_key:
        print("Please set both YOUTUBE_API_KEY and ANTHROPIC_API_KEY environment variables")
        return

    youtube = YouTubeAPI(youtube_api_key)
    anthropic = AnthropicAPI(anthropic_api_key)

    while True:
        print("\n=== YouTube Video Idea Analyzer ===")
        print("\n1. Analyze current trends")
        print("2. Get video ideas based on trends")
        print("3. Evaluate your video idea")
        print("4. Exit")

        choice = input("\nSelect an option (1-4): ")

        if choice == "1":
            print("\nFetching trending videos...")
            trending_videos = youtube.get_trending_videos()
            trend_analysis = analyze_trends(trending_videos, CATEGORIES)

            print("\n=== Current YouTube Trends ===")
            for category, count in trend_analysis['top_categories'].items():
                print(f"• {category}: {count} videos")

            print("\nTop Tags:")
            for tag, frequency in trend_analysis['top_tags'].items():
                print(f"• {tag}: {frequency} occurrences")

            print(f"\nAverage Views: {int(trend_analysis['average_views']):,}")

        elif choice == "2":
            print("\nGenerating video ideas...")
            trending_videos = youtube.get_trending_videos()
            trend_analysis = analyze_trends(trending_videos, CATEGORIES)

            num_ideas = input("How many ideas would you like? (default 5): ")
            num_ideas = int(num_ideas) if num_ideas.isdigit() else 5

            ideas = generate_video_ideas(trend_analysis, {}, num_ideas, anthropic)
            if not ideas:
                print("No ideas generated. Please try again.")
                continue

            for i, idea in enumerate(ideas, start=1):
                # Print the idea text since the response contains plain-text idea descriptions
                print(f"\nIdea {i}:")
                print(idea['idea_text'])

        elif choice == "3":
            idea = input("\nEnter your video idea: ")
            print("\nEvaluating your idea...")
            trending_videos = youtube.get_trending_videos()
            trend_analysis = analyze_trends(trending_videos, CATEGORIES)
            evaluation = evaluate_video_idea(idea, trend_analysis, anthropic)

            if "error" in evaluation:
                print(f"\nError: {evaluation['error']}")
            else:
                print("\n=== Evaluation Results ===")
                print(f"Trend Alignment: {evaluation['alignment_with_trends']['score']}/10")
                print(f"Analysis: {evaluation['alignment_with_trends']['analysis']}\n")
                
                print(f"Originality: {evaluation['originality']['score']}/10")
                print(f"Analysis: {evaluation['originality']['analysis']}\n")
                
                print(f"Sustainability: {evaluation['sustainability']['score']}/10")
                print(f"Analysis: {evaluation['sustainability']['analysis']}\n")
                
                print(f"SEO Potential: {evaluation['seo_potential']['score']}/10")
                print(f"Analysis: {evaluation['seo_potential']['analysis']}")

        elif choice == "4":
            break

        else:
            print("\nInvalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
