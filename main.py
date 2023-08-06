"""Principal """

import os
from rich import print
from rich.table import Table
import typer
import openai

import config


def presentacion():
    print("[bold green]Bienvenido a una aplicación de ChatGPT con Python[/bold green]")
    table = Table("Comando", "Descripción")
    table.add_row("Exit", "Cerrar la aplicación")
    # table.add_row("Contexto", "Modificar el contexto/prompt del chat")
    print(table)


def validacion_input() -> list:
    print("[bold yellow]Ingresa tu pregunta o comando: [/bold yellow]")
    entrada = typer.prompt("")

    # if entrada == "contexto":

    #     context.clear()
    #     prompt = input("Ingresar el contexto/prompt deseado: ")
    #     context = contexto_chat(prompt)

    if entrada == "exit":
        salir = typer.confirm("Estás seguro de salir?")
        if salir:
            print("[red]Cerrando aplicación.[/red]")
            raise typer.Abort()
        else:
            validacion_input()

    else:
        datos = [entrada, context]
        return datos


def contexto_chat(contexto) -> list:

    contexto = [{"role": "system", "content": contexto}]
    return contexto


def pregunta_chat(datos):

    datos[1].append({"role": "user", "content": datos[0]})

    response = datos[1]
    return response


context = contexto_chat("Eres un asistente")


def main():
    openai.api_key = config.OPENAI_API_KEY

    # contexto del asistente

    presentacion()

    while True:
        datos = validacion_input()
        # print(datos)

        conversacion = pregunta_chat(datos)
        # print(conversacion)

        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=conversacion)

        response = respuesta.choices[0].message.content

        conversacion.append({"role": "assistant", "content": response})

        # print(conversacion)

        print(
            f"> [bold blue]{response}[/bold blue]")


if __name__ == "__main__":
    typer.run(main)
