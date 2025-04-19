# api_openai_class

## Descrição

Este projeto demonstra como interagir com a API da OpenAI usando Python. Ele inclui um ambiente virtual (`.venv`), um arquivo de dependências (`requirements.txt`) e o código principal em `src/main.py`.

## Instalação

1.  **Clone o repositório:**
    ```bash
    git clone <url-do-repositorio>
    cd api_openai_class
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    # Windows
    python -m venv .venv
    .\.venv\Scripts\activate

    # macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure sua chave da API OpenAI:**
    Crie um arquivo `.env` na raiz do projeto e adicione sua chave:
    ```
    OPENAI_API_KEY='sua_chave_api_aqui'
    ```
    *Certifique-se de adicionar `.env` ao seu arquivo `.gitignore`.*

## Uso

Execute o script principal:

```bash
python src/main.py
```

O script `src/main.py` contém exemplos de como usar a biblioteca da OpenAI para interagir com diferentes modelos e funcionalidades. Modifique o script conforme necessário para seus casos de uso.
