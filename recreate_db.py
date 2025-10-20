# Importar as entidades ANTES do connection_handler
# para que sejam registradas no Base.metadata
from src.models.sqlite.entities.people import PeopleTable  # noqa: F401
from src.models.sqlite.entities.pets import PetsTable  # noqa: F401

# Agora importar o connection_handler
from src.models.sqlite.settings.connection import db_connection_handler

if __name__ == "__main__":
    print("🔄 Conectando ao banco de dados...")
    db_connection_handler.connect_to_db()

    print("🗑️  Removendo tabelas antigas...")
    print("✨ Criando novas tabelas...")
    db_connection_handler.recreate_db()

    print("✅ Banco de dados recriado com sucesso!")
    print("📊 Tabelas criadas: people (com last_name), pets")
