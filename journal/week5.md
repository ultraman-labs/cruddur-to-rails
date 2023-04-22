# Week 5 — DynamoDB and Serverless Caching

## Ultra Man (Tony)


# Progress/reference and "Ah-ha" notes to self.
| *********************** |
| --- |
| * [Field Notes](https://github.com/ultraman-labs/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week5/Notes-Week5.txt) |
| --- |
| ** Directory Cleanup |
| --- |
| * ![Directory CLeanup](../_docs/assets/week5/directorycleanup.png) |
| --- |
| ** Verifying the availbility zone for my region.|
| --- |
| * ![Availability Zone](../_docs/assets/week4/availabilityzone.png) |
| * ---|
| ** Listing the database before creating the Cruddur DB.
| * ---|
| * ![List DBs](../_docs/assets/week4/dblist.png) |
| * --- | 
<p> --- <br>  
    **Connect to postgres first, then create database buddy!  </p>
    
   ![Cruddur DB Listed](../_docs/assets/week4/postgrescreatedb1.png)  <br><br><br><br><br><br>
   ---
  >> ** Moving towards automizing postgres password<br><br> 
       ![Auto PW](../_docs/assets/week4/autopwpostgres.png)
   
<br><br><br><br><br><br>
---


 >> ** Exporting the connection url to GitPod environment. <br><br><br><br>
 ![Connection URL](../_docs/assets/week4/autopsqllogin.png) 
 
 <br><br><br><br><br><br>
 ---   
 
 >> ** Testing the bash db-drop script. <br><br><br><br>
 ![Drop DB](../_docs/assets/week4/dropdb.png) 
 
 <br><br><br><br><br><br>
 ---
>> ** Testing the bash db-create script. <br><br><br><br>
      ![Creating Cruddur DB](../_docs/assets/week4/createdb.png) 

<br><br><br><br><br><br>
 ---
>> ** Testing the bash db-schema-load script. <br><br><br><br>
  ![Schema Loading](../_docs/assets/week4/dbschemaload.png)

<br><br><br><br><br><br>
 ---

>> ** Testing the bash db-connect script. <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week4/dbconnect.png)

<br><br><br><br><br><br>
 --- 
 
 >> ** Using the command \dt to list the users and activities tables. <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week4/listingtables.png)

<br><br><br><br><br><br>
 --- 

>> ** Seeding the data into the tables. <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week4/dbseeddata.png)

<br><br><br><br><br><br>
 --- 
 
 >> ** False negative-- Cruddur DB instance did spin up successfully. <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week4/awsrdslied.png)

<br><br><br><br><br><br>
 --- 
 
 >> ** Editing security group inbound rule for GitPod. <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week4/beforesginboundrule.png)

<br><br><br><br><br><br>
 ---

 >> ** Testing the connection to the production database. <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week4/successprodconnect2.png)

<br><br><br><br><br><br>
 ---

 >> ** Listing production database. <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week4/listofproddbs.png)

<br><br><br><br><br><br>
 ---

---

 >> ** Setting GitPod's environmental variables for DB security group identification. <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week4/returntrue1.png)

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
 
 
 
 
 
 
