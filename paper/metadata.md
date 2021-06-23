Tue Jun 22 13:08:11 PDT 2021

Do we want to use CSVW for the metadata, or do we want to use something else?
I'm thinking about the [metadata from AWS Athena](https://docs.aws.amazon.com/athena/latest/ug/datastores-hive-cli.html#datastores-hive-cli-showing-details-of-a-table).

First, we should use an existing standard.
What do we want out of a standard?

1. Simplicity. That's the premise of CTF.
2. Support. The more people already use it, the more we can borrow from and integrate with existing technologies.
3. Big Data Use Case. Our use case is analyzing and processing big data, and not web development. By following a standard that was developed for a use case that's closest to ours, we will probably have an easier time.
4. Open Source.


This blog post, [Metadata Management: Hive Metastore vs AWS Glue
](https://lakefs.io/metadata-management-hive-metastore-vs-aws-glue/) nicely explains the difference between Hive metastore and AWS Glue.

Our purpose is to demonstrate the efficiency of this data format.
For this, we need to actually do something with a large data set.
I already have Athena set up, and it would take me time to set up Hive.
So Athena is going to be faster.

A single JSON file is easier and lighter weight than a full database with a managed service, like Hive has.


## AWS Athena metadata

The AWS Athena use case is pretty similar to ours.
Let's see how their metadata looks.

```
aws athena get-table-metadata --catalog-name AwsDataCatalog --database-name covid19-homework-crawler --table-name covid
```

Here it is for the large `covid` table.

```json
{
    "TableMetadata": {
        "Name": "covid",
        "CreateTime": "2021-04-27T21:32:53-07:00",
        "LastAccessTime": "2021-04-27T21:32:53-07:00",
        "TableType": "EXTERNAL_TABLE",
        "Columns": [
            {
                "Name": "data_source",
                "Type": "string"
            },
            {
                "Name": "signal",
                "Type": "string"
            },
            {
                "Name": "geo_type",
                "Type": "string"
            },
            {
                "Name": "time_value",
                "Type": "int"
            },
            {
                "Name": "geo_value",
                "Type": "string"
            },
            {
                "Name": "direction",
                "Type": "int"
            },
            {
                "Name": "value",
                "Type": "double"
            },
            {
                "Name": "stderr",
                "Type": "double"
            },
            {
                "Name": "sample_size",
                "Type": "double"
            }
        ],
        "PartitionKeys": [],
        "Parameters": {
            "CrawlerSchemaDeserializerVersion": "1.0",
            "CrawlerSchemaSerializerVersion": "1.0",
            "UPDATED_BY_CRAWLER": "crawler1",
            "averageRecordSize": "14",
            "classification": "parquet",
            "compressionType": "none",
            "inputformat": "org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat",
            "location": "s3://stat196k-data-examples/covid_db/covid/",
            "objectCount": "21",
            "outputformat": "org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat",
            "recordCount": "136060398",
            "serde.param.serialization.format": "1",
            "serde.serialization.lib": "org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe",
            "sizeKey": "1102566068",
            "typeOfData": "file"
        }
    }
}
```


The `columns` look just as we would hope, with the names and data types.
One issue is that the [Athena docs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-table-metadata.html) don't allow other entries in the columns; the only allowed keys are Name, Type, and Comment.
We can get around this by saying that ctf metadata extends the information in AWS glue, and writing a crawler that recognizes ctf metadata.
The same kind of thing happens in Parquet, and other binary data formats.
They store all their metadata in the binary files themselves, and some metadata gets duplicated in AWS glue, no big deal.

In conclusion, the CTF metadata doesn't need to follow the AWS Glue format exactly, but I think that following Glue where possible will make it easier when we later write the crawler and demonstrate how to use this data format with AWS.
Maybe that's a lofty goal!


## Advantages of CSVW

We already have a working implementation in Python based on CSVW.

CSVW seems carefully and thoughtfully designed for a wide range of use cases, and there are mechanisms to extend it.
The documentation is extremely thorough and precise.
In contrast, AWS glue appears to do the minimum that's necessary to support AWS Athena.
The documentation is sparse, and the actual format could change at any time.
Not that AWS would do that- it would break a bunch of stuff.

CSVW seems like the right long term solution.
We can still implement the crawler from CSVW, and generate the Glue metadata.
It may be more work, but it will also support the use case of reading regular CSV files that are described with CSVW metadata.
As an academic, I'm not in huge hurry to ship working software.
I'd rather start with the right technologies in the first place.

Side note-
It would be worthwhile to develop software that reads and validates CSV files based on CSVW.
CTF could depend on it.
