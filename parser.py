from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(api_key=os.environ["groq_api_key"], model='llama-3.1-70b-versatile')


template = """
			You are tasked with extracting specific content from the following text content: {dom_content}.
			Please Follow the following instructions carefully:


			1. **Extract Information** Only extract information that directly matches with the provided description: {desc}.
			2. **No Extra Content** Do not include any extra text, comments, explanations in your responses.
			3. **Empty Response** If no information matches the given description return an empty string ('').
			4. **Direct Data Only** Your output should contain only the data that is explicitly requested, with no other text.
"""


def parse_with_llm(batch_content, description):
	prompt_extract = PromptTemplate.from_template(template)
	chain = prompt_extract|llm
	
	parsed_result = []

	for i, chunk in enumerate(batch_content, start=1):
		response = chain.invoke({"dom_content":chunk, "desc":description})
		print(f'Parsed batch: {i} of {len(chunk)}')
		parsed_result.append(response.content)

	return "\n".join(parsed_result)