# Week 1 — App Containerization

## Ultra Man (Tony)


# Progress and "Ah-ha" notes to self
| *********************** |
| --- |
| * Writing two docker files |
| * Success with Docker files running |
| * Success with Docker files working together |
| * After an intial hiccup, was able to get Docker files working together with Docker Compose |
| * In GitPod Dev, identified and understood inside outside container processes of Dockerfile |
| * Containerized Backend -- Got JSON from https://4567-ultramanlab-awsbootcamp-fn2r29njef5.ws-us87.gitpod.io/api/activities/home |
| * Successfully built Frontend and Backend Docker containers |
| * Remembered to make port 4567 public by unlocking padlock icon |
| ![Port Screenshot](../_docs/assets/week1/UnlockPort.png) |
| ---------------------------------------------------------------------------------------------------------------------------------- |
| * Fascinating how Docker Composer runs multiple containers simultaneously |
| * Ran into a CORS error, resolved by restarting workspace |
| * Cruddur Screenshot of SignUp |
| ![Crudder SignUp Screenshot](../_docs/assets/week1/CruddarSignUp.png) |
| * Discovered how to toggle the mini-map in GitPod |
| * Endpoint for notifications tab. Resolved issue of "user_notification.py" module not found. Extra blank space after extension was the issue. |
| --- |
## * NameError ... trying to figure out how to trace "UserNotifications" not defined error.  
| ![NameError Screenshot](../_docs/assets/week1/NameError.png) |
## * Resolved. Within "user_notifications.py" file, the "class"  was not defined with the correct name of "UserNotifications"
| ![Class Name Screenshot](../_docs/assets/week1/ClassName1.png) |
## Success. Rendered JSON structured data with intended string changes
| ![JSON Data Screenshot](../_docs/assets/week1/JsonData1.png) |
| --- |
## Created the FrontEnd user notifications tab
| ![FrontEndNotification Screenshot](../_docs/assets/week1/NotificationsTab.png) |
| --- |
## Established db connection
| ![FrontEndNotification Screenshot](../_docs/assets/week1/dbconnect.png) |
| --- |
## Had to circle back and recreate the credentials for the IAM user and confirm subscripiton. My error was using the access keys of a different user. All good now.
| ![FrontEndNotification Screenshot](../_docs/assets/week1/subscriptionConfirmed2.png) |
| --- |
## Retrieved records (two music artist)
| ![FrontEndNotification Screenshot](../_docs/assets/week1/tableitems.png) |
| --- |





