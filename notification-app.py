import requests  # pip install requests
import json
import sys


def send_message_to_slack(event, context):
    webhook_url = "https://hooks.slack.com/services/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"
    # Build Message
    try:
        message = {
            "alarmName": event['alarmData']['alarmName'],
            "state": event['alarmData']['state']  # json.dumps(event['alarmData']['state'])
        }

        payload = {
            "text": json.dumps(message)
        }
        print(type(payload))
        # Send Message to Slack
        response = requests.post(
            webhook_url,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"}
        )
        # sys.exit(1)  # Something happened here and your application going to crash. Nothing after this line of code going
        # to work
        print("Slack response", response)

    except Exception as problem:
        print(f"An error occurred: {problem}")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


# event_object = {
#     'source': 'aws.cloudwatch',
#     'alarmArn': 'arn:aws:cloudwatch:us-east-1:444455556666:alarm:lambda-demo-metric-alarm',
#     'accountId': '444455556666',
#     'time': '2023-08-04T12:36:15.490+0000',
#     'region': 'us-east-1',
#     'alarmData': {
#         'alarmName': 'lambda-demo-metric-alarm',
#         'state': {
#             'value': 'ALARM',
#             'reason': 'test',
#             'timestamp': '2023-08-04T12:36:15.490+0000'
#         },
#         'previousState': {
#             'value': 'INSUFFICIENT_DATA',
#             'reason': 'Insufficient Data: 5 datapoints were unknown.',
#             'reasonData': '{"version":"1.0","queryDate":"2023-08-04T12:31:29.591+0000","statistic":"Average","period":60,"recentDatapoints":[],"threshold":5.0,"evaluatedDatapoints":[{"timestamp":"2023-08-04T12:30:00.000+0000"},{"timestamp":"2023-08-04T12:29:00.000+0000"},{"timestamp":"2023-08-04T12:28:00.000+0000"},{"timestamp":"2023-08-04T12:27:00.000+0000"},{"timestamp":"2023-08-04T12:26:00.000+0000"}]}',
#             'timestamp': '2023-08-04T12:31:29.595+0000'
#         },
#         'configuration': {
#             'description': 'Metric Alarm to test Lambda actions',
#             'metrics': [
#                 {
#                     'id': '1234e046-06f0-a3da-9534-EXAMPLEe4c',
#                     'metricStat': {
#                         'metric': {
#                             'namespace': 'AWS/Logs',
#                             'name': 'CallCount',
#                             'dimensions': {
#                                 'InstanceId': 'i-12345678'
#                             }
#                         },
#                         'period': 60,
#                         'stat': 'Average',
#                         'unit': 'Percent'
#                     },
#                     'returnData': True
#                 }
#             ]
#         }
#     }
# }
#
#send_message_to_slack(event=event_object)