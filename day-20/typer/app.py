# Install type
import typer

app = typer.Typer()

@app.command()
def greet(name: str, age: int = typer.Option(18, help="Your age")):
    typer.echo(f"Hello {name}! You are {age} years old.")

if __name__ == "__main__":
    app()