from openai import AsyncOpenAI
from typing import Any

r"""
This file will handle all of the response fetching , the streaming of the response and retrying with exponential backoff. All that sort of stuff will go in to this LLM. 
For this to operate wit any LLM provider for our choice we want the dependencies and there are multiple packages that allows it like pydantic that even has a support for creating our own agent ,
openai it allows us to use the LLM of our choice.Their is also an another option that we can go with is Open-router.Open Router SDK which we can use in this i am ussing open ai:

Openai:To use this we need a base url that points to open router

What is Open Router:Open Router is the unified face for the LLMs it is basically the collection of multiple LLMs models.


"""


class LLmClient:
    def __init__(self) -> None:
        self._client: AsyncOpenAI | None = None

    def get_client(self) -> AsyncOpenAI:

        if self._client is None:
            self._client = AsyncOpenAI(
                api_key="<your own api key>",
                base_url="<your own base url>",
            )

            r""" 
            This is the setup for the making request to ai and make the connection with your ai: and then it will give the response basically we want to fetcgh the response from the LLMs:
            Responses in LLMs: There are tow types of responses that we can get from the LLMs 
            1.Streaming Response : Streaming Response means whenever we talk to an ai agent or an LLMs, you might have seen thta the LLMs gives out the bunch of text somthing like chunks 
            of text like of 30 to 50 words or something together.It does that because LLMs are auto regressive , they generate one token at a time and whenever the bunch of tokens are ready 
            it just sends it through the API for us and if we have the non-streaming response version we'll see the entire response when it's done so it might take let's say 15 seconds to get
            the entire response which is not the good user experience that's why they stream the response as soon as a bunch of  tokens are available they send it to us so we show the user a
            response every one sencond so the first 30 words or the first 30 tokens are coming in the first second itself and then another 30 then another 30 and then another 30 like that.
            so the user doesn't have to wait the entire 15 seconds. They can just get started reading the entire thing as soomn as the first set of words come in.  
            
            2. Non-Streaming Response : Non-streaming response means we just wait for the LLM to give us an entire response.
             
            In this both the Streamin and Non-streaming response will be there because the streaming response will be shown to the user for the good usre experience But the non-streaming response 
            version will be required when we have to do compaction or sumarzation when we hit the context length. 
            
            """
        return self._client

    async def close(self):
        if self._client:
            await self._client.close()
            self._client = None

    async def chat_completion(self, messages: list[dict[str:Any]], stream: bool = True):
        r"""
        What are these messages and stream:So the thing about the LLMs is that they are stateless they don't contain any state if we have the bunch of messages 
        for example let's say i am talking to chat gpt and send the message Hii which is 1 message form my side in response chatgpt sended hey, whats'up?  
        so this is basically a list of messages so in this the first one has the role of user that it's a message i have to sent and the second one is comming from the 
        assistant which is the message they have now if i want to continue this chat ley's say i typed 'nothing much' so i am continuing the messages but the LLMs dosen't 
        inherently remember that these were the text that was in this conversation.
        No,
        Whenever we send the message another text 'nothing much' the above entire list that was present get resent to the LLMs to contrast 
        this to somthing like actual chat app like WhatsApp where whenever we send the message only the last message get's sent that's 
        not the case over here in chatgpt all of the messages are sent back because that' how the auto regressive generation will work so 
        again this messages ['hii' , 'hey, whats'up?','nothing much'] get sent's so that the Chatgpt get to know the context of the thing u 
        are talking about and then replies in the context we are talking about 
        [Fair enough😄,Wanna keep it chill, or dive into something nerdy —— AI,operating systems,S#,regex wiredness,startup ideas, whatever's on your mind?] 
        so here what i mean by stateless. it doesn't really contain any state.we have to keep sending it all of this data and that's 
        why we have messages which is a 'list[dict]' -> in this why  it is sotored on this method is because
        """
        pass
