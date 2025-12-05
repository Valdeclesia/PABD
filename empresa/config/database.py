import os

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    load_dotenv = None

try:
    from supabase import create_client
except ModuleNotFoundError:
    create_client = None


class SupabaseConnection:
    def __init__(self):
        if load_dotenv is None:
            raise ModuleNotFoundError(
                "Pacote 'python-dotenv' não está instalado. Rode: `pip install python-dotenv`"
            )

        if create_client is None:
            raise ModuleNotFoundError(
                "Pacote 'supabase' não está instalado. Rode: `pip install supabase`"
            )

        load_dotenv()

        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")

        if not url or not key:
            raise ValueError("Erro: SUPABASE_URL ou SUPABASE_KEY não definidos no .env")

        self.client = create_client(url, key)