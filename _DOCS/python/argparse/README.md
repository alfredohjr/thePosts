# argparse

---

creation: 2024-01-02 18:32:30

---

## Introdução

Continuamente estou escrevendo scripts, em alguns momentos até mais do que criando programas, classes e tudo mais que o OOP tem a nos oferecer, e sem dúvida um script no qual você não precisa dar manutenção em toda execução trocando variáveis aqui ou ali para executar é muito melhor!

Uma confissão e um mesmo tempo um agradecimento ao copilot, sem ele talvez eu evitaria ou adiaria a implementação dessas opções na linha de comando, ele faz a parte pesada do negócio, testando a mim a revisão para ver se tudo está certo.

Agora, vamos ao exemplo prático desta bagaça.

## Exemplos

Este script é usado neste repositório para gerar um padrão de arquivos e pastas, da minha parte agora só é necessário indicar a pasta e assunto via linha de comando para criar o básico do básico, e isso é fantástico em vários sentidos.

o exemplo completo pode ser visto [aqui](
https://github.com/alfredohjr/thePosts/blob/master/src%2FcreateDOCSBase.py)

o bloco que nos interessa é esse:

```python 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create the base of the documentation')
    parser.add_argument('--folder', type=str, help='Folder to create the documentation')
    parser.add_argument('--subject', type=str, help='Subject of the documentation')

    args = parser.parse_args()

    run(folder=args.folder,subject=args.subject)
```

desta forma, se eu simplesmente chamar o script assim no terminal.

```bash
python src/createDOCSBase.py --folder python --subject "how datetime module works"
```

e já vai ser criado um arquivo base para que depois eu possa editar.

esse é um exemplo bem simples do que pode ser feito.

você pode chamar isso num subprocess por exemplo, pegar uma lista de tópicos e adicionar, da mesma forma pode importar a função run num outro script e também gerar várias estruturas básicas, mas já prontas.

por hoje é só, e aí, gostou da dica, alguma sugestão? manda aí.
