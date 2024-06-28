# Arquitetura

![Arquitetura](https://github.com/jlsilva01/projeto-ed-satc/assets/484662/541de6ab-03fa-49b3-a29f-dec8857360c1)

## Estrutura da Pipeline

A pipeline de dados foi organizada em três camadas principais: Bronze, Silver e Gold. Cada camada desempenha um papel específico na preparação e transformação dos dados.

### Conectando Azure ADLS Gen2 no Databricks

#### Definindo storage account e sas key

```python
storageAccountName = "sua_storage_account"
sasToken = dbutils.secrets.get(scope="sas-token", key="sas-token")
```

#### Definindo uma função para montar um ADLS com um ponto de montagem com ADLS SAS

```python
def mount_adls(blobContainerName):
    try:
      dbutils.fs.mount(
        source = "wasbs://{}@{}.blob.core.windows.net".format(blobContainerName, storageAccountName),
        mount_point = f"/mnt/{storageAccountName}/{blobContainerName}",
        extra_configs = {'fs.azure.sas.' + blobContainerName + '.' + storageAccountName + '.blob.core.windows.net': sasToken}
      )
      print("OK!")
    except Exception as e:
      print("Falha", e)
```

#### Montando todos os containers

```python 
mount_adls('landing-zone')
mount_adls('bronze')
mount_adls('silver')
mount_adls('gold')
```

#### Mostrando os pontos de montagem no cluster Databricks

```python
display(dbutils.fs.mounts())
```