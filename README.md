# Sistema Bancário – Etapa 2

## Centro Universitário de Viçosa – UNIVIÇOSA

*Disciplina:* INF101 – Programação de Computadores I  
*Aluno:* Lucas Pinheiro de Souza Pereira 
*Matrícula:* 27256
*Trabalho:* Implementação de um Sistema de Registro e Gestão de Contas Bancárias

---

## 1. Descrição do Projeto

Este projeto consiste no desenvolvimento de um sistema bancário utilizando a linguagem C++.

O programa permite cadastrar e gerenciar várias contas bancárias, realizar operações financeiras e consultar o histórico de movimentações.

Nesta segunda etapa, foram utilizados arrays para armazenar os dados das contas e as movimentações realizadas durante a execução do programa.

## 2. Funcionalidades

O sistema possui as seguintes funcionalidades:

1. *Cadastrar contas:* permite cadastrar uma nova conta bancária com número, nome do cliente, CPF e tipo de conta.
2. *Listar contas:* apresenta todas as contas cadastradas.
3. *Consultar conta:* permite pesquisar uma conta pelo número.
4. *Realizar depósitos:* adiciona um valor ao saldo da conta.
5. *Realizar saques:* retira um valor da conta, verificando se existe saldo suficiente.
6. *Realizar transferências:* transfere valores entre duas contas cadastradas.
7. *Exibir extrato:* apresenta as movimentações financeiras de uma conta.

## 3. Tecnologias Utilizadas

- Linguagem C++
- Compilador G++
- Arrays (vetores)
- Estruturas condicionais (if e else)
- Estruturas de repetição (for e do while)
- Funções
- Biblioteca iostream
- Biblioteca string
- Biblioteca iomanip

## 4. Armazenamento dos Dados

O sistema utiliza arrays para armazenar as informações.

*Contas bancárias:*
- Número da conta.
- Nome do cliente.
- CPF.
- Tipo de conta.
- Saldo.
- Situação da conta.

*Histórico de movimentações:*
- Número da conta.
- Tipo de movimentação.
- Valor movimentado.

Limites utilizados:
- Máximo de 100 contas.
- Máximo de 500 movimentações.

Os dados permanecem armazenados somente na memória durante a execução do programa.

## 5. Tipos de Movimentações

| Código | Movimentação |
|---|---|
| D | Depósito |
| S | Saque |

Nas transferências, são registrados dois lançamentos: uma saída na conta de origem e uma entrada na conta de destino.

## 6. Como Executar o Programa

Primeiro, é necessário ter um compilador C++ instalado.

Abra o terminal na pasta onde está o arquivo main.cpp e execute:

bash
g++ main.cpp -o sistema


Depois, execute o programa:

*Windows:*
bash
sistema.exe


*Linux:*
bash
./sistema


## 7. Validações do Sistema

O programa possui verificações para evitar operações incorretas:

- Não permite cadastrar contas com números repetidos.
- Não permite valores negativos ou iguais a zero nas operações financeiras.
- Não permite realizar saques com saldo insuficiente.
- Não permite transferências para a mesma conta.
- Verifica se as contas de origem e destino existem e estão ativas.
- Verifica o espaço disponível no histórico de movimentações.

## 8. Objetivo do Trabalho

O objetivo deste trabalho é colocar em prática os conhecimentos adquiridos na disciplina de Programação de Computadores I, utilizando a linguagem C++.

O projeto permite compreender o uso de arrays, funções, estruturas condicionais e estruturas de repetição na criação de um sistema de gerenciamento bancário.

## 9. Considerações Finais

O desenvolvimento deste sistema possibilitou aplicar os conceitos de programação estudados em sala de aula, criando um programa capaz de realizar operações bancárias básicas.

O sistema atende às funcionalidades solicitadas na Etapa 2 do trabalho, mantendo as contas e movimentações em memória durante sua execução.

---

*Desenvolvido por:* Lucas Pinheiro de Souza Pereira  
*Disciplina:* INF101 – Programação de Computadores I  
*Instituição:* UNIVIÇOSA – Centro Universitário de Viçosa  
*Ano:* 2026
