import boto3

s3 = boto3.client('s3')

bucket_name = 'my-bucket'
s3.create_bucket(Bucket=bucket_name)

file_name = 'example.txt'
with open(file_name, 'rb') as f:
    s3.upload_fileobj(f, bucket_name, file_name)

with open('downloaded.txt', 'wb') as f:
    s3.download_fileobj(bucket_name, file_name, f)

response = s3.list_objects_v2(Bucket=bucket_name)
for item in response['Contents']:
    print(item['Key'])
