from typing import List, Dict
from anthropic_api import AnthropicAPI
import json

def generate_video_ideas(trend_analysis: Dict, creator_goals: Dict, num_ideas: int, anthropic_api: AnthropicAPI):
    """
    Generate faceless video ideas based on current trends and creator's goals.
    """
    prompt = f"""Based on the following YouTube trend analysis:
    {json.dumps(trend_analysis, indent=2)}

    And the creator's goals:
    {json.dumps(creator_goals, indent=2)}

    Please generate {num_ideas} unique video ideas that can be created as faceless videos. Each idea should include:
    - A title
    - A brief concept description
    - The target audience
    - Viability rating
    - Production complexity
    - A short-form video script (30-60 seconds) using only visuals, background music, sound effects, and text overlays.

    Format each idea as follows:
    Idea 1:
    Title: ...
    Concept: ...
    Target Audience: ...
    Viability: ...
    Production Complexity: ...
    Short-Form Video Script:
    ...
    """

    response = anthropic_api.generate_response(prompt, max_tokens=1500, temperature=0.8)
    if response:
        try:
            # Extract text content from response
            if isinstance(response, list):
                response_text = "".join(block.text for block in response)
            else:
                response_text = response

            # Split response into ideas by "Idea N:" format
            raw_ideas = response_text.split("Idea ")
            parsed_ideas = []

            for raw_idea in raw_ideas[1:]:  # Skip the first empty split
                # Add "Idea" back to each block for consistency
                idea_text = "Idea " + raw_idea.strip()
                parsed_ideas.append({"idea_text": idea_text})

            return parsed_ideas

        except Exception as e:
            print(f"Error processing response: {e}")
    return []

def evaluate_video_idea(idea: str, trend_analysis: Dict, anthropic_api: AnthropicAPI):
    """
    Evaluate a YouTube video idea using Anthropic API and trending data.
    """
    prompt = f"""Please evaluate this YouTube video idea: "{idea}"

    Here is the current trending data on YouTube:
    {json.dumps(trend_analysis, indent=2)}

    Based on this trending data and the video idea, please evaluate:
    1. Trend alignment (how well it fits with current popular content)
    2. Originality while maintaining trend relevance
    3. Content sustainability (evergreen value and long-term interest)
    4. SEO/discoverability potential

    Format your response as JSON with the following structure:
    {{
        "alignment_with_trends": {{
            "score": <1-10>,
            "analysis": "..."
        }},
        "originality": {{
            "score": <1-10>,
            "analysis": "..."
        }},
        "sustainability": {{
            "score": <1-10>,
            "analysis": "..."
        }},
        "seo_potential": {{
            "score": <1-10>,
            "analysis": "..."
        }}
    }}
    """

    response = anthropic_api.generate_response(prompt, max_tokens=1000, temperature=0.7)
    if response:
        try:
            # If response is a list of TextBlocks, extract the text content
            if isinstance(response, list):
                response_text = "".join(block.text for block in response)
            else:
                response_text = response

            # Attempt to parse the response as JSON
            return json.loads(response_text)

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
            print(f"Response text: {response_text}")  # Debugging: Show the raw response
    return {"error": "Failed to evaluate video idea"}

