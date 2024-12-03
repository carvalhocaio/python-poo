# While

Imagine que estamos desenvolvendo um programa para uma aplicação de entrada de dados em que precisamos coletar informações do usuário. Uma das informações que precisamos é um número positivo, e queremos garantir que o usuário forneça um valor válido.

Nosso desafio é criar um código que solicite ao usuário que insira um número positivo. No entanto, como não podemos confiar no usuário para fornecer um valor válido na primeira tentativa, precisamos criar uma lógica que permita solicitar novamente até que o usuário finalmente insira um número válido.

Podemos utilizar a estrutura de repetição `for` para solicitar esse valor até que essa condição seja satisfeita, como mostrado no código seguinte:

```python
numero = -1
for _ in range(3):  # Supondo um número máximo de tentativas (3) arbitrário
    numero = int(input("Digite um número positivo: "))
    if numero > 0:
        break

print("Você digitou:", numero)
```

Perceba que, para criar esse loop, precisamos definir um número arbitrário de tentativas para que o usuário inserisse esse valor. Isso acontece porque o loop `for` é utilizado quando se conhece previamente o número de iterações que devem ser realizadas.

Contudo, nós queremos que o usuário digite diversas vezes até que ele coloque um valor positivo e não tenha nenhuma limitação.

Neste caso, a estrutura `for` não consegue satisfazer o que desejamos para nosso código. E agora? O Python tem outra estrutura que podemos utilizar? A resposta é sim!

Essa linguagem oferece duas estruturas de controle de fluxo fundamentais para a execução de blocos de repetiação: o `for` e o `while`. Ambas são utilizadas para a implementação de loops, permitindo que um bloco de código seja executado repetidamente enquanto determinadas condições são atendidas.

O loop `for` é utilizado quando se conhece previamente o número de iterações que devem ser realizadas. Ele é especialmente eficaz ao percorrer elementos em sequências, como listas, tuplas, strings ou ranges.

O loop `while`, diferente do `for`, é utilizado quando o número de iterações não é conhecido de antemão, mas ainda assim depende de uma condição específica para manter o bloco de código em repetição. Ele continua a executar o bloco de código enquanto a condição fornecida for avaliada como verdadeira.

A sintaxe do loop `while` é a seguinte:

```python
while condição:
    # Bloco de código a ser repetido
```

O bloco de código dentro do `while` continuará a ser executado até a condição se torne falsa, ou seja, ele apenas será executado quando a condição assumir o valor booleano de `true`. Isso siginifica que é essencial e necessário garantir que a condição eventualmente se torne falsa para evitar um loop infinito em seu projeto.

Então podemos adaptar nosso projeto anterior para utilizar o while ao invés do for, como vemos no código a seguir:

```python
numero = -1
while numero <= 0:
    numero = int(input("Digite um número positivo: "))

print("Você digitou:", numero)
```

Enquanto o número digitado for menor ou igual a zero, o programa continuará pedindo ao usuário que insira um número positivo. Quando o usuário finalmente fornecer um número positivo, o loop `while` será encerrado e o programa exibirá o número digitado.

Sendo assim, esse é um cenário em que loop `while` é mais apropriado, pois não sabemos com antecedência quantas vezes precisaremos solicitar ao usuário que insira um número.

Ou seja, a escolha entre `for` e `while` dependerá da natureza específica do problema que você está resolvendo. Entender as nuances a aplicar a estrutura de controle de fluxo mais apropriada contribuirá para um código mais claro e eficiente a depender do seu projeto.

---
