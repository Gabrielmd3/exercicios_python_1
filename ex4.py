class CadastroUsuarios:
    def __init__(self):
        self.usuarios = {}

    def cadastrar_usuario(self, nome, email, telefone):
        if email not in self.usuarios:
            self.usuarios[email] = {'nome': nome, 'email': email, 'telefone': telefone}
            print("Usuário cadastrado com sucesso!")
        else:
            print("O email já está cadastrado.")

    def listar_usuarios(self, email_pesquisa=None):
        if self.usuarios:
            if email_pesquisa:
                # Se um email de pesquisa foi fornecido, verifica se o usuário existe e exibe suas informações
                if email_pesquisa in self.usuarios:
                    dados = self.usuarios[email_pesquisa]
                    print("\nInformações do Usuário:")
                    print(f"Nome: {dados['nome']}")
                    print(f"Email: {dados['email']}")
                    print(f"Telefone: {dados['telefone']}\n")
                else:
                    print("Usuário não encontrado.")
            else:
                # Se nenhum email de pesquisa foi fornecido, lista todos os usuários
                print("\n### Lista de Usuários ###")
                for email, dados in self.usuarios.items():
                    print(f"Nome: {dados['nome']}")
                    print(f"Email: {dados['email']}")
                    print(f"Telefone: {dados['telefone']}\n")
        else:
            print("Nenhum usuário cadastrado.")

def menu():
    cadastro = CadastroUsuarios()
    while True:
        print("\n### Menu ###")
        print("1. Cadastrar Usuário")
        print("2. Listar Usuários")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome: ")
            email = input("Digite o email: ")
            telefone = input("Digite o telefone: ")
            cadastro.cadastrar_usuario(nome, email, telefone)
        elif opcao == '2':
            email_pesquisa = input("Digite o email do usuário a ser pesquisado (ou pressione Enter para listar todos): ")
            cadastro.listar_usuarios(email_pesquisa if email_pesquisa.strip() else None)
        elif opcao == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
