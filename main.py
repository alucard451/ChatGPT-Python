"""Principal """

import os
from rich import print
from rich.table import Table
import typer
import openai

import config


def main():
    openai.api_key = config.OPENAI_API_KEY

    presentacion()

    while True:
        pregunta = validacion_preguntas()
        # print(pregunta)
        mensajes = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": pregunta}])

        print(
            f"> [bold blue]{mensajes.choices[0].message.content}[/bold blue]")


def presentacion():
    print("[bold green]Bienvenido a una aplicación de ChatGPT con Python[/bold green]")
    table = Table("Comando", "Descripción")
    table.add_row("Exit", "Cerrar la aplicación")
    print(table)


def validacion_preguntas() -> str:
    print("[bold yellow]Ingresa tu pregunta: [/bold yellow]")
    pregunta = typer.prompt("")

    if pregunta == "exit":
        exit = typer.confirm("Estás seguro de salir?")
        if exit:
            print("[red]Cerrando aplicación.[/red]")
            raise typer.Abort()
        else:
            validacion_preguntas()

    else:
        return pregunta


if __name__ == "__main__":
    typer.run(main)
