from client.llm_client import LLMClient
import asyncio

r""" """


async def main():
    client = LLMClient()
    messages = [{"role": "user", "content": "whats's up"}]
    async for event in client.chat_completion(messages, True):
        print(event)
    print("Done")


asyncio.run(main())
