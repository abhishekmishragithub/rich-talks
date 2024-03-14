# default print
print("the addition of 2+3 is =", 2+3)
print({"a":[1,2,4], "b":{"x":12, "y":34}})
print("this is some text")

# with rich
from click import style
from rich import print
print("the addition of 2+3 is =", 2+3)
print({"a":[1,2,4], "b":{"x":12, "y":34}})



# the right way to do rich
from rich.console import Console
console = Console()
console.print("the addition of 2+3 is =", 2+3)
console.print("this is some text", style="bold")
console.print("this is some text", style="bold underline blue")
console.print("this is some text", style="bold underline blue on white")

# subset
console.print("[bold] this [underline]is[/] some text[/]")

# theme
from rich.theme import Theme

custom_theme = Theme(
    {
        "sucess":"green",
        "failure": "bold red"

    }
)
console = Console(theme=custom_theme)
console.print("this is sucess", style="sucess")
console.print("this is failure", style="failure")
console.print("[failure] auth failed[/]")
