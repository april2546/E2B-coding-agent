# Data Analysis Agent
The code in this repository is for building a coding agent run in an E2B sandbox for secure execution. There is also a Gradio UI component for a nicer user experience while chatting. Any helper methods are in the `/lib` directory which are imported into the JupyterNotebook for the agent to use.

## Requirements
- The E2B API Key is in the .env file that is directly accessed by the code
- An OpenAI api key is also necessary as this is a data analysis agent running using OpenAI

## To Run
The executable file is `data-analysis-agent.ipynb`, and there are 2 `.csv` files for the agent to run analysis on. Try it out with other csv files for your own analysis!
