## 1. Visão Geral do Projeto

Este projeto implementa um fluxo completo de **ETL (Extração, Transformação e Carga)** para analisar dados de Pokémon obtidos da [PokeAPI](https://pokeapi.co/). O sistema foi projetado para ser modular, robusto e de fácil execução, utilizando tecnologias como Python, Docker, Pandas e Matplotlib para coletar, processar e visualizar informações sobre os Pokémon.

O resultado final do processo são relatórios em formato CSV e visualizações gráficas que fornecem insights sobre os atributos dos Pokémon, como suas estatísticas de combate, distribuição por tipo e ranking de experiência.

## 2. Arquitetura e Estrutura

O projeto é organizado em módulos distintos, cada um com uma responsabilidade clara, seguindo as melhores práticas de desenvolvimento de software para garantir a manutenibilidade e escalabilidade do código.

```
. # Diretório raiz
├── main.py
├── requirements.txt
├── Dockerfile
├── extract.py
├── transform.py
├── analyze.py
├── data/
│   └── reports/
│       ├── relatorio_pokemon_top5.csv
│       ├── relatorio_pokemon_stats.csv
│       └── distribuicao_por_tipo_pokemon.png
├── logs/
│   └── pokemon_report_YYYY-MM-DD.log
```

### Componentes Principais

| Módulo | Descrição |
| :--- | :--- |
| `main.py` | Ponto de entrada da aplicação. Orquestra a execução dos módulos de extração, transformação e análise. |
| `extract.py` | Responsável por se conectar à PokeAPI, extrair os dados brutos dos Pokémon e estruturá-los em um formato inicial. |
| `transform.py` | Contém a lógica para transformar os dados extraídos, calculando estatísticas, categorizando Pokémon e preparando os dados para análise. |
| `analyze.py` | Gera os relatórios finais em CSV e os gráficos de visualização de dados. |
| `Dockerfile` | Define o ambiente de contêiner para a aplicação, permitindo que ela seja executada de forma isolada e consistente em qualquer ambiente que suporte Docker. |
| `requirements.txt` | Lista todas as dependências Python do projeto. |

## 3. Funcionalidades Detalhadas

### 3.1. Extração de Dados (`extract.py`)

O módulo de extração é a primeira etapa do fluxo ETL. Ele se comunica com a PokeAPI para buscar uma lista de Pokémon e, em seguida, itera sobre essa lista para obter os detalhes de cada um.

- **`get_pokemon_list(limit, offset)`**: Obtém uma lista paginada de Pokémon.
- **`get_pokemon_details(pokemon_url)`**: Busca os dados detalhados de um Pokémon específico a partir de sua URL.
- **`parse_pokemon(details_pokemon)`**: Extrai e formata as informações mais relevantes de cada Pokémon, como ID, nome, experiência base, tipos e estatísticas (HP, Ataque, Defesa).
- **`process_extractor(limit, offset)`**: Orquestra todo o processo de extração, consolidando os dados de múltiplos Pokémon em um único DataFrame do Pandas.

### 3.2. Transformação de Dados (`transform.py`)

Após a extração, os dados brutos são processados pelo módulo de transformação para gerar informações mais elaboradas e insights.

- **`add_category(df)`**: Adiciona uma coluna "Categoria" ao DataFrame, classificando os Pokémon como "Fraco", "Médio" ou "Forte" com base em sua experiência base.
- **`stats_by_type(df)`**: Calcula a média de HP, Ataque e Defesa para cada tipo de Pokémon.
- **`pokemon_count_by_type(df)`**: Conta a quantidade de Pokémon por tipo.
- **`top5_by_experience(df)`**: Identifica os 5 Pokémon com a maior experiência base.
- **`process_transform_data_pokemon(df)`**: Executa todas as transformações em sequência, retornando múltiplos DataFrames com os resultados.

### 3.3. Análise e Geração de Relatórios (`analyze.py`)

Na etapa final, o módulo de análise utiliza os dados transformados para gerar os artefatos de saída do projeto.

- **`generate_top5_pokemon_csv(df)`**: Cria um arquivo CSV (`relatorio_pokemon_top5.csv`) com os 5 Pokémon de maior experiência.
- **`generate_stats_csv(df)`**: Gera um arquivo CSV (`relatorio_pokemon_stats.csv`) com as estatísticas médias por tipo.
- **`plot_distribution_by_type_pokemon(df)`**: Cria um gráfico de barras (`distribuicao_por_tipo_pokemon.png`) que mostra a distribuição de Pokémon por tipo, permitindo uma visualização clara de quais tipos são mais comuns.
- **`generate_report(...)`**: Orquestra a geração de todos os relatórios e gráficos.

## 4. Como Executar o Projeto

Existem duas maneiras de executar o projeto: localmente, utilizando um ambiente virtual Python, ou através de um contêiner Docker.

### 4.1. Execução Local

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_DIRETORIO>
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    ```bash
    python main.py
    ```

### 4.2. Execução com Docker

A utilização de Docker simplifica a execução, pois encapsula todas as dependências e configurações em um ambiente isolado.

1.  **Construa a imagem Docker:**
    ```bash
    docker build -t pokemon-etl .
    ```

2.  **Execute o contêiner:**
    ```bash
    docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/logs:/app/logs pokemon-etl
    ```
    - O uso de volumes (`-v`) garante que os relatórios e logs gerados dentro do contêiner sejam persistidos no diretório local do seu computador.

## 5. Logging e Monitoramento

O projeto implementa um sistema de logging robusto para registrar todos os eventos importantes, avisos e erros durante a execução. Os logs são salvos em arquivos no diretório `logs/`, com um novo arquivo sendo criado para cada dia de execução (`pokemon_report_YYYY-MM-DD.log`).

Isso facilita o monitoramento e a depuração, permitindo que o usuário acompanhe o progresso da execução e identifique rapidamente qualquer problema que possa ocorrer.

## 6. Conclusão

Este projeto serve como um exemplo prático e completo de um pipeline de dados, demonstrando desde a coleta de dados de uma API externa até a geração de análises e visualizações. A sua arquitetura modular e o uso de tecnologias modernas como Docker o tornam uma base sólida para projetos de análise de dados mais complexos.



Um novo arquivo é criado a cada execução diária, permitindo monitoramento e depuração eficientes.

6. Conclusão

Este projeto demonstra um pipeline de dados completo, desde a coleta de dados de uma API externa até a geração de análises e visualizações.

Sua arquitetura modular, uso de boas práticas em Python e integração com Docker tornam o projeto uma base sólida para análises de dados mais complexas ou projetos similares de ETL.