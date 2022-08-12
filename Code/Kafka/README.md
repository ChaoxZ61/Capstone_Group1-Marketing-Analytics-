# File Explained

**Creating_Topic.ipynb:** Databrick used to create a topic in Kafka (Only run once so it is not in the data pipeline in the factory).

**Creating_Producer.ipynb:** Databrick used to create a producer on the topic and send messages regarding state names and their respective abbreviatlions.

**Creating_Consumer.ipynb:** Databrick used to create a consumer that consumes the message produced by the procuder, store it in the data lake, and send it to the MS SQL Server.
