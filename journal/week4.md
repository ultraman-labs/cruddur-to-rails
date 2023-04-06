# Week 4 — Postgres and RDS

## Ultra Man (Tony)


# Progress/reference and "Ah-ha" notes to self.
| *********************** |
| --- |
| * [Field Notes](https://github.com/ultraman-labs/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week4/Notes-Week4.txt) |
| --- |
| ** Created the Cruddur DB instance |
| --- |
| * ![Cruddur DB Instance](../_docs/assets/week4/rdscruddur.png) |
| --- |
| ** Verifying the availbility zone for my region.|
| --- |
| * ![Availability Zone](../_docs/assets/week4/availabilityzone.png) |
| * ---|
| ** Creating user in AWS Cognito
| * ---|
| * ![Cognito User](../_docs/assets/week3/creatinguser.png) |
| * --- | 
<p> --- <br>  
    ** Wow! In the sign-in page of Cruddur, I was receiving an error of "User pool us-west-1_gOH8uljSz does not exist." <br>
       This threw me good! I initially thought to look in the docker-compose.yml file for code line that referenced <br>
       the "REACT_APP_AWS_USER_POOLS_ID" environment variable-- which contained the prior "User pool ID" that AWS <br>
       Cognito generated. After updating this variable, I went back and restarted the docker-compose.ym file. But <br>
       the sign-in error persisted. Hmmm...what the strange tacos was going on!? Okay, somehow I made the cerbral <br>
       leap of thinking that perhaps the REACT_APP_CLIENT_ID env var had change as well--- well it did! So I grabbed <br>
       (copied) the new Client ID that Cognito generated, and updated the pertinent variable in docker-compose.yml <br>
       Restarted the docker file and voila! After going back to the Cruddur sign-in page I was able to log in! </p>
    
   ![Another Sigin Error](../_docs/assets/week3/signinerror.png)  <br><br><br><br><br><br>
   ---
  >> ** Confirming that, after authenticating, the preferred user name atribute from Cognito was passed onto the Cruddur app.<br><br> 
       ![Preferred User](../_docs/assets/week3/preferredusername.png)
   
<br><br><br><br><br><br>
---


 >> ** Received email confirmaition code. <br><br><br><br>
 ![Confirm Email](../_docs/assets/week3/verifycode2.png) 
 
 <br><br><br><br><br><br>
 ---   
 
 >> ** Cruddur prompting to enter confirmation code sent to my email. <br><br><br><br>
 ![Confirm Email](../_docs/assets/week3/confcode.png) 
 
 <br><br><br><br><br><br>
 ---
>> ** In Cognito, verifying the status of of the user account as enabled and user email as confirmed. <br><br><br><br>
      ![Confirming](../_docs/assets/week3/confirmuser.png) 

<br><br><br><br><br><br>
 ---
>> ** Testing Cruddur's password recovery page. It Worked! <br><br><br><br>
  ![Password Recovery](../_docs/assets/week3/pwrecovery.png)

<br><br><br><br><br><br>
 ---

>> ** Successfully resetting user password. <br><br><br><br>
  ![Password Recovery](../_docs/assets/week3/pwresetgood.png)

<br><br><br><br><br><br>
 ---   
