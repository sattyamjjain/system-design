import boto3

cloudfront = boto3.client("cloudfront")


def create_distribution():
    response = cloudfront.create_distribution(
        DistributionConfig={
            "CallerReference": "example.com",
            "Aliases": {"Quantity": 1, "Items": ["example.com"]},
            "Origins": {
                "Quantity": 1,
                "Items": [
                    {
                        "Id": "example_origin",
                        "DomainName": "example.com.s3.amazonaws.com",
                        "S3OriginConfig": {"OriginAccessIdentity": ""},
                    }
                ],
            },
            "DefaultCacheBehavior": {
                "TargetOriginId": "example_origin",
                "ForwardedValues": {
                    "QueryString": False,
                    "Cookies": {"Forward": "none"},
                },
                "ViewerProtocolPolicy": "allow-all",
                "MinTTL": 0,
            },
            "Enabled": True,
            "Comment": "Example CloudFront Distribution",
        }
    )
    return response["Distribution"]["DomainName"]
