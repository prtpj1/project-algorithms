# 34º Projeto Algorithms: 
<p align="center">
<img src="https://github.com/prtpj1/prtpj1/blob/main/Headers/34-Algorithms.jpeg?raw=true" alt="Header" />

---
<p align="center">
<a href="#project-description">Project Description</a> •
<a href="#in-this-project-i-learned-and-put-into-practice">Learning</a> •
<a href="#according-to-the-project-requirements-designated-by-trybe-i-learned-how-to">Requirements</a> •
<a href="#stacks">Stacks</a> •
<a href="#how-to-run-the-application">How to run the application</a>
</p>

---
<p align="center">
<a href="#descrição-do-projeto">Descrição do Projeto</a> •
<a href="#nesse-projeto-aprendi-e-coloquei-em-prática">Aprendizado</a> •
<a href="#de-acordo-com-os-requisitos-do-projeto-designados-pela-trybe-aprendi-como">Requisitos</a> •
<a href="#tecnologias-utilizadas">Tecnologias Utilizadas</a> •
<a href="#como-rodar-a-aplicação">Rodar a Aplicação</a>
</p>

---
## Project Description
I completed this Computer Science project in Python during my learning period at Trybe, where I developed functions to solve problems and optimize algorithms. This helped me further develop my ability to implement solutions for various everyday problems!

## In this project, I learned and put into practice:
- Logic
- Ability to interpret problems
- Ability to interpret legacy code
- Ability to optimize problem-solving

---
## According to the project requirements designated by Trybe, I learned how to:
- ✅ Search and return the number of students studying at the same time `(Search Algorithm)`
- ✅ Implement the test for the encrypt_message function
- ✅ Return whether the word is a palindrome or not `(Recursion)`
- ✅ Compare two strings, sort them, and identify if one is an anagram of the other `(Sorting Algorithm)`

#### Bonus Requirements:
- ❌ Find (if any) and return repeated numbers in a list `(Search Algorithm)`
- ❌ Return whether the word is a palindrome or not `(Iteration)`

_*Note: In some projects, some requirements were not completed due to the accelerated dynamics of the course, not because I didn't know how to do them. At the time, I just needed a little more time.*_

_*I still haven't decided if it's better to leave it this way to demonstrate my progress during my learning or if it would be better to complete the requirements that were missing in the course projects.*_

_*Feedback is welcome.*_

---
## Stacks
### BackEnd:
- Python

<a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://github.com/prtpj1/prtpj1/blob/main/Github%20Imgs/Python2.png?raw=true" width="50" height="50" alt="Python Icon" /></a>

---
## How to run the application?
- Clone the repository: <br>
`git clone git@github.com:prtpj1/project-algorithms.git`
- Navigate to the project folder: <br>
`cd project-algorithms`
- Create and activate the virtual environment: <br>
`python3 -m venv .venv && source .venv/bin/activate`
- Install dependencies: <br>
`python3 -m pip install -r dev-requirements.txt`
- You can execute the functions using the commands below in the terminal: <br>
`python3 challenges/challenge_study_schedule.py`<br>
`python3 challenges/challenge_palindromes_recursive.py`<br>
`python3 challenges/challenge_anagrams.py`
- If you want to try the functions with different parameters, you can access the python terminal: <br>
`python3`
- And execute the functions with new parameters, for example: <br>
##### Function that searches and returns the number of students studying at the same time: <br>
`from challenges.challenge_study_schedule import study_schedule`<br>
`study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 4)`<br>
##### Function that checks if a word is a palindrome: <br>
`from challenges.challenge_palindromes_recursive import is_palindrome_recursive`<br>
`is_palindrome_recursive("LEVEL", 0, 4)`<br>
`is_palindrome_recursive("REVIVE", 0, 5)`<br>
##### Function that compares two words and checks if one is an anagram of the other: <br>
`from challenges.challenge_anagrams import is_anagram`<br>
`is_anagram("stone", "notes")`<br>
`is_anagram("listen", "silent")`<br>

_*Note: If you have any difficulties with the instructions and would like to give feedback, send me a message*_

---
## Descrição do Projeto
Fiz este projeto de Ciência da Computação em Python, durante meu período de aprendizagem na Trybe, onde desenvolvi funções para resolver problemas e otimizar algoritmos, o que me ajudou a desenvolver mais a minha capacidade de implementar soluções para os mais diversos problemas do dia a dia!

## Nesse projeto, aprendi e coloquei em prática:
- Lógica
- Capacidade de interpretação de problemas
- Capacidade de interpretação de um código legado
- Capacidade de otimizar a resolução de problemas

---
## De acordo com os requisitos do projeto designados pela Trybe aprendi como:
- ✅ Buscar e retornar o número de estudantes estudando no mesmo horário `(Algoritmo de busca)`
- ✅ Implementar o teste para a função encrypt_message
- ✅ Retornar se a palavra é um palíndromo ou não `(Recursividade)`
- ✅ Comparar duas strings, ordená-las e identificar se uma é um anagrama da outra `(Algoritmo de ordenação)`

#### Requisitos Bônus:
- ❌ Encontrar (se houver) em uma lista e retornar números os repetidos `(Algoritmo de busca)`
- ❌ Retornar se a palavra é um palíndromo ou não `(Iteratividade)`


_*OBS: Em alguns projetos alguns requisitos não foram feitos devido a dinâmica acelerada do curso e não por eu não saber como fazê-los. Na época eu apenas precisaria de um pouco mais de tempo.*_

_*Ainda não decidi se é melhor deixar desta forma para demonstrar o meu progresso durante meu aprendizado ou se seria melhor completar os requisitos que ficaram faltando nos projetos do curso.*_

_*Feedbacks são bem vindos.*_

---
## Tecnologias Utilizadas
### BackEnd:
- Python

<a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://github.com/prtpj1/prtpj1/blob/main/Github%20Imgs/Python2.png?raw=true" width="50" height="50" alt="Python Icon" /></a>

---
## Como rodar a aplicação?
- Clone o repositório: <br>
`git clone git@github.com:prtpj1/project-algorithms.git`
- Acesse a pasta do projeto: <br>
`cd project-algorithms`
- Crie e habilite o ambiente virtual: <br>
`python3 -m venv .venv && source .venv/bin/activate`
- Instale as dependências: <br>
`python3 -m pip install -r dev-requirements.txt`
- Você pode executar as funções através dos comandos abaixo no terminal: <br>
`python3 challenges/challenge_study_schedule.py`<br>
`python3 challenges/challenge_palindromes_recursive.py`<br>
`python3 challenges/challenge_anagrams.py`
- Se quiser experimentar as funções com outros parâmetros, você pode acessar o terminal python: <br>
`python3`
- E executar as funções com novos parâmetros, por exemplo: <br>
##### Função que busca e informa o número de estudantes estudando no mesmo horário: <br>
`from challenges.challenge_study_schedule import study_schedule`<br>
`study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 4)`<br>
##### Função que verifica se a palavra é um palíndromo ou não: <br>
`from challenges.challenge_palindromes_recursive import is_palindrome_recursive`<br>
`is_palindrome_recursive("RADAR", 0, 4)`<br>
`is_palindrome_recursive("AMOR", 0, 3)`<br>
##### Função que compara duas palavras e informa se uma é um anagrama da outra: <br>
`from challenges.challenge_anagrams import is_anagram`<br>
`is_anagram("perda", "pedra")`<br>
`is_anagram("teste", "testa")`<br>

---
_*OBS: Se tiver alguma dificuldade com as instruções e quiser dar um feedback me mande uma mensagem*_

---
