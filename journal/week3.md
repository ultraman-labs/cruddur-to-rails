# Week 3 — Decentralized Authentication

## Ultra Man (Tony)


# Progress/reference and "Ah-ha" notes to self
| *********************** |
| --- |
| * [Field Notes](https://github.com/ultraman-labs/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week3/Notes-Week3.txt) |
| --- |
| * Using Chrome's DevTools to troubleshoot un-authenticated user |
| --- |
| * ![Sigin Error](../_docs/assets/week3/goodsignuperror.png) |
| --- |
| * Received the expected signin error, now time to setup Cognito user and user pool.|
| --- |
| * ![Happy Error](../_docs/assets/week3/happyerror.png) |
| * ---|
| * Creating user in AWS Cognito
| * ![Cognito User](../_docs/assets/week3/creatinguser.png) |
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




