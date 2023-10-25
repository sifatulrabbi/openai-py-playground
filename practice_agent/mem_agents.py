from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.prompts.chat import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
)


def mem_completion_chain():
    """LLM Chain that uses completion models with memory."""
    template = """You are a chatbot having a conversation with a human.

    {chat_history}
    Human: {human_input}
    Chatbot:"""

    prompt = PromptTemplate(
        input_variables=["chat_history", "human_input"], template=template
    )
    memory = ConversationBufferMemory(memory_key="chat_history")
    llm = OpenAI()
    llm_chain = LLMChain(llm=llm, memory=memory, prompt=prompt, verbose=True)
    return llm_chain


def mem_chat_chain():
    llm = ChatOpenAI(temperature=0.5)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
                content="You are a chatbot having a conversation with a human."
            ),  # This is a persistent system message.
            MessagesPlaceholder(
                variable_name="chat_history"
            ),  # This is where the memory history will be loaded.
            HumanMessagePromptTemplate.from_template(
                "{human_input}"
            ),  # Where the human message will be loaded.
        ]
    )
    chat_llm_chain = LLMChain(llm=llm, memory=memory, prompt=prompt, verbose=True)
    return chat_llm_chain
