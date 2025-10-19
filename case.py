class AlgumaCoisa:
    def __enter__(self):
        print("Estou entrando")

    def __exit__(self, exc_type, exc_val, exec_tb):
        print(exc_type)
        print(exc_val)
        print(exec_tb)
        print("Estou Saindo")


with AlgumaCoisa() as something:
    # raise Exception("Erro ocorreu")
    print("Estou no meio")
