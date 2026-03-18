# cli.py

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from bot.agent import GeniusAgent

console = Console()
agent = GeniusAgent()

def print_welcome():
    welcome_text = Text()
    welcome_text.append(" Apple Genius Bar\n", style="bold white")
    welcome_text.append("Your support specialist is ready to help.\n", style="dim white")
    welcome_text.append("\nType ", style="dim white")
    welcome_text.append("reset", style="bold cyan")
    welcome_text.append(" to start a new session or ", style="dim white")
    welcome_text.append("quit", style="bold cyan")
    welcome_text.append(" to exit.", style="dim white")

    console.print(Panel(welcome_text, style="bold white", padding=(1, 4)))

def print_Armani(message: str):
    console.print(Panel(message, title="[bold white] Armani[/bold white]",
                        title_align="left", style="white", padding=(1, 2)))

def print_user(message: str):
    console.print(Panel(message, title="[bold cyan]You[/bold cyan]",
                        title_align="left", style="cyan", padding=(1, 2)))

def main():
    print_welcome()

    while True:
        user_input = console.input("\n[bold cyan]You:[/bold cyan] ").strip()

        if not user_input:
            continue

        if user_input.lower() == "quit":
            console.print("\n[dim white]Thanks for visiting the Genius Bar. Have a great day! [/dim white]\n")
            break

        if user_input.lower() == "reset":
            agent.reset()
            console.print("\n[dim white]Session reset. Starting fresh![/dim white]\n")
            continue

        print_user(user_input)

        with console.status("[dim white]Armani is thinking...[/dim white]", spinner="dots"):
            response = agent.chat(user_input)

        print_Armani(response)

if __name__ == "__main__":
    main()