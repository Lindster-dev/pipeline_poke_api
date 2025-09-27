# Análise de Dados Pokémon com PokeAPI

![Distribuição de Pokémon por Tipo](distribuicao_por_tipo_pokemon.png)

**Projeto Python que coleta, transforma e analisa dados de Pokémon da [PokeAPI](https://pokeapi.co/), gerando relatórios CSV, gráficos e logs.**

---

## 1. Descrição do Projeto

Este projeto demonstra um fluxo completo de **ETL (Extração, Transformação, Carga)** com dados de Pokémon. Ele gera relatórios em CSV e gráficos que mostram estatísticas e distribuição por tipo de Pokémon. Também implementa **logging** para monitorar a execução.

---

## 2. Funcionalidades

* **Extração de Dados**: Busca informações detalhadas de Pokémon na PokeAPI.
* **Transformação de Dados**:

  * Identifica os 5 Pokémon com maior experiência base.
  * Categoriza Pokémon por experiência (Fraco, Médio, Forte).
  * Calcula média de HP, Ataque e Defesa por tipo.
  * Conta a quantidade de Pokémon por tipo.
* **Geração de Relatórios**: Salva dados em arquivos CSV.
* **Visualização de Dados**: Cria gráficos usando `matplotlib` e `seaborn`.
* **Logging**: Registra eventos, avisos e erros durante a execução.

---

## 3. Estrutura do Projeto

```
. # Diretório raiz
├── main.py
├── requirements.txt
├── Dockerfile
├── src/
│   ├── __init__.py
│   ├── analyze.py
│   ├── extract.py
│   └── transform.py
├── data/
│   └── reports/
│       ├── relatorio_pokemon_top5.csv
│       ├── relatorio_pokemon_stats.csv
│       └── distribuicao_por_tipo_pokemon.png
├── logs/                # Logs gerados durante execução
```

---

## 4. Tecnologias Utilizadas

* Python 3.x
* `requests`
* `pandas`
* `matplotlib`
* `seaborn`
* `logging`

---

## 5. Logging

O projeto cria logs detalhados de execução no diretório `logs/`:

* **Formato do log**:

  ```
  2025-09-27 14:00:00 [INFO] main: Iniciando execução do fluxo ETL
  2025-09-27 14:00:05 [WARNING] extract: Pokémon X não encontrado
  2025-09-27 14:00:10 [ERROR] transform: Falha ao calcular estatística
  ```

* **Onde são gerados**:

  * Localmente: dentro da pasta `logs/` do projeto.
  * Docker: montando o volume `-v $(pwd)/logs:/app/logs`, os logs são persistidos no host.

* **Vantagem**: Permite monitorar erros, avisos e progresso sem precisar abrir o terminal.

---

## 6. Como Executar

### 6.1. Localmente

1. Clone o repositório e acesse o diretório:

```bash
git clone <https://github.com/Lindster-dev/pipeline_poke_api.git>
cd <pipeline_poke_api>
```

2. Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows
```

3. Instale dependências:

```bash
pip install -r requirements.txt
```

4. Execute o projeto:

```bash
python main.py
```

* Os relatórios e gráficos serão gerados em `data/reports/`.
* Os logs serão criados em `logs/`.

---

### 6.2. Usando Docker

1. **Build da imagem Docker**:

```bash
docker build -t pokemon-etl .
```

2. **Executar o container**:

```bash
docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/logs:/app/logs pokemon-etl
```

* Os volumes `-v` garantem que **logs e relatórios fiquem no host**, mesmo após o container ser removido.
* O container executa `main.py` automaticamente.

---

## 7. Resultados Gerados

### `relatorio_pokemon_top5.csv`

Top 5 Pokémon por experiência base.

### `relatorio_pokemon_stats.csv`

Estatísticas médias (HP, Ataque, Defesa) por tipo.

### `distribuicao_por_tipo_pokemon.png`

Gráfico de barras com distribuição de Pokémon por tipo.

### Logs

* Arquivos de log detalhados por execução em `logs/`.


