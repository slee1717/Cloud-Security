import boto3

# Create an SNS client
client = boto3.client("sns")

topic_arn = "arn:aws:sns:us-east-1:612359070197:homework6"

# Publish a simple message to the specified SNS topic

# Sends three good messages to the SNS
for i in range(0, 3):
    response = client.publish(
        TopicArn=topic_arn,
        Message="good",
        MessageAttributes={
            'attr': {
                'DataType': 'String',
                'StringValue': 'good'
            }
        },
    )
    # Print out the response
    print(response)

# Sends two bad messages to the SNS
for i in range(0, 2):
    response = client.publish(
        TopicArn=topic_arn,
        Message="bad",
        MessageAttributes={
            'attr': {
                'DataType': 'String',
                'StringValue': 'bad'
            }
        },
    )
    # Print out the response
    print(response)
