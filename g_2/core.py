import json
import os
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams
import g_2



def getSystemPrompt(q, rag_num_max=None, rag_max_distance=None):

        with open('documentation/shifter_resource.txt', 'r') as f:
            content = f.read()

        SYSTEM_PROMPT = f"""You are a g-2 ShifterBot, a helpful assistant that answers questions about shifter documentation and performs shifter actions.

        Here is some related shifter documentation for the g-2 experiment:
    	<documentation>
    	{content}
    	</documentation>


        Format your response as clear, bulleted instructions.

    	"""
        return SYSTEM_PROMPT
