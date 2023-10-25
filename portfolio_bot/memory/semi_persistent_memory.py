from langchain.memory import RedisChatMessageHistory, ConversationBufferMemory

from .memory import XAgentMemory


class SemiPersistentChatMemory(XAgentMemory):
    def __init__(self, *, user_id: str, memory_key: str):
        """Initialize the SemiPersistentChatMemory.

        Args:
            user_id (str): The user's id (required).
            memory_key (str): The key where the chat history will load. Probably get it from `CustomXAgentPrompt`
        """
        if not user_id or not memory_key:
            raise ValueError(
                "`user_id` and `memory_key` is required to instantiate the Memory."
            )
        self._user_id = user_id
        message_history = RedisChatMessageHistory(
            url=self._get_redis_url(), ttl=600, session_id=self._user_id
        )
        self._memory = ConversationBufferMemory(
            memory_key=memory_key, chat_memory=message_history
        )

    @property
    def memory(self):
        return self._memory

    def _get_redis_url(self) -> str:
        """Get the redis connection url"""
        # TODO: validate and verify the redis db before sending back the url. This will prevent any complicated errors related to redis.
        host = "127.0.0.1"
        port = "6379"
        return f"redis://{host}:{port}"
