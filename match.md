# Instrução match

Ao explorarmos as intruções `if else` percebemos que elas são uma poderosa e fundamental construção da linguagem, que nos permite controlar o fluxo do código com base em condições lógicas que determinamos de acordo com a necessidade de nosso projeto.

Com o surgimento de novas versões do Python, a linguagem de programção continua a evoluir e se aprimorar, trazendo consigo uma variedade de novas funcionalidades que enriquecem a experiência e a legibilidade do código, mas também oferecem aos desenvolvedores ferramentas mais poderosase expressivas para lidar com desafios diversos.

Dentre as funcionalidades mais recentes, destaca-se a introdução da instrução `match` no Python 3.10, oferecendo uma abordagem mais elegante para a correspondência de padrões em dados. Essa adição não apenas simplifica a lógica do código, mas também proporciona uma alternativa expressiva e legível às construções tradicionais de controle de fluxo, como `is elif else`, que são necessários para adaptar o comportamento do programa, como vimos anteriormente.

A principal finalidade da instrução match é simplificar a lógica de código ao facilitar o trabalho com diferentes padrões de dados. Isso pode tornar o código mais legível e consiso em situações onde uma cadeia de `if elif else` pode se tornar complicada e difícil de manter.

## Sintaxe do Match

```python
opcao_escolhida = int(input('Escolha uma opção: '))
if opcao_escolhida == 1:
    print('Adicionar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurantes')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
elif opcao_escolhida == 4:
    print('Finalizar app')
else:
    print('Opção inválida!')
```

Se decidirmos utilzar a instrução `match` nesse caso, obteríamos a seguinte resultado:

```python
opcao_escolhida = int(input('Escolha uma opção: '))
match opcao_escolhida:
    case 1:
        print('Adicionar restaurante')
    case 2:
        print('Listar restaurantes')
    case 3:
        print('Ativar restaurante')
    case 4:
        print('Finalizar app')
    case _:
        print('Opção inválida!')
```

Perceba que recebemos a variável `opcao_escolhida` como parâmetro da instrução match e será feito um comparativo com todos os valores determinados pelos blocos de case, e no final temos uma instrução `case _`, que é um padrão curinga, que corresponde a qualquer valor que não tenha sido correspondido pelos casos anteriores, ou seja, equivalente ao `else` da condicional anterior.

## Qual instrução devo usar?

O `if` nos proporciona uma maneira eficaz de tomar decisões simples ou complexas em nosso código, adaptando o comportamento do programa de acordo com as circustâncias determinadas. Ao usar `match`, podemos simplificar a lógica do código em situações que envolvem múltiplos padrões complexos. Ela oferece uma estrutura mais legível, especialmente quando temos diversos casos a serem tratados.

### Vantagens da Instrução `match`

- Lidar com condições complexas e múltiplos padrões de maneira mais intuitiva.
- Sintaxe concisa melhora a legibilidade do código, especialmente em casos complexos.
- Permite desestruturação direta, evitando repetiçao excessiva de variáveis.
- Adiciona expressividade ao código, especialmente em situações de correspondência de padrões.

### Vantagens da Instrução `if`

- Implementação clássica a amplamente conhecida.
- Amplamente suportada em todas as versões do Python.
- Estrutura simples e direta para lógica condicional básica.
- Pode ser mais intuitiva para devs familiarizados com estruturas de controle convencionais.

No geral, tanto `if` quanto o `match` são ferramentas poderosas à disposição de pessoas desenvolvedoras de Python. A escolha entre elas depende das necessidades específicas do seu código e das preferências da pessoa que está a desenvolver o código. A instrução `match` oferece uma nova abordagem elegante para a correspondência de padrões, abrindo novas possibilidades e aprimoramento e expressividade do código.

---
