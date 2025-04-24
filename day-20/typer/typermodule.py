import typer
app=typer.Typer() #object is app

@app.command()
def greet(name:str, age:int=typer.Option(18,help="your age")):
    typer.echo(f"Hello {name}!you are {age} years old")

if __name__=="__main__":
    app()


