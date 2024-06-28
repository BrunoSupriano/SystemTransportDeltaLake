# Camada Bronze

Na camada Bronze, os dados brutos são coletados e armazenados. Isso inclui informações diretamente obtidas das tabelas principais. A integridade e a fidelidade dos dados são preservadas nesta etapa inicial.

### Mostrando todos os arquivos da camada landing-zone

```python 
display(dbutils.fs.ls(f"/mnt/{storageAccountName}/landing-zone"))
```

### Gerando um dataframe para cada arquivo a partir dos arquivos CSV gravado no container landing-zone do Azure Data Lake Storage

```python 
df_agendamentos = spark.read.option("infeschema", "true").option("header", "true").csv(f"/mnt/{storageAccountName}/landing-zone/Agendamentos.csv")
df_cargas = spark.read.option("infeschema", "true").option("header", "true").csv(f"/mnt/{storageAccountName}/landing-zone/Cargas.csv")
df_clientes = spark.read.option("infeschema", "true").option("header", "true").csv(f"/mnt/{storageAccountName}/landing-zone/Clientes.csv")
df_motoristas = spark.read.option("infeschema", "true").option("header", "true").csv(f"/mnt/{storageAccountName}/landing-zone/Motoristas.csv") 
df_rotas = spark.read.option("infeschema", "true").option("header", "true").csv(f"/mnt/{storageAccountName}/landing-zone/Rotas.csv")
df_veiculos = spark.read.option("infeschema", "true").option("header", "true").csv(f"/mnt/{storageAccountName}/landing-zone/Veiculos.csv")
```

### Adicionando metadados de data e hora de processamento e nome do arquivo de origem

```python 
from pyspark.sql.functions import current_timestamp, lit

df_agendamentos = df_agendamentos.withColumn("data_hora_bronze", current_timestamp()).withColumn("nome_arquivo", lit("Agendamentos.csv"))
df_cargas = df_cargas.withColumn("data_hora_bronze", current_timestamp()).withColumn("nome_arquivo", lit("Cargas.csv"))
df_clientes = df_clientes.withColumn("data_hora_bronze", current_timestamp()).withColumn("nome_arquivo", lit("Clientes.csv"))
df_motoristas = df_motoristas.withColumn("data_hora_bronze", current_timestamp()).withColumn("nome_arquivo", lit("Motoristas.csv"))
df_rotas = df_rotas.withColumn("data_hora_bronze", current_timestamp()).withColumn("nome_arquivo", lit("Rotas.csv"))
df_veiculos = df_veiculos.withColumn("data_hora_bronze", current_timestamp()).withColumn("nome_arquivo", lit("Veiculos.csv"))
```

### Salvando os dataframes em delta lake (formato de arquivo) no data lake (repositorio cloud)

```python 
df_agendamentos.write.format('delta').mode("overwrite").save(f"/mnt/{storageAccountName}/bronze/agendamentos")
df_cargas.write.format('delta').mode("overwrite").save(f"/mnt/{storageAccountName}/bronze/cargas")
df_clientes.write.format('delta').mode("overwrite").save(f"/mnt/{storageAccountName}/bronze/clientes")
df_motoristas.write.format('delta').mode("overwrite").save(f"/mnt/{storageAccountName}/bronze/motoristas")
df_rotas.write.format('delta').mode("overwrite").save(f"/mnt/{storageAccountName}/bronze/rotas")
df_veiculos.write.format('delta').mode("overwrite").save(f"/mnt/{storageAccountName}/bronze/veiculos")
```
### Verificando os dados gravados em delta na camada bronze

```python
display(dbutils.fs.ls(f"/mnt/{storageAccountName}/bronze/"))
```

### Lendo um exemplo de um delta lake para validar a existencia dos dados e das colunas do metadados

```python 
spark.read.format('delta').load(f'/mnt/{storageAccountName}/bronze/veiculos').limit(10).display()
```



