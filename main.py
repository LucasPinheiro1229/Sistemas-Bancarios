#include <iostream>
#include <iomanip>
#include <string>
#include <limits>

using namespace std;

// Limites do sistema
const int MAX_CONTAS = 100;
const int MAX_MOVIMENTACOES = 500;

// Arrays das contas
int numeroConta[MAX_CONTAS];
string nomeCliente[MAX_CONTAS];
string cpf[MAX_CONTAS];
int tipoConta[MAX_CONTAS];
double saldo[MAX_CONTAS];
bool contaAtiva[MAX_CONTAS];

int quantidadeContas = 0;

// Arrays do historico de movimentacoes
int contaMovimentacao[MAX_MOVIMENTACOES];
char tipoMovimentacao[MAX_MOVIMENTACOES];
double valorMovimentacao[MAX_MOVIMENTACOES];

int quantidadeMovimentacoes = 0;

// Localiza uma conta pelo numero
int buscarConta(int numero) {
    for (int i = 0; i < quantidadeContas; i++) {
        if (numeroConta[i] == numero && contaAtiva[i]) {
            return i;
        }
    }

    return -1;
}

// Registra uma movimentacao no historico
void registrarMovimentacao(int numero, char tipo, double valor) {
    if (quantidadeMovimentacoes < MAX_MOVIMENTACOES) {
        contaMovimentacao[quantidadeMovimentacoes] = numero;
        tipoMovimentacao[quantidadeMovimentacoes] = tipo;
        valorMovimentacao[quantidadeMovimentacoes] = valor;

        quantidadeMovimentacoes++;
    }
}

// 1 - Cadastrar conta
void cadastrarConta() {
    if (quantidadeContas >= MAX_CONTAS) {
        cout << "\nLimite de contas atingido!\n";
        return;
    }

    int numero;

    cout << "\n===== CADASTRAR CONTA =====\n";

    cout << "Numero da conta: ";
    cin >> numero;

    if (numero <= 0 || buscarConta(numero) != -1) {
        cout << "Numero invalido ou ja cadastrado!\n";
        return;
    }

    numeroConta[quantidadeContas] = numero;

    cout << "Nome do cliente: ";
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    getline(cin, nomeCliente[quantidadeContas]);

    cout << "CPF: ";
    getline(cin, cpf[quantidadeContas]);

    cout << "Tipo de conta:\n";
    cout << "1 - Corrente\n";
    cout << "2 - Poupanca\n";
    cout << "Opcao: ";
    cin >> tipoConta[quantidadeContas];

    if (tipoConta[quantidadeContas] != 1 &&
        tipoConta[quantidadeContas] != 2) {
        cout << "Tipo de conta invalido!\n";
        return;
    }

    saldo[quantidadeContas] = 0.0;
    contaAtiva[quantidadeContas] = true;

    quantidadeContas++;

    cout << "\nConta cadastrada com sucesso!\n";
}

// 2 - Listar contas
void listarContas() {
    cout << "\n===== CONTAS CADASTRADAS =====\n";

    if (quantidadeContas == 0) {
        cout << "Nenhuma conta cadastrada.\n";
        return;
    }

    for (int i = 0; i < quantidadeContas; i++) {
        if (contaAtiva[i]) {
            cout << "\nNumero: " << numeroConta[i];
            cout << "\nCliente: " << nomeCliente[i];
            cout << "\nCPF: " << cpf[i];

            cout << "\nTipo: ";
            if (tipoConta[i] == 1) {
                cout << "Corrente";
            } else {
                cout << "Poupanca";
            }

            cout << "\nSaldo: R$ "
                 << saldo[i] << endl;
        }
    }
}

// 3 - Consultar conta
void consultarConta() {
    int numero;

    cout << "\n===== CONSULTAR CONTA =====\n";
    cout << "Informe o numero da conta: ";
    cin >> numero;

    int indice = buscarConta(numero);

    if (indice == -1) {
        cout << "Conta nao encontrada!\n";
        return;
    }

    cout << "\nNumero: " << numeroConta[indice];
    cout << "\nCliente: " << nomeCliente[indice];
    cout << "\nCPF: " << cpf[indice];

    cout << "\nTipo: ";
    if (tipoConta[indice] == 1) {
        cout << "Corrente";
    } else {
        cout << "Poupanca";
    }

    cout << "\nSaldo: R$ " << saldo[indice] << endl;
}

// 4 - Realizar deposito
void depositar() {
    int numero;
    double valor;

    cout << "\n===== DEPOSITO =====\n";
    cout << "Numero da conta: ";
    cin >> numero;

    int indice = buscarConta(numero);

    if (indice == -1) {
        cout << "Conta nao encontrada!\n";
        return;
    }

    if (quantidadeMovimentacoes >= MAX_MOVIMENTACOES) {
        cout << "Limite de movimentacoes atingido!\n";
        return;
    }

    cout << "Valor do deposito: R$ ";
    cin >> valor;

    if (valor <= 0) {
        cout << "Valor invalido!\n";
        return;
    }

    saldo[indice] += valor;

    registrarMovimentacao(numero, 'D', valor);

    cout << "Deposito realizado com sucesso!\n";
    cout << "Novo saldo: R$ " << saldo[indice] << endl;
}

// 5 - Realizar saque
void sacar() {
    int numero;
    double valor;

    cout << "\n===== SAQUE =====\n";
    cout << "Numero da conta: ";
    cin >> numero;

    int indice = buscarConta(numero);

    if (indice == -1) {
        cout << "Conta nao encontrada!\n";
        return;
    }

    if (quantidadeMovimentacoes >= MAX_MOVIMENTACOES) {
        cout << "Limite de movimentacoes atingido!\n";
        return;
    }

    cout << "Valor do saque: R$ ";
    cin >> valor;

    if (valor <= 0) {
        cout << "Valor invalido!\n";
        return;
    }

    if (saldo[indice] < valor) {
        cout << "Saldo insuficiente!\n";
        return;
    }

    saldo[indice] -= valor;

    registrarMovimentacao(numero, 'S', valor);

    cout << "Saque realizado com sucesso!\n";
    cout << "Novo saldo: R$ " << saldo[indice] << endl;
}

// 6 - Realizar transferencia
void transferir() {
    int origem, destino;
    double valor;

    cout << "\n===== TRANSFERENCIA =====\n";

    cout << "Conta de origem: ";
    cin >> origem;

    cout << "Conta de destino: ";
    cin >> destino;

    int indiceOrigem = buscarConta(origem);
    int indiceDestino = buscarConta(destino);

    if (indiceOrigem == -1 || indiceDestino == -1) {
        cout << "Uma ou ambas as contas nao foram encontradas!\n";
        return;
    }

    if (origem == destino) {
        cout << "Nao e possivel transferir para a mesma conta!\n";
        return;
    }

    if (quantidadeMovimentacoes + 2 > MAX_MOVIMENTACOES) {
        cout << "Espaco insuficiente no historico!\n";
        return;
    }

    cout << "Valor da transferencia: R$ ";
    cin >> valor;

    if (valor <= 0) {
        cout << "Valor invalido!\n";
        return;
    }

    if (saldo[indiceOrigem] < valor) {
        cout << "Saldo insuficiente!\n";
        return;
    }

    // Atualiza os saldos das duas contas
    saldo[indiceOrigem] -= valor;
    saldo[indiceDestino] += valor;

    // Registra a saida da conta de origem
    registrarMovimentacao(origem, 'S', valor);

    // Registra a entrada na conta de destino
    registrarMovimentacao(destino, 'D', valor);

    cout << "\nTransferencia realizada com sucesso!\n";

    cout << "Saldo da conta de origem: R$ "
         << saldo[indiceOrigem] << endl;

    cout << "Saldo da conta de destino: R$ "
         << saldo[indiceDestino] << endl;
}

// 7 - Exibir extrato
void exibirExtrato() {
    int numero;
    bool encontrou = false;

    cout << "\n===== EXTRATO BANCARIO =====\n";
    cout << "Numero da conta: ";
    cin >> numero;

    int indice = buscarConta(numero);

    if (indice == -1) {
        cout << "Conta nao encontrada!\n";
        return;
    }

    cout << "\nCliente: " << nomeCliente[indice];
    cout << "\nConta: " << numeroConta[indice];

    cout << "\n\nMovimentacoes:\n";

    for (int i = 0; i < quantidadeMovimentacoes; i++) {

        if (contaMovimentacao[i] == numero) {
            encontrou = true;

            if (tipoMovimentacao[i] == 'D') {
                cout << "Deposito: R$ ";
            }
            else if (tipoMovimentacao[i] == 'S') {
                cout << "Saque: R$ ";
            }

            cout << valorMovimentacao[i] << endl;
        }
    }

    if (!encontrou) {
        cout << "Nenhuma movimentacao registrada.\n";
    }

    cout << "\nSaldo atual: R$ "
         << saldo[indice] << endl;
}

// Funcao principal
int main() {

    int opcao;

    // Configura duas casas decimais para valores monetarios
    cout << fixed << setprecision(2);

    do {
        cout << "\n================================\n";
        cout << "       SISTEMA BANCARIO\n";
        cout << "================================\n";

        cout << "1 - Cadastrar conta\n";
        cout << "2 - Listar contas\n";
        cout << "3 - Consultar conta\n";
        cout << "4 - Realizar deposito\n";
        cout << "5 - Realizar saque\n";
        cout << "6 - Realizar transferencia\n";
        cout << "7 - Exibir extrato\n";
        cout << "0 - Sair\n";

        cout << "================================\n";
        cout << "Escolha uma opcao: ";
        cin >> opcao;

        switch (opcao) {

            case 1:
                cadastrarConta();
                break;

            case 2:
                listarContas();
                break;

            case 3:
                consultarConta();
                break;

            case 4:
                depositar();
                break;

            case 5:
                sacar();
                break;

            case 6:
                transferir();
                break;

            case 7:
                exibirExtrato();
                break;

            case 0:
                cout << "\nSistema encerrado. Obrigado!\n";
                break;

            default:
                cout << "\nOpcao invalida! Tente novamente.\n";
        }

    } while (opcao != 0);

    return 0;
}
