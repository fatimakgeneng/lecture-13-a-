First I ran main.py file using uv run kickoff to see if the gemini API key is working properly
config folder is working with main.py file in default (i.e I didn't utilize it in this project, it is covered in b project)

Then made a simple Q & A bot using liteLLM.
The file is main1.py and the command is uv run simple-llm


CMD Result

PS C:\Users\User\lecture-13-a-> uv run kickoff
      Built lecture13 @ file:///C:/Users/User/lecture-13-a-
Uninstalled 1 package in 30ms
Installed 1 package in 138ms
 Flow started with ID: 5d3214e3-e3ba-405e-9fea-4e43c7c73da9
Generating sentence count
Generating poem
# Agent: CrewAI Poem Writer
## Task: Write a poem about how CrewAI is awesome. Ensure the poem is engaging and adheres to the specified sentence count of 5.



# Agent: CrewAI Poem Writer
CrewAI, oh CrewAI, you're quite the clever tool! You wrangle tasks and agents, bending them to your rule. No more chaotic workflows, or projects in despair, with agents collaborating, problems disappear! So thank you, CrewAI, for making work feel cool!


Poem generated CrewAI, oh CrewAI, you're quite the clever tool! You wrangle tasks and agents, bending them to your rule. No more chaotic workflows, or projects in despair, with agents collaborating, problems disappear! So thank you, CrewAI, for making work feel cool!
Saving poem



PS C:\Users\User\lecture-13-a-> uv run simple-llm
 Flow started with ID: 7141b4f0-4aa0-471b-b3d7-69c5ffe1fc2e
Muhammad Ali Jinnah is considered the founder of Pakistan. He was the leader of the All-India Muslim League and advocated for the creation of a separate 
nation for Muslims in British India.

PS C:\Users\User\lecture-13-a-> 
