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

    gem install rails
    gem update --system 3.5.5


 ## Creating the Rails Project
    At the CLI, run 

```bash 
$ rails new Cruddur
```

## Start the Rails server with:
```bash
$ rails server
```
---
### NOTE: Model-View-Controller (MVC) pattern: 
 Rails uses the MVC pattern to structure your application. This separates the data (model), the presentation (view), and the logic (controller) of your application, making it easier to maintain and understand.
---

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

## 4) Create a route for user

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