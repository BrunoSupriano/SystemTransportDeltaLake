---
hide:
  - h1
  #- toc # table of contents - menu da direita
---

Um pipeline de dados é um conjunto de processos que extrai dados de várias fontes, transforma esses dados para um formato adequado e os carrega em um sistema de armazenamento, como um banco de dados ou um data warehouse. Os principais componentes de um pipeline de dados são:

1. **Extração (Extract):** Coleta dados de fontes diversas, como bancos de dados, APIs, arquivos CSV, logs, etc.
2. **Transformação (Transform):** Converte os dados brutos em um formato mais adequado para análise. Isso pode incluir limpeza de dados, agregação, normalização, filtragem, enriquecimento, etc.
3. **Carregamento (Load):** Carrega os dados transformados para o sistema de destino, como um data warehouse, data lake, ou banco de dados analítico.

## Arquitetura Medalhão

A arquitetura medalhão é um padrão de design utilizado em data lakes para organizar e gerenciar dados em diferentes camadas de qualidade e maturidade. Ela geralmente é composta por três camadas principais:

??? "Bronze"
    A camada bronze é onde os dados brutos são armazenados. Esses dados são ingeridos de várias fontes sem muitas transformações, mantendo sua forma original. A ideia é preservar a integridade e a granularidade dos dados originais para que possam ser revisitados, se necessário.

    ```json
    {
        "data_source": "API",
        "data_type": "raw",
        "timestamp": "2024-06-28T12:00:00Z"
    }
    ```

??? "Silver"
    Na camada silver, os dados da camada bronze são transformados, limpos e estruturados. Esta camada inclui processos de deduplicação, formatação, limpeza de dados, e outras transformações necessárias para tornar os dados mais úteis e consistentes. A camada silver é frequentemente usada para análises exploratórias e geração de relatórios.

    ```json
    {
        "data_source": "API",
        "data_type": "cleaned",
        "timestamp": "2024-06-28T12:00:00Z"
    }
    ```

??? "Gold"
    
    A camada gold contém dados altamente refinados e otimizados para consumo analítico. Nesta camada, os dados são agregados, enriquecidos e organizados de forma a atender necessidades específicas de análise, como dashboards, relatórios detalhados e modelos de machine learning. A camada gold é usada para fornecer insights de negócios e suporte a decisões estratégicas.

    ```json
    {
        "data_source": "API",
        "data_type": "aggregated",
        "timestamp": "2024-06-28T12:00:00Z",
        "insights": {
            "key_metric": 1234.56
        }
    }
    ```

## Vantagens da Arquitetura Medalhão

- :key: **Organização:** Ajuda a estruturar e organizar os dados em um data lake, facilitando a gestão e o acesso.
- :chart_with_upwards_trend: **Flexibilidade:** Permite que dados brutos sejam preservados, enquanto versões mais refinadas dos dados podem ser criadas conforme necessário.
- :heavy_check_mark: **Qualidade dos Dados:** Melhora a qualidade dos dados ao aplicar processos de limpeza e transformação em etapas distintas.
- :arrows_counterclockwise: **Escalabilidade:** Facilita a escalabilidade, uma vez que diferentes camadas podem ser geridas e escaladas independentemente.

Esses conceitos são fundamentais para o gerenciamento eficaz de dados em um ambiente de big data, permitindo que as organizações extraiam valor dos dados de forma eficiente e estruturada.