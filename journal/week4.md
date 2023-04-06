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

>> ** Editing security group inbound rule for GitPod. <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week4/beforesginboundrule.png)

<br><br><br><br><br><br>
 ---
 
 >> ** Testing the connection to the production database. <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week4/successprodconnect.png)

<br><br><br><br><br><br>
 ---

 >> ** Testing the connection to the production database. <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week4/successprodconnect.png)

<br><br><br><br><br><br>
 ---

 >> ** Testing the connection to the production database. <br><br><br><br>
  ![DB Connect Script](../_docs/assets/week4/successprodconnect.png)

<br><br><br><br><br><br>
 ---


