import click
import openai
import os 
import dotenv

# Load in .env file
dotenv.load_dotenv('.env')

@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    """
    A CLI wrapper around the openai API called 'gene'.
    """
    # click.echo(f"Debug mode is {'on' if debug else 'off'}")
    pass


@cli.command()
@click.argument('question')
@click.option('--model', '-m', default='gpt-3.5-turbo', help='Model to use.')
@click.option('--max-tokens', '-max_t', default=200, help='Maximum number of tokens for the AI to return.')
def ask(question: str, model: str, max_tokens: int) -> str:
    """Ask any question you can think of!"""
    check_openapi_key()
    # Check for user configured settings
    if os.getenv('MAX_TOKENS'):
        max_tokens = int(os.getenv('MAX_TOKENS'))
    if os.getenv('MODEL'):
        model = os.getenv('MODEL')
    if os.getenv('TEMPERATURE'):
        temperature = float(os.getenv('TEMPERATURE'))

    completion = create_completion_request(question, model=model, max_tokens=max_tokens)

    click.secho(completion, fg='green')
    return 

@cli.command()
@click.option('--verbose', '-v', is_flag=True, default=False)
def settings(verbose: bool) -> None:
    """Goes through configurable settings and prompts user for input. Leave blank for default."""
    # TODO: Allow user to pass in options to bypass going through all settings (don't prompt anything just change whats passed in) 

    model = click.prompt("Set model to use (Must be a chat completion model)", default='gpt-3.5-turbo', type=str)
    max_tokens = click.prompt("Set max tokens returned", default=200, type=str)
    temperature = click.prompt("Set model temperature to use", default=1.0, type=str)

    # Write these settings to the .env file
    for key, config in zip(['MODEL', 'MAX_TOKENS', 'TEMPERATURE'], [model, max_tokens, temperature]):
        if not dotenv.set_key('.env', key, config):
            with open(".env", "w") as f:
                f.write(key + "=" + config + "\n")

    if verbose:
        click.echo(f"Chat Completion Model: {model}")
        click.echo(f"Max tokens returned: {max_tokens}")
        click.echo(f"Model temperature: {temperature}")
    return 

def check_openapi_key() -> None: 
    """Check if the OPENAI_API_KEY environment variable is available."""
    if os.getenv("OPENAI_API_KEY") is None:
        key = click.prompt("Please enter your OPENAI_API_KEY", hide_input=True)
        if len(key) != 51:
            key = click.prompt("Please re-enter your OPENAI_API_KEY - it should be a 51 character string", hide_input=True) 
        openai.api_key = key
        with open(".env", "w") as f:
            f.write("OPENAI_API_KEY=" + key)
    else: 
        openai.api_key = os.getenv("OPENAI_API_KEY")
    return


def create_completion_request(question: str, context: str = '', max_tokens: int = 25, model: str = "gpt-3.5-turbo"):
    """Create a request to the OpenAI API to generate completions."""
    # Create a completions using the question and context
    completion = openai.ChatCompletion.create(
        model=model,
        messages=[
                {"role": "user", "content": question}
            ],
        max_tokens=max_tokens,
        )
    return completion.choices[0].message['content']

