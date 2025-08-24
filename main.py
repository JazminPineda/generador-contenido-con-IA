from langchain_ollama import OllamaLLM


def main():
    tema = input("De que tema quieres que hable el articulo? ")
    prompt = "Generar un articulo  para un blog personal de tecnologia y bussiness inteligence"
    "El articulo debe tener un titulo llamativo, un sutitulo y al menos 3 parrafos de contenido"
    "el articulo debe estar en español y ser apto para todo publico"
    "El articulo debe tener un tono amigalble y cercano"
    "El articulo debe tener una extension de al menos 500 palabras"
    "la salida debe estar en formato markdown"
    "El tema del articulo es " + tema

    model = OllamaLLM(model="llama3:8b")
    response = model.invoke(prompt)
    print(response)
    with open(f'{tema}.md', "w", encoding="utf-8") as f:
        output = f.write(response)


if __name__ == "__main__":
    main()