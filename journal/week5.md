# Week 5 — DynamoDB and Serverless Caching

## Ultra Man (Tony)


# Progress/reference and "Ah-ha" notes to self.
| *********************** |
| --- |
| * [Field Notes](https://github.com/ultraman-labs/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week5/Notes-Week5.txt) |
| --- |
| ** Backend directory cleanup. |
| --- |
| * ![Directory CLeanup](../_docs/assets/week5/directorycleanup.png) |
| --- |
| ** Updating seed file user handles.|
| --- |
| * ![Updating User Handles](../_docs/assets/week5/updatinguserhandles.png) |
| * ---|
| ** Creating DB and loading schema.
| * ---|
| * ![Creating DB and loading schema](../_docs/assets/week5/cratingdbschema.png) |
| * --- | 
<p> --- <br>  
    **Seeding messages  </p>
    
   ![Seeding messages](../_docs/assets/week5/creatingmessagebunch.png)  <br><br><br><br><br><br>
   ---
  >> ** Running data scan.<br><br> 
       ![Running data scan](../_docs/assets/week5/performscan.png)
   
<br><br><br><br><br><br>
---


 >> ** Retrieving conversations. <br><br><br><br>
 ![Retrieving Conversations](../_docs/assets/week5/getconversations.png) 
 
 <br><br><br><br><br><br>
 ---   
 
 >> ** Time format error. <br><br><br><br>
 ![Time format error](../_docs/assets/week5/whatthehecktimeerror.png) 
 
 <br><br><br><br><br><br>
 ---
>> ** Resolving the time format error. <br><br><br><br>
      ![Time Format Error](../_docs/assets/week5/thetimefix.png) 

<br><br><br><br><br><br>
 ---
>> ** Listing users. <br><br><br><br>
  ![Listing users](../_docs/assets/week5/awsclilistusers.png)

<br><br><br><br><br><br>
 ---

>> ** Exporting environmental variables. <br><br><br><br>
  ![Exporting environmental variables](../_docs/assets/week5/exportingenvvar.png)

<br><br><br><br><br><br>
 --- 
 
 >> ** Changing file permissions. <br><br><br><br>
  ![Changing file permissions](../_docs/assets/week5/listusersfile.png)

<br><br><br><br><br><br>
 --- 

>> ** Updating Cognito users ids and generating its output. <br><br><br><br>
  ![Updating Cognito users](../_docs/assets/week5/verifyinguserdata.png)

<br><br><br><br><br><br>
 --- 
 
 >> ** Error that "setCognitoErrors" is undefined. <br><br><br><br>
  ![setCognitoErrors](../_docs/assets/week5/troublewithconfirmaitonpage.png)

<br><br><br><br><br><br>
 --- 
 
 >> ** Resolved setCognitoErrors, with code change shown in pic. <br><br><br><br>
  ![setCognitoErrors Fixed](../_docs/assets/week5/troublewithmessagegroupspage.png)

<br><br><br><br><br><br>
 ---

 >> ** The cause of this error was the referencing to a bash script. <br><br><br><br>
  ![Wrong reference](../_docs/assets/week5/bashtopythonerror.png)

<br><br><br><br><br><br>
 ---

 >> ** Resolved this error by moving the file to the correct directory . <br><br><br><br>
  ![Moved file](../_docs/assets/week5/nosuchfile.png)

<br><br><br><br><br><br>
 ---

---

 >> ** Andrew explained this error, and the temp fix is to re-login. <br><br><br><br>
  ![Expired token](../_docs/assets/week5/expiredtoken.png)

<br><br><br><br><br><br>
 ---
 
 ---

 >> ** Hmmm...the endpoint_url can not be found. The outputted suggestion is that this is a syntax error. <br><br><br><br>
  ![Syntax error](../_docs/assets/week5/findingsyntaxerror.png)

<br><br><br><br><br><br>
 ---
 
 >> ** Some times looking for the simple things can be the answer. In this case, it was an extra blank space. <br><br><br><br>
  ![Extra space](../_docs/assets/week5/extraspacenowfixed.png)

<br><br><br><br><br><br>
 ---
 
 >> ** Debugging this Unhandled thrown error when loading Londo new message. <br><br><br><br>
  ![No Londo message](../_docs/assets/week5/lostlondo.png)

<br><br><br><br><br><br>
 ---
 
 >> ** The solution was adding the path and element to the App.js. <br><br><br><br>
  ![Adding Path and Element](../_docs/assets/week5/codetrace.png)

<br><br><br><br><br><br>
 ---
 
 >> ** Creating the VPC endpoint <br><br><br><br>
  ![VPC endpoint](../_docs/assets/week5/cruddurendpoint.png)

<br><br><br><br><br><br>
 ---
 
 >> ** Created the AWS Dynamo DB table. <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week5/dynamodbcruddurtable.png)

<br><br><br><br><br><br>
 ---
 
 >> ** Creating the prod table onto AWS by runningthe  schema-load file with the prod flag. <br><br><br><br>
  ![Prod table](../_docs/assets/week5/gitpodclicruddurtable.png)
 
<br><br><br><br><br><br>
 ---
 
  >> ** Enabling the Dynamo DB stream for the cruddur-messages table. <br><br><br><br>
  ![Enabling stream](../_docs/assets/week5/dynamostreamon.png)
 
<br><br><br><br><br><br>
 ---
 
  >> ** Verifying that the stream trigger was created. <br><br><br><br>
  ![Stream trigger](../_docs/assets/week5/triggerstream.png)
 
<br><br><br><br><br><br>
 ---
 
  >> ** ClickOps for creating the inline policy for the lambda function. <br><br><br><br>
  ![inline policy](../_docs/assets/week5/creatininlinepolicyi.png)
 
<br><br><br><br><br><br>
 ---
 
  >> ** Verifying the creation of the inline policy. <br><br><br><br>
  ![Verifying inline policy](../_docs/assets/week5/lambdapolicy.png)
 
<br><br><br><br><br><br>
 ---
 
  >> ** Londo user is now working. <br><br><br><br>
  ![Got londo](../_docs/assets/week5/gotlondo.png)
 
<br><br><br><br><br><br>
 ---
 
  >> ** Generating AWS Dynamo prod messages . <br><br><br><br>
  ![Prod messages](../_docs/assets/week5/prodcrudmessage.png)
 
<br><br><br><br><br><br>
 ---
 
  >> ** Now using Cruddur app to test Londo messages on prod. <br><br><br><br>
  ![Testing Londo on prod](../_docs/assets/week5/londotacocheck.png)
 
<br><br><br><br><br><br>
 ---
 
  >> ** CloudWatch logs for Cruddur messages appear to be good. <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week5/logevents.png)
 
<br><br><br><br><br><br>
 ---
 
 
 
 
 
