# /// script
# dependencies = [
#   "pydantic-ai"
# ]
# ///


from pydantic_ai import Agent, RunContext
from pydantic_ai.models.vertexai import VertexAIModel

agent = Agent(
    model=VertexAIModel(
        model_name='gemini-1.5-flash',
        service_account_file='/path/to/service_account_file.json',
    )
)


@agent.tool
def fetch_weather(_ctx: RunContext[None], city: str) -> str:
    return f'The weather in {city} is sunny.'


def main():
    prompt = "What's the weather in Paris, Tokyo, and New York?"
    result = agent.run_sync(prompt, model_settings={'temperature': 0.0})

    # Expect error here
    #     pydantic_ai.exceptions.UnexpectedModelBehavior: Unexpected response from gemini 400, body:
    # {
    #   "error": {
    #     "code": 400,
    #     "message": "Please ensure that the number of function response parts should be equal to number of function call parts of the function call turn.",
    #     "status": "INVALID_ARGUMENT"
    #   }
    # }

    print('=== Final Result ===')
    print(result.data)


if __name__ == '__main__':
    main()
