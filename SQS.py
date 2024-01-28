import boto3
import json
import time

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/612359070197/homework6sqs'

# run forever
while True:
    # Receive message from SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )

    # because message queue might be empty, we will TRY to fetch the next message
    try:
        # try to take the next message off the queue
        # note that the response is a dict, not a string
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']

        # Create a json object to read the resulting json from the response
        body = message['Body']
        bodyJson = json.loads(body)

        # Checks if message is bad within the json object
        if 'bad' in bodyJson['Message']:
            print(bodyJson['Message'] + ' - Error, leaving it in queue')
        # If it is not bad, we assume it is good
        else:
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=receipt_handle
            )
            # Delete message from queue - we won't get this far if the queue was empty
            # print out the body of the message
            print(bodyJson['Message'] + ' - Possibly good, removing from queue')

    except KeyError:
        print('no messages on the queue')
        message = []
        # if no messages, take a nap for a minute before trying again
        time.sleep(60)
