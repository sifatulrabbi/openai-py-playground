from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.tools import MoveFileTool, format_tool_to_openai_function


load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")
tools = [MoveFileTool()]
functions = [format_tool_to_openai_function(t) for t in tools]
message = model.predict_messages(
    [HumanMessage(content="move file foo to bar")], functions=functions
)

print(message)
print(message.additional_kwargs["function_call"])
