# Week 2 — Distributed Tracing

## Ultra Man (Tony)


# Progress/reference and "Ah-ha" notes to self
| *********************** |
| --- |
| * [Field Notes](https://github.com/ultraman-labs/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week2/Notes-Week2-2.txt) |
| --- |
| * After much troubleshooting, successfully produce a backend trace sent from cruddur|
| --- |
| * ![HoneyComb Trace](../_docs/assets/week2/honeycombtrace1.png) |
| --- |
| * Received HoneyComb email confirmation of trace from the backend-flask dataset|
| --- |
| * ![HoneyComb Confirmation](../_docs/assets/week2/datasetconfirmation2.png) |
| * ---|
| * Verifying Cruddur sampling rule
| * ![XRAY Sampling](../_docs/assets/week2/xraysamplingrule1.png) |
| * --- |
| * Xray daemon port 200 was available but not being served, i.e, not open. The issue was that the environmental AWS region varialble, in docker-compose.yml file, was        referencing this variable as "AWS_REGION", instead of "AWS_DEFAULT_REGION'. A small code fix victory for me! |
| * --- |
| * Segment from Cruddur |
| * ![XRAY Sampling](../_docs/assets/week2/segmentstimeline.png) |
| * --- |
| * Impement CloudWatch Logs |
| * ![CLoud Watch Logs](../_docs/assets/week2/logstreams.png) |
| * --- |
| *Confirming RollBar Access Token in GitPod |
| * ![RollBar Acess Token](../_docs/assets/week2/rollbaraccesstoken.png) |
| * ---|
| * Rollbar backend endpoint working |
| * ![RollBar Acess Token](../_docs/assets/week2/holarollbar.png) |
| * --- |
| * Rollbar capturing janked error |
| * ![RollBar Acess Token](../_docs/assets/week2/rollbarjankederror.png) |
| * --- |
| --- |





