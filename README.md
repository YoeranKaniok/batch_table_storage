Async Microsoft Azure CosmosDB Table SDK for Python with batching functionality
=========================================================================

This project provides a asynchronous wrapper for the Azure cosmosdb TableService.
The wrapper lets you insert/merge/replace/delete lists of entities using `aioify`.
You can give it any number of PartitionKeys, they will be processed in different batches.
 
For documentation on the base package please see `azure-cosmosdb-table` package. (https://pypi.org/project/azure-cosmosdb-table/)

Features
========

-  Automatically split lists of entities into batches based on PartitionKey
-  Automatically chunk entities into sub-lists for correct batch sizes
-  Batch Insert Entities async
-  Batch Update Entities async
-  Batch Merge Entities async
-  Batch Delete Entities async
-  Batch Insert or Replace Entities async
-  Batch Insert or Merge Entities async
   
Getting Started
===============

To install via the Python Package Index (PyPI), type:


    pip install batch-table-storage
    
Minimum Requirements
--------------------

-  azure-cosmosdb-table==1.0.6


Code Sample
-----------

Import the wrapper class

    from batch_table_service import BatchTableService

Instantiate the service
 
    service = BatchTableService(account_name='storageAccount', account_key='x')
  
Create some entities
  
    entities = [
        {'PartitionKey': 'person', 'RowKey': '1', 'name': 'John'},
        {'PartitionKey': 'pet', 'RowKey': '1', 'name': 'Cat'}
    ]

Import asyncio:
   
    import asyncio

Create and commit the batches async:
   
    asyncio.run(
        service.batch_insert_entities(table_name='tableA', entities=entities)
    )


Learn More
==========
Microsoft Azure CosmosDB Table SDK for Python: https://pypi.org/project/azure-cosmosdb-table/