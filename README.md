# Gene - Simple ChatGPT Terminal Access.
Gene is a command-line tool that allows quick access to OpenAI's GPT-3 language model without leaving the terminal. With Gene, you can easily generate natural language text for a variety of tasks, such as generating code snippets, composing documentation, and more.

When you ask gene for any code snippet, it will automatically copy the code portion to your clipboard.
```python
gene ask "Can you write a python function to generate a random number?" 
```

![gene example](./assets/Gene%20example.PNG)



# Installation 
Currently, you need to locally install with pip.Clone the git repository and run: 
```
pip install .
```
To use Gene, you will also need an OpenAI API key. You can obtain one by following the instructions on the [OpenAI website](https://platform.openai.com/docs/api-reference/introduction). The first time running your 'gene ask' command it will ask for you API key. It will write it to a .env file where it can be referenced in future requests. 


# License
Gene is licensed under the MIT license.