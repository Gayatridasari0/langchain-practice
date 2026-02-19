from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

output_parser = CommaSeparatedListOutputParser()
format_instructions = output_parser.get_format_instructions()

prompt = PromptTemplate(
    template = "List five {subject}.\\n{format_instructions}",
    input_variables=['subject'],
    partial_variables={'format_instructions':format_instructions}
)

chain = prompt | model | output_parser

result = chain.invoke({'subject':'ice cream flavors'})

print(result)