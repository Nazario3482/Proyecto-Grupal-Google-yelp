from google.cloud import bigquery
from google.cloud import storage
import os

def merge_csv_to_bigquery(data, context):
    """Fusionar un archivo CSV recién subido a Cloud Storage con una tabla existente en BigQuery."""
    # Obtener información sobre el archivo cargado
    bucket_name = data['bucket']
    file_name = data['name']
    print(f'Archivo subido: {file_name}')

    # Configurar el cliente de Cloud Storage
    storage_client = storage.Client()

    # Obtener el bucket y el blob
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)

    # Descargar el archivo CSV a un directorio temporal
    temp_file_path = f'/tmp/{file_name}'
    blob.download_to_filename(temp_file_path)
    print(f'Archivo descargado a: {temp_file_path}')

    # Configurar el cliente de BigQuery
    bq_client = bigquery.Client()

    # Configurar el dataset y la tabla en BigQuery
    dataset_id = 'henry-416317.carga_incremental'
    temp_table_id = 'temp_table_business'  # Nombre de la tabla temporal
    main_table_id = 'business'  # Nombre de la tabla principal

    # Cargar el archivo CSV en una tabla temporal en BigQuery
    job_config = bigquery.LoadJobConfig(
        schema=[
          bigquery.SchemaField("name", "STRING"),
          bigquery.SchemaField("business_id", "STRING"),
          bigquery.SchemaField("latitude", "FLOAT"),
          bigquery.SchemaField("longitude", "FLOAT"),
          bigquery.SchemaField("category", "STRING"),
          bigquery.SchemaField("avg_rating", "FLOAT"),
          bigquery.SchemaField("num_of_reviews", "INTEGER"),
        ],
        skip_leading_rows=1,
        source_format=bigquery.SourceFormat.CSV
    )

    with open(temp_file_path, "rb") as source_file:
        job = bq_client.load_table_from_file(
            source_file,
            dataset_id + '.' + temp_table_id,
            job_config=job_config
        )

    job.result()  # Espera a que termine la carga
    print(f'Carga completada en BigQuery: {dataset_id}.{temp_table_id}')

    # Realizar la fusión de datos utilizando una consulta SQL
    merge_query = f"""
        MERGE INTO {dataset_id}.{main_table_id} AS main
        USING {dataset_id}.{temp_table_id} AS temp
        ON main.business_id = temp.business_id AND main.latitude = temp.latitude
        WHEN NOT MATCHED THEN
            INSERT (name, business_id, latitude, longitude, category, avg_rating, num_of_reviews)
            VALUES (temp.name, temp.business_id, temp.latitude, temp.longitude, temp.category, temp.avg_rating, temp.num_of_reviews)
    """


    query_job = bq_client.query(merge_query)
    query_job.result()  # Espera a que la consulta se complete

    print(f'Fusión completada en BigQuery: {dataset_id}.{main_table_id}')

    # Eliminar el archivo temporal
    os.remove(temp_file_path)
    print(f'Archivo temporal eliminado: {temp_file_path}')

    print('Proceso completado exitosamente.')
