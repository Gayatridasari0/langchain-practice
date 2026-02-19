from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

parser = JsonOutputParser()

template = PromptTemplate(
    template = 'Give me 5 facts about {topic} \n {format_instruction}',
    input_variables= ['topic'],
    partial_variables= {'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)