import boto3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

primary_db_uri = 'postgresql://user:password@primary-db-host:port/primary_db_name'
primary_engine = create_engine(primary_db_uri)

session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='YOUR_REGION'
)

client = session.client('rds')

response = client.create_db_instance_read_replica(
    DBInstanceIdentifier='my-read-replica',
    SourceDBInstanceIdentifier='my-primary-db',
    DBInstanceClass='db.t2.micro',
    AvailabilityZone='us-west-2a',
    PubliclyAccessible=False,
    Tags=[
        {
            'Key': 'Name',
            'Value': 'my-read-replica'
        }
    ]
)
read_replica_endpoint = response['DBInstance']['Endpoint']['Address']

read_replica_uri = f"postgresql://user:password@{read_replica_endpoint}:port/read_replica_db_name"
read_replica_engine = create_engine(read_replica_uri)

Session = sessionmaker(bind=read_replica_engine)
result = Session().execute('SELECT * FROM my_table')
