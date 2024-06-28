# Sistema de Transportes (DeltaLake)

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Este projeto visa construir um Data Lake utilizando uma arquitetura de camadas, ingestão e transformação de dados, e visualização de dados em um dashboard.

## Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **[Implantação](#-implanta%C3%A7%C3%A3o)** para saber como implantar o projeto.

## Desenho de Arquitetura

Coloqui uma imagem do seu projeto, como no exemplo abaixo:

![image](https://github.com/jlsilva01/projeto-ed-satc/assets/484662/541de6ab-03fa-49b3-a29f-dec8857360c1)

## Pré-requisitos

De que coisas você precisa para instalar o software e como instalá-lo?

- **Python 3.8+** 
- **Git**: [Instalar Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Instalação

Uma série de exemplos passo-a-passo que informam o que você deve executar para ter um ambiente de desenvolvimento em execução.

### Clonando o Repositório

```bash
git clone https://github.com/brunosupriano/SystemTransportDeltaLake.git
```

```bash
cd SystemTransportDeltaLake
```

### Configurando o Ambiente Virtual

#### Com pip 
```bash
python3 -m venv env
source env\Scripts\activate # No linux use `source env/bin/activate` 
pip install -r requirements.txt
```
#### Com poetry

```bash
poetry init
poetry add mkdocs mkdocs-material mkdocs-material-extensions
poetry shell
```

### Rodando o mkdocs

```bash
mkdocs serve
```

---

## Ferramentas Utilizadas

#### [Faker](https://faker.readthedocs.io/)

Biblioteca Python utilizada para gerar dados falsos realistas, como nomes, endereços, datas e mais. Essencial para criar a massa de dados necessária para o ambiente relacional.

#### [Docker](https://www.docker.com/)

Plataforma de contêineres que permite criar, implantar e executar aplicativos de maneira isolada. Usada para configurar ambientes locais consistentes, incluindo o armazenamento de objetos para o Data Lake.

#### [Delta Lake](https://delta.io/)

Armazenamento de dados em formato de tabela otimizado para grandes volumes de dados e processamento transacional em escala. Usado para armazenar dados nas camadas Bronze, Silver e Gold.

#### [Apache Spark](https://spark.apache.org/)

Motor de processamento de dados distribuído que permite a execução de tarefas de transformação e análise em grandes volumes de dados. Utilizado para transformação de dados com PySpark.

#### [Power BI](https://powerbi.microsoft.com/)

Serviço de análise de negócios que fornece visualizações interativas e recursos de inteligência de negócios. Utilizado para criar o dashboard que consome dados do modelo dimensional na camada Gold.

#### [GitHub](https://github.com/)

Plataforma de hospedagem de código-fonte com controle de versão usando Git. Utilizada para colaboração, versionamento de código, gerenciamento de issues, e publicação da documentação do projeto.

#### [MkDocs](https://www.mkdocs.org/)

Gerador de sites estáticos que converte arquivos markdown em uma documentação bem estruturada. Utilizado para documentar o projeto de forma clara e organizada.

---

## Colaboração

<!-- Por favor, leia o [COLABORACAO](https://gist.github.com/usuario/colaboracao.md) para obter detalhes sobre o nosso código de conduta e o processo para nos enviar pedidos de solicitação. -->

Se desejar publicar suas modificações em um repositório remoto no GitHub, siga estes passos:

1. Crie um novo repositório vazio no GitHub.
2. No terminal, navegue até o diretório raiz do projeto.
3. Execute os seguintes comandos:

```bash
git remote set-url origin https://github.com/seu-usuario/nome-do-novo-repositorio.git
git add .
git commit -m "Adicionar minhas modificações"
git push -u origin master
```

Isso configurará o repositório remoto e enviará suas modificações para lá.

## Versão

Fale sobre a versão e o controle de versões para o projeto. Para as versões disponíveis, observe as [tags neste repositório](https://github.com/suas/tags/do/projeto). 

## Autores

Mencione todos aqueles que ajudaram a levantar o projeto desde o seu início

- **Henrique Forgiarini** - *Leitura de dados e geração de massa de dados* - [Perfil GitHub](https://github.com/HenriqueSilva29)
- **Bruno Supriano** - *Ingestão de dados no Data Lake* - [Perfil GitHub](https://github.com/BrunoSupriano)
- **Renato Ribas** - *Configuração do Data Lake* - [Perfil GitHub](https://github.com/RenatoRibas)
- **Tiago Salles** - *Gravação de dados no Data Lake* - [Perfil GitHub](https://github.com/TiagoS4)
- **João Pedro Cardoso** - *Transformação de dados com Apache Spark* - [Perfil GitHub](https://github.com/jpdarabas)
- **Diego Hahn** - *Orquestração das tarefas* - [Perfil GitHub](https://github.com/DiegoHahn)
- **Jhayne Henemam** - *Desenvolvimento do dashboard* - [Perfil GitHub](https://github.com/JhayneK)
- **Keniel  Alves** - *GitHub e documentação* - [Perfil GitHub](https://github.com/kenielnunes)

Você também pode ver a lista de todos os [colaboradores](https://github.com/BrunoSupriano/SystemTransportDeltaLake/Colaborators) que participaram deste projeto.

## Licença

Este projeto está sob a licença (sua licença) - veja o arquivo [LICENSE](https://github.com/jlsilva01/projeto-ed-satc/blob/main/LICENSE) para detalhes.

## Referências

Cite aqui todas as referências utilizadas neste projeto, pode ser outros repositórios, livros, artigos de internet etc.

`referencias`
