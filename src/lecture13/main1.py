from crewai.flow import Flow, start, listen
from litellm import completion

class LitellmFlow(Flow):
    @start()
    def start_function(self):
        output = completion(
            model="gemini/gemini-2.0-flash",
            messages=[
                {'role': 'user',
                 'content': 'Who is the founder of Pakistan?'}
            ]
        )
        return output['choices'][0]['message']['content']

def run_litellm_flow():
    obj = LitellmFlow()
    result = obj.kickoff()
    print(result)