# Tuplas vs Listas

As tuplas são estruturas de dados que nos permitem armazenar elementos de maneira ordernada e sequencial, assim como as listas. Dessa forma, ambas mantêm a ordem dos elementos e oferecem índices para acessar esses valores.

Contudo, existem diferenças fundamentais entre tuplas e listas que as tornam adequadas para diferentes situações.

## Sintaxe

O primeiro ponto que diferencia esses dois arranjos é a sintaxe de cada um. Como vimos, as listas são definidas utilizando colchetes `[ ]`, enquanto as tuplas são definidas utilizando parênteses `( )`, como mostra o exemplo a seguir:

```python
lista = [1, 'qualé', True, 9.7]
tuplas = (1, 'qualé', True, 9.7)
```

## Mutabilidade

A maior diferença entre essas duas configurações são suas propriedades de mutabilidade.

As listas são estruturas mutáveis, o que significa que é possível modificar seus elementos, adicionar novos itens ou remover existentes após a criação da lista, podendo inclusive utilizar funções próprias para isso como `append()`, `remove()`, `pop()`, e `insert()`.

Ao contrário das listas, tuplas são imutáveis. Uma vez que uma tupla é criada, seus elementos não podem ser alterados, adicionados ou removidos.

## Desempenho

Devido à sua imutabilidade, as tuplas têm um desempenho melhor de que listas para algumas operações. Elas são mais eficientes em termos de espaço e processamento em determinados cenários.

Sendo assim, listas podem ser menos eficientes em termos de desempenho para operações específicas, especialmente quando se trata de manipulação de grandes conjuntos de dados, devido à sua mutabilidade.

## Quando devo utilizar cada estrutura?

As listas são ideais quando você precisa de uma coleção de elementos que pode ser modificada ao longo do tempo. Por exemplo, ao criar uma lista de tarefas que pode ser atualizada com novos itens ou marcada como concluída.

Além disso, se você precisa adicionar, remover ou modificar elementos com frequência, as listas oferecem métodos próprios convenientes, como mencionado anteriormente. Podemos ver isso com uma lista de compras, como mostrado no código a seguir:

```python
# Criando uma lista de compras
lista_de_compras = ["Maçã", "Banana", "Leite", "Pão", "Queijo"]

# Adicionando um item à lista
lista_de_compras.append("Ovos")

# Removendo um item da lista
lista_de_compras.remove("Banana")

# Exibindo a lista
print("Lista de Compras:")
for item in lista_de_compras:
    print("- " + item)
```

Já as tuplas são apropriadas quando se deseja garantir que os elementos não sejam alterados após a criação. Isso é útil para dados que devem permanecer constantes ao longo do tempo. Como as tuplas são imutáveis, elas podem ter um desempenho ligeiramente melhor em operações de leitura e acesso a elementos. Isso também as tornam adequadas para situações em que a eficiência é crucial.

Podemos ver um exemplo de uma tupla que armazena as coordenadas geográficas de uma localização específica, que são dados imutáveis que queremos ter acesso, como mostrado a seguir:

```python
# Definindo uma tupla de coordenadas geográficas
coordenadas_gps = (40.7128, -74.0060)

# Exibindo as coordenadas
print("Coordenadas GPS:")
print("Latitude:", coordenadas_gps[0])
print("Longitude:", coordenadas_gps[1])
```

Lembre-se de sempre avaliar as condições de seu projeto e escolher qual das duas estruturas é mais adequada para cada situação.

---
