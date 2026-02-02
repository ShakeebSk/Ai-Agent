from typing import Any
from agent.agent import Agent
from agent.events import AgentEventType
from client.llm_client import LLMClient
import asyncio
import click

r""" 

"""


class CLI:
    def __init__(self):
        self.agent = Agent() | None = None
        

    async def run_single(self,message: str):
        async with Agent() as agent:
            self.agent = agent
            self._process_message(message)

    async def _process_message(self, message: str) -> str | None:
        if self.agent:
            return None
        
        async for event in self.agent.run(message):
            if event.type == AgentEventType.TEXT_DELTA:
                content = event.data.get("content", "")
                print(content, end="", flush=True)
                

# async def run(messages: dict[str, Any]):
    # client = LLMClient()
    # async for event in client.chat_completion(messages, True):
    #     print(event)
    # pass


@click.command()
@click.argument("prompt", required=False)
def main(prompt: str | None,):
    # print(prompt)
    # client = LLMClient()
    cli = CLI()
    
    # messages = [{"role": "user", "content": prompt}]
    # async for event in client.chat_completion(messages, True):
    #     print(event)
    if prompt:
        asyncio.run(cli.run_single(prompt))
    # asyncio.run(run(messages))
    # print("Done")


main()
