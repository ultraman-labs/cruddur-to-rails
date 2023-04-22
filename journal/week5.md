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
  ![Changing file permissions](../_docs/assets/week5/listusersfile.pngg)

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
  ![Expired token](../_docs/assets/week5/expired token.png)

<br><br><br><br><br><br>
 ---
 
 ---

 >> ** Adding description to security group rule. <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week4/descriptionwentthrough.png)

<br><br><br><br><br><br>
 ---
 
 >> ** Retrieving email confirmation code. <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week4/confirmationcode.png)

<br><br><br><br><br><br>
 ---
 
 >> ** Logging into Cruddur. <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week4/confirmemail.png)

<br><br><br><br><br><br>
 ---
 
 >> ** Logging into Cruddur. <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week4/confirmemail.png)

<br><br><br><br><br><br>
 ---
 
 >> ** Investigating CloudWatch logs for any errors. There were none! <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week4/lognoerrors2.png)

<br><br><br><br><br><br>
 ---
 
 >> ** Successfully retrieved new Cruddur users <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week4/verifieddbuserentry2.png)

<br><br><br><br><br><br>
 ---
 
 >> ** Bingo! The Crud posted as expected. <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week4/crudpostverified2.png)
 
<br><br><br><br><br><br>
 ---
 
 
 
 
 
 
