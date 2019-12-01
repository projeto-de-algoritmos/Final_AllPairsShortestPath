# Kattis - All Pairs Shortest Path

**Número da Lista**: 6 <br>
**Conteúdo da Disciplina**: Grafos <br>

## Alunos

|Matrícula | Aluno | GitHub |
| -- | -- | -- |
| 16/0010195 | João Vítor Morandi | [@joaovitorml](https://github.com/joaovitorml) |
| 16/0006210 | Francisco Heronildo | [@FranciscoHeronildo](https://github.com/FranciscoHeronildo) |

## Sobre

Problema encontrado no [Kattis Problems](https://open.kattis.com/problems/allpairspath) relacionado a Grafos com o intuito de fixar o conteúdo ministrado na disciplina.

## Screenshots

![img]()

## Instalação

**Linguagem**: Python <br>

## Uso

Clone o Repositório: `$ git clone https://github.com/projeto-de-algoritmos/Final_AllPairsShortestPath.git` </br>
Acesse o diretório: `$ cd Final_AllPairsShortestPath.git` </br>
Execute: `$ python kattis-All_Pairs_Shortest_Path.py` </br>

## Outros

<h1 align="center">All Pairs Shortest Path<br/>

<h2>Input</h2>

<p>The input consists of several test cases. Each test case starts with a line with three non-negative integers, 1≤𝑛≤150, 0≤𝑚≤5000 and 1≤𝑞≤1000, separated by single single spaces, where 𝑛 is the numbers of nodes in the graph, 𝑚 the number of edges and 𝑞 the number of queries. Nodes are numbered from 0 to 𝑛−1. Then follow 𝑚 lines, each line consisting of three (space-separated) integers 𝑢, 𝑣 and 𝑤 indicating that there is an edge from 𝑢 to 𝑣 in the graph with weight −1000≤𝑤≤1000. Then follow 𝑞 lines of queries, each consisting of two node numbers 𝑢 and 𝑣 (separated by a space), asking for the minimum distance from node 𝑢 to node 𝑣. Input will be terminated by a line containing 0 0 0, this line should not be processed.</p>

<h2>Output</h2>

<p>For each query, output a single line containing the minimum distance from node 𝑢 to 𝑣, or the word Impossible if there is no path from 𝑢 to 𝑣, or -Infinity if there are arbitrarily short paths from 𝑢 to 𝑣. Print a blank line after each test case.</p>

| Sample Input 1 | Sample Output 1 |
| :-- | :-- |
| 4 3 4 </br> 0 1 2 </br> 1 2 2 </br> 3 3 1 </br> 0 2 </br> 1 2 </br> 3 0 </br> 3 3 </br> 2 1 2 </br> 0 1 100 </br> 0 1 </br> 1 0 </br> 0 0 0 | 4 </br> 2 </br> Impossible </br> 0 </br> </br> </br> </br> 100 </br> Impossible |
