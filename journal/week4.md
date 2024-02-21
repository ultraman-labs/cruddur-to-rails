## Stuff I discovered deving with Rails

- [The routes.rb file](#here's-why)
- [What is ERB?](#what-is-erb)
- [What is the command **$ rvm list** for?](#what-is-the-command--rvm-list-for)
- [Rails common commands](#rails-common-commands)
- [Configuring the *development.rb* file](#configuring-the-developmentrb-file)
- [Steps for deleting a specific](#steps-for-deleting-a-specific-user-and-their-associated-data-in-this-case-posts-from-the-database-via-the-rails-console)
- [Create a Homepage](#create-a-homepage)



### Model-View-Controller (MVC) pattern: 
Rails uses the MVC pattern to structure your application. This separates the data (model), the presentation (view), and the logic (controller) of your application, making it easier to maintain and understand.

 ### Breakdown Of The routes.rb File 
 The file extension for `routes.rb` is **.rb**, which stands for **Ruby**. It's a plain text file that contains code written in the Ruby programming language.

**Here's why it's a .rb file:**

1. **Purpose:** The `routes.rb` file is specifically used in **Ruby on Rails** web applications to define the application's routes. These routes determine how incoming web requests are mapped to specific controller actions, essentially controlling how users navigate through different pages and features of the application.

2. **Ruby code:** The content of `routes.rb` is written in Ruby syntax, using keywords, methods, and structures that are part of the Ruby language. This code is responsible for setting up the routing rules and defining how URLs are matched to controller actions.

3. **Convention:** In Rails, files ending with the .rb extension are conventionally used for source code files written in Ruby. This helps maintain consistency and organization within a Rails project.

**Key points:**

- It's a core part of the Rails framework.
- It's essential for defining the application's navigation structure.
- It's written in Ruby, hence the .rb extension.
- It's typically located in the `config` directory of a Rails application.

## What is ERB?
In Ruby on Rails, "ERB" stands for "Embedded Ruby". ERB is a templating system that enables Ruby code to be embedded within a text document. This is particularly useful in web applications where you might want to use Ruby to dynamically generate HTML content. In an ERB template, Ruby code is enclosed in special tags that the ERB processor recognizes and executes when the template is rendered.


## What is the command *$ rvm list* for?

In Ruby on Rails, the command $ rvm list is used when working with RVM (Ruby Version Manager). It's not specific to Rails itself but is commonly used in Rails development environments to manage different Ruby versions.

Here's what the command does:

**List Installed Ruby Versions:* $ rvm list displays a list of all Ruby versions that are currently installed via RVM on your machine. This includes the default Ruby version set by RVM and any other versions you may have installed for different projects or testing purposes.

**Indicate Current and Default Rubies:* The command also typically indicates which Ruby version is currently being used in the shell session (=>) and which is set as the default for new sessions (=*).

The output of *$ rvm list* might look something like this:
```shell
rvm rubies

=* ruby-2.7.2 [ x86_64 ]
   ruby-3.0.0 [ x86_64 ]
   ruby-3.2.2 [ x86_64 ]

# => - current
# =* - current && default
#  * - default
```
This is especially useful when working on multiple projects that may require different Ruby versions, as you can switch between installed versions using commands like *$ rvm use ruby-2.7.2* to set your active Ruby version to 2.7.2 for the current terminal session.](week3.md)

---

## Rails common commands
**rails new <appname>:** Creates a new Rails application with the given name. You can also pass additional options to customize the setup.

**rails server or rails s:** Starts the Rails server, making your application accessible via a web browser. You can specify the environment and port.

**rails console or rails c:** Opens the Rails console, an interactive environment for running Ruby and Rails commands against your application.

**rails db:create:** Creates the database defined in your database configuration file (database.yml).

**rails db:drop:** Drops (deletes) the database.

**rails db:migrate:** Runs the migrations to update your database schema to the latest version.

**rails db:rollback:** Rolls back the last database migration.

**rails db:seed:** Runs the db/seeds.rb file to seed the database with default or test data.

**rails generate or rails g:** Used to generate various components like models, controllers, views, and more. For example, rails generate model User name:string email:string.

**Open the Rails console** 

```bash
rails console
Rails.cache.clear
exit
```

**rails destroy:** The opposite of generate, used to undo generated code. For instance, rails destroy model User would remove the files generated by rails generate model User.

**rails routes:** Lists all your application's routes, showing the URL, HTTP verb, and the corresponding controller action.

**rails test:** Runs all your application's tests.

**rails db:setup:** Creates the database, loads the schema, and initializes it with the seed data (if any).

**rails assets:precompile:** Precompiles static assets.

**rails about:** Provides information about your application’s environment, like versions of Ruby and Rails, database, middleware, and so on.

**rails db:schema:**load: Loads the schema into the database. This is useful when setting up an existing application for the first time.

**rails credentials:edit:** Opens an editor to manage your application's credentials securely.


These commands cover a wide range of tasks you'll typically perform while developing a Rails application, from setup and configuration to development and testing.

---

### Steps for deleting a specific user and their associated data (in this case, posts) from the database via the *Rails console:*

### 1. Finding the User:

- Use the *find_by* method to locate the user you want to delete based on a unique attribute, such as an email address.
- Example: *user_to_delete = User.find_by(email: 'example@example.com')*

### 2. Deleting Associated Posts:

- Before deleting the user, ensure that all associated data that depends on the user is also deleted. This is important to maintain  
  referential integrity and to avoid foreign key constraint violations.
  
- Example: *user_to_delete.posts.destroy_all if user_to_delete*
  
### 3.  Deleting the User:

- Once the associated data is deleted, you can safely delete the user.

- Example: *user_to_delete.destroy if user_to_delete*

### 4. Verification:

- After performing the deletion, you can verify that the user has been successfully removed by querying the database again.

- Example: Use *User.find_by(email: 'example@example.com') to check if the user still exists (it should return nil).*

## *NOTE:*
    Remember, these commands should be executed carefully, especially in a production environment, as they will permanently remove data from your database. Always ensure that you have appropriate backups and understand the implications of these operations. 

---

 ## Configuring the *development.rb* file:
  Currently the Gitpod host is *config.hosts << "3000-ultramanlab-cruddurtora-la0p81ysawe.ws-us108.gitpod.io*. In the *development.rb* file, under the */cruddur/config/environments/* directory, Rails has this line of code as a static configuration. However each time a new Gitpod workspace environment is started, the host id will change. Consequently, we need to change this line of code so that it dynamically loads the Gitpod host id.

  So how do we find out what the host random genereated id is? More so, how do we code this line into the *development.rb* file? Well, we have to use the CLI and sift Gitpod's environment (similar if uisng Github's Code-Space). If you look at the URL of your Gitpod workspace, you'll see the generated host id. Now since the Rails server is using port 3000 and
  
  One way is to enter the bash command:

  ```bash
  env | grep la0p
  ```

  config.hosts << "3000-#{ENV['HOSTNAME']}.ws-us108.gitpod.io"

---

# Frontend
  ### Create a Homepage

 **1)** To create a homepage you need to generate a new controller. You can call this PagesController with an index action as it's a common convention for html pages.

  ```bash
  rails generate controller Pages index
  ``` 
  This will generate a new controller with a view for the index action, typically at **app/views/pages/index.html.erb**

**2)** Set the Homepage as the Root Route:

In your config/routes.rb, set the root path to the index action of your PagesController:
```ruby
root 'pages#index'
```

**3)** Add Navigation to the Login Page:

On your new homepage (app/views/pages/index.html.erb), add a link to the login page:

``erb
<%= link_to 'Login', new_user_session_path %>
``
The ****new_user_session_path** is a path helper provided by Devise for the login page. Make sure you have the right path name. You can check the available paths by running rails routes in your terminal.

**4)** Update the Login Page:

- Move the form and related content from app/views/posts/index.html.erb to a new view provided by Devise for sessions, typically app/views/devise/sessions/new.html.erb.
- If you've customized the Devise views, ensure you place the form code in the appropriate Devise view for signing in.
- If you haven't already customized Devise views, you can do so by running:

```bash
rails generate devise:views
```
- After running this command, you'll find all the Devise views in app/views/devise. Locate the sessions/new.html.erb file and update it with your form code.

**5)** Style and Structure Your Homepage:

- The homepage should welcome users and provide information about your application. Here's a simple example

```html
<!-- app/views/pages/index.html.erb -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="description" content="Welcome to Cruddur" />
  <title>Welcome to Cruddur</title>
  <%= stylesheet_link_tag 'application', media: 'all', 'data-turbolinks-track': 'reload' %>
</head>
<body>
  <noscript>You need to enable JavaScript to run this app.</noscript>
  <main class="container">
    <h1>Welcome to Cruddur!</h1>
    <p>The disposable micro-blogging platform. Say it... then forget it...</p>
    <%= link_to 'Login', new_user_session_path, class: 'btn btn-primary' %>
    <!-- Add more content and styling as needed -->
  </main>
</body>
</html>
```

- Customize this page with your desired content, styling, and additional links as needed.

---



[def]: #rvm-list
[def2]: #what-is-the-command--rvm-list-for