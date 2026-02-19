from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

prompt = PromptTemplate(
    template="Answer the following question \n {question} from the following text - \n {text}",
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://www.amazon.com/Apple-2025-MacBook-13-inch-Laptop/dp/B0DZD91W4F/ref=sr_1_3?crid=1HAX1FJ5VSGEN&dib=eyJ2IjoiMSJ9.RhEwzvALwVBeDAnr2Dz1oFWG_ddvtFRRt92P4BBRiwvJNDFwpY2HDaX5_F6g9Ic3syRtu9sMhVLTik-Aws5JPMds-VobMX_T2ZbM7uXFeT_MZl35WJzYSHDf2BNEV0EzfBn8jEeY1hWoYBPAhVeGSdo-7hJOP2zdYYuN_vqiPm2KnkwACrd4TE2GOZYk5cE7RyGO492RQf-mOC578kj5_sJH6_tocBgnGZJZSm7G4xk.SqQ9UWpPHLG0PRtu0a61spOm431OUG07yMH6LY9XCBM&dib_tag=se&keywords=apple%2Bmacbook&qid=1771471561&sprefix=apple%2Bmacbook%2Caps%2C207&sr=8-3&th=1'
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))