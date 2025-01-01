from anthropic import Anthropic

class AnthropicAPI:
    def __init__(self, api_key: str):
        self.anthropic = Anthropic(api_key=api_key)

    def generate_response(self, prompt: str, max_tokens=1000, temperature=0.7):
        """
        Sends a prompt to the Anthropic API and retrieves the response.
        """
        try:
            response = self.anthropic.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content
        except Exception as e:
            print(f"Error communicating with Anthropic API: {e}")
            return None
