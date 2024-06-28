---
hide:
  - navigation
  #- toc # table of contents - menu da direita
---




# Configuração do Ambiente

##  Databricks Community Edition

1. Crie uma conta no [Databricks Community Edition](https://community.cloud.databricks.com/).
2. Configure um novo workspace e cluster.

 Integração com Azure Data Lake Storage

1. Configure a conta do Azure e crie um Data Lake Storage.
2. Integre o Databricks com o Azure Data Lake Storage.

##  Desenvolvimento

Para detalhes sobre os exemplos de código do pipeline, consulte a página [Pipeline de Dados](pipeline.md).

 Criação de Dashboards com Power BI

1. Conecte o Power BI ao Azure Data Lake Storage.
2. Crie relatórios e dashboards interativos.

## Controle de Versão com Git

- Inicialização de um repositório Git:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    ```

- Exemplo de workflow Git:
    ```bash
    git branch feature-branch
    git checkout feature-branch
    git add .
    git commit -m "Add new feature"
    git checkout main
    git merge feature-branch
    ```


