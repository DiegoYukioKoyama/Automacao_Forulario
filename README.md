# Automacao_Forulario

Este repositório contém um script em Python que automatiza a transferência de dados de um arquivo `.csv` para um formulário web. O script foi desenvolvido para treinar a automação de tarefas repetitivas (RPA - Robotic Process Automation) e interação com interfaces gráficas.

## 🛠️ Tecnologias Utilizadas
* **Python 3.13**
* **PyAutoGUI** (para simulação de cliques e digitação)
* **CSV** (para leitura e extração dos dados)

## ⚙️ Como o Script Funciona
1. O código abre um arquivo `.html` contendo um formulário web que recebe os dados de uma pessoa (Nome, CPF e Telefone).
2. O código abre um arquivo `.csv` contendo dados de usuários fictícios (Nome, CPF e Telefone).
3. Entra em um loop (linha por linha do arquivo).
4. Utiliza o `PyAutoGUI` para mover o mouse até os campos do formulário web.
5. Digita as informações e clica em "Enviar".
6. Repete o processo até que todas as linhas do arquivo `.csv` sejam cadastradas.

## ⚠️ Aviso Importante (Resolução de Tela)
O `PyAutoGUI` funciona mapeando as coordenadas exatas da sua tela. Os cliques neste código foram configurados para a resolução do meu monitor. Para rodar este script na sua máquina, você precisará recalibrar as posições (X, Y) dos campos do seu formulário utilizando o comando `pyautogui.position()`.

## 🚀 Como Executar
1. Clone este repositório:
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
