# Ruby On Rails Refresher And Overview

**Ruby**

Ruby is a high-level, interpreted programming language. It's known for its simplicity and productivity, with an elegant syntax that's natural to read and easy to write. Created by Yukihiro Matsumoto in the mid-1990s, Ruby has become popular for its use in web development, among other applications.

**Ruby on Rails (or simply Rails)**

Ruby on Rails, often just called Rails, is a server-side web application framework written in Ruby. It's a model-view-controller (MVC) framework that provides default structures for a database, a web service, and web pages. Rails emphasizes the use of well-known software engineering patterns and paradigms, such as convention over configuration (CoC), don't repeat yourself (DRY), and the active record pattern.
Rails is particularly noted for its ease of use and speed of development. It allows developers to get a working web application up and running with minimal configuration and coding, making it a popular choice for web application development.
Rails is not a programming language itself; it's a framework that uses Ruby as its underlying language. It extends Ruby's capabilities, enabling developers to build complex web applications more efficiently.

**Gems**

Gems in the context of Ruby are essentially libraries or packages that extend the functionality of Ruby applications. Each gem contains a packaged Ruby application or library.
RubyGems, the package manager for Ruby, provides a standard format for distributing Ruby programs and libraries and a tool for managing the installation of gems.
Rails itself is distributed as a gem. When you install Rails using gem install rails, you're actually downloading and installing the Rails gem and its dependencies.
Developers can use gems to add new features to their Ruby applications without having to write these features from scratch. There's a gem for almost everything – from handling user authentication to managing file uploads, processing payments, and much more.

---
**Amalgamation in the Ruby Ecosystem**

The Ruby ecosystem, particularly for web development, often involves using Rails as the web framework and a variety of gems to add specific functionalities. This combination enables developers to build powerful, feature-rich web applications with relatively little boilerplate code.
The cohesive integration of Ruby, Rails, and gems makes development smoother and more efficient, adhering to Rails' philosophy of making developers happy and productive.

**In summary** 

While Ruby is the programming language, Rails is a web framework built using Ruby, and gems are modular libraries that can be used in Ruby (and Rails) applications to extend their capabilities. This integration forms a robust platform for web development.

---

### Setting up .gitpod.yml so that the Gitpod environment is ready to run Rails for each new workspace instantiantion.
The .gitpod.yml file, includes:

```yml
- name: rails
    init: |
       # Source RVM scripts
       source /home/gitpod/.rvm/scripts/rvm
   
       # Install and use a specific Ruby version
       rvm install "ruby-3.2.2"
       rvm use "ruby-3.2.2" --default
     
       # Update RubyGems
       gem update --system
   
       # Install Rails
       gem install rails  
   
       # Append Gem bin directory to PATH (for the current session)
       export PATH="$(ruby -e 'puts Gem.user_dir')/bin:$PATH"

       # Change to the root directory of the Rails application
       cd Cruddur

       # Install all gems specified in Gemfile
       bundle install

      # Cache the installation of gems to speed up future workspace startups
      # Optional: Specify the path to cache
```

 ## Creating the Rails Project
    At the CLI, run 

```bash 
$ rails new Cruddur
```

## Start the Rails server with:
```bash
$ bundle exec rails server
```
*Ensures that only the gems and versions listed in the Gemfile.lock are used to run the server. If there are version conflicts or if you have multiple versions of Rails installed, bundle exec will correctly use the version tied to the current app's bundle.

*It is a safer way to ensure consistent behavior across different environments (like development, testing, and production) and among different developers on the same project.
---

# Fatures to implement in Cruddur web app:

## 0) Create a new Rails project called Cruddur

Creating a new Rails project called "Cruddur" involves a few straightforward steps. Before you begin, ensure that you have Ruby and Rails installed on your system. Here’s a step-by-step guide:

1. Install Ruby
Rails requires Ruby, so first ensure you have Ruby installed. You can check your Ruby version by running:

```bash
ruby -v
```
If you need to install or upgrade Ruby, you can use a version manager like rbenv or rvm. This helps in managing multiple Ruby versions on the same system.

2. Install Rails
Once Ruby is set up, you can install Rails. To install the latest version of Rails, run:

```bash
gem install rails
```

After installation, you can verify it by checking the Rails version:

```bash
rails -v
```

3. Create the Rails Project
Now you are ready to create your new Rails project "Cruddur". In your terminal, run:

```bash
rails new Cruddur
```
This command will create a new directory named Cruddur with all the necessary Rails files and directories.

## 1) Configure the Project to connect to a Postgres database

## 2) Create a users controller

1. Open Your Terminal
Make sure you're in the root directory of your Rails application. This is where your Gemfile, app, config, and other key directories are located.

2. Generate the Users Controller
Run the following command in your terminal to generate a users controller:

```bash
rails generate controller Users
```
This command will create several files and directories:

*A controller file (app/controllers/ 
 users_controller.rb) where you will define actions like show, new, 
 edit, etc.

*A view directory (app/views/users/) where you can create view templates for each action in the controller.

*A helper file (app/helpers/users_helper.rb) for any helper methods you might need for your views.

*A CoffeeScript file (app/assets/javascripts/users.coffee) for JavaScript specific to this controller's views (if you're using CoffeeScript).

*A SCSS file (app/assets/stylesheets/users.scss) for styles specific to this controller's views.

3. Define Actions in the Controller
Open the generated users_controller.rb file in your text editor. Here, you can define the actions that your controller will handle. For example:

```ruby
class UsersController < ApplicationController
  def show
    # action code here
  end

  def new
    # action code here
  end

  def edit
    # action code here
  end

  # more actions as needed
end
```

## 3) Create a posts controller

**Step 1:** Open Terminal and Navigate to Your Rails Application
Ensure you're in the root directory of your Rails application. This is where you'll find folders like app, config, and Gemfile.

**Step 2:** Generate the Posts Controller
Use the Rails generator command to create your new controller. In your terminal, run:

```bash
rails generate controller Posts
```
This command does several things:

Creates a controller file named posts_controller.rb in app/controllers. This is where you'll define actions like index, show, new, edit, etc.
Creates a corresponding view directory app/views/posts. Here you'll add view templates for each of your controller actions.
Generates a helper file in app/helpers/posts_helper.rb. This module can be used to store helper methods for your views.
Adds a new file in app/assets/javascripts for JavaScript specific to the posts controller (if using the Asset Pipeline).
Adds a new stylesheet in app/assets/stylesheets for CSS specific to the posts controller (if using the Asset Pipeline).

**Step 3:** Define Actions in the Controller
Open the generated posts_controller.rb file in your text editor or IDE. It will be located under app/controllers. Here you can define the actions (methods) your controller will handle. For instance:

```ruby
class PostsController < ApplicationController
  def index
    # Code for listing all posts
  end

  def show
    # Code for showing a single post
  end

  def new
    # Code for showing a new post form
  end

  def create
    # Code for creating a new post
  end

  # Add more actions as needed
end
```

## 4) Create a route for user


Creating a route for a User resource in a Rails application involves defining the route in the application's routing file. Here's how to do it:

1) Open the routing file located at **config/routes.rb** in your text editor or IDE.

2) Inside this file, you can define a route for the User resource. There are different ways to do this depending on what you need. Here are a few common examples:

*To create a standard RESTful route for a User resource (which includes routes for **index**, **new**, **create**, **show**, **edit**, **update**, and **destroy actions**), add:

```ruby
resources :users
```

3) After modifying the routes.rb file, save your changes.

4) To view the list of routes that you have just created, you can run the following command in your terminal:

```ruby
rails routes
```

This will display a list of all routes in your application, including the ones you've just added for the User resource. Look for routes prefixed with users to verify that they have been added correctly.

Remember, the resources method is a powerful tool in Rails that automates the creation of a set of routes associated with a given resource. It is part of Rails' convention over configuration philosophy, providing a standard RESTful route structure.

## 5) Create a route for post

To define a route for a post in a Ruby on Rails application, you need to specify the type of HTTP request and the corresponding controller action in your routes.rb file. Assuming you have a PostsController with a create action to handle the creation of new posts, you can define the route as follows:

Step-by-Step Guide
Open the routes.rb File: This file is located in the config directory of your Rails application.

Add the POST Route: You'll add a line that defines the route for creating posts. This will map a POST request to a specific action in the controller. Here’s how you do it:

```ruby
Rails.application.routes.draw do
  # existing routes

  # Route for creating a new post
  post 'posts' => 'posts#create'

  # other routes
end
```
### In this line, post is the HTTP method, 'posts' is the path (as in yourdomain.com/posts), and 'posts#create' specifies the create action in the PostsController.


## 6) Create a model for user

---
## Docker Commands with PSQL

To connect to the 'cruddur' database in PostgreSQL, you can use the \c command followed by the name of the database. Here's how you do it:

*1.* First, ensure you are in the PostgreSQL command line interface. You can access it using the Docker command:

```bash
docker exec -it cruddur-to-rails-db-1 psql -U postgres
```

*2.* To list all databases, you should use the command below. This command displays the databases along with their owners, encoding, collation, ctype, and access privileges. This is how you can get an overview of all the databases present in your PostgreSQL instance.

```sql
\l or \list
```


*3.* Once in the PostgreSQL CLI, connect to the 'cruddur' database by executing:

```sql
\c cruddur
```
Now that you're connected to the 'cruddur' database in PostgreSQL, here are some common commands you can use to explore and interact with the database:

```sql
\dt                            List Tables
\d table_name                  Describe a table
SELECT * FROM table_name;      Query data
\du                            List Users and Their Roles
\s                             View Query History
SELECT current_database();     Show Current Database

CREATE TABLE new_table_name (             Create a New Table
    column1_name column1_datatype,
    column2_name column2_datatype,
    ...
);


INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);           Insert Data: To insert data into a table:


UPDATE table_name SET column = value WHERE condition;                                  Update Data: To update existing data:


DELETE FROM table_name WHERE condition;                                                Delete Data: To delete data from a table:

```


---

# Knowledge NOTES:

## Model-View-Controller (MVC) pattern: 
Rails uses the MVC pattern to structure your application. This separates the data (model), the presentation (view), and the logic (controller) of your application, making it easier to maintain and understand.

 ## Breakdown Of The routes.rb File 
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
This is especially useful when working on multiple projects that may require different Ruby versions, as you can switch between installed versions using commands like *$ rvm use ruby-2.7.2* to set your active Ruby version to 2.7.2 for the current terminal session.