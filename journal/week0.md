# Setting up .gitpod.yml so that the Gitpod environment is ready to run Rails for each new workspace instantiantion.
The .gitpod.yml file, so far, contains:

    gem install rails
    gem update --system 3.5.5


 ## Creating the Rails Project
    At the CLI, ran 

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

# FEATURES TO IMPLEMENT:

## 0) Configure the Project to connect to a Postgres database

## 1) Create a users controller

## 2) Create a posts controller

## 3) Create a route for user

## 4) Create a route for post

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


## 5) Create a model for user