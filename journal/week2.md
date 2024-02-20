## Features to implement in Cruddur web app:

#### 0) Create a new Rails project called Cruddur

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

#### 1) Configure the Project to connect to a Postgres database

#### 2) Create a users controller

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

#### 3) Create a posts controller

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

#### 4) Create a route for user


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

#### 5) Create a route for post

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
#### In this line, post is the HTTP method, 'posts' is the path (as in yourdomain.com/posts), and 'posts#create' specifies the create action in the PostsController.


#### 6) Create a model for user


#### 7) Create a model for a post


#### 8 & 9) Create a migration for a user table and for post table 

To create the **user** and **post** tables respectively, use the following commands in the terminal:

```bash
rails generate migration CreateUsers
```

```bash
rails generate migration CreatePosts
```

To verify that these tables have been created run the command:

```bash
$ rails db:migrate:status

database: cruddur

 Status   Migration ID    Migration Name
--------------------------------------------------
   up     20240206031844  Create users
   up     20240206031938  Create posts
```
The output shows that both migrations have a status of "up," which indicates theythese migration tables have been run successfully and are applied to the database.


#### 10) Apply validation to the user table

Validations are applied at the model level. To add validations to a User model, what needs to be done is to write validation rules in the User model file **(app/models/user.rb)**. Here are the current validations:

```ruby
class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable
    validates :name, presence: true
    validates :email, presence: true, uniqueness: true, format: { with: URI::MailTo::EMAIL_REGEXP }
    validates :password_digest, presence: true
  
    # Association with posts
    has_many :posts

     # Custom validation
  validate :check_additional_requirements

  private

  def check_additional_requirements
    # Custom validation logic here
  end

  end
```


#### 11) Apply validation to the post table

To apply validations to the Post table in the Cruddur Rails application, you would be working with the model file associated with the Post table, typically named **post.rb** within the **app/models** directory.

**Run a Rails Generator**
If the Post model hasn't been created yet, you can generate it using a Rails generator. This will create the model file along with other associated files like migration files.

```bash
rails generate model Post name:string description:text
```

This command creates the Post model with name and description fields. 


**Edit the Post Model:** Open the post.rb file and define your validations. Rails provides a variety of validation helpers to check for conditions such as presence, uniqueness, format, and length.

```ruby
class Post < ApplicationRecord
  validates :name, presence: true
  validates :description, presence: true

  # Association with user
  belongs_to :user
end
```

#### 12) Define table relationships between the user and post table


-- **1. Set Up Model Associations**

You need to edit the model files to define the relationship between *'User'* and *'Post'*.

**User Model (app/models/user.rb):**

Add **has_many :posts** to indicate that each user can have many posts.

```ruby
class User < ApplicationRecord
  has_many :posts
  # other code...
end
```
**Post Model (app/models/post.rb):**

Add belongs_to :user to indicate that each post belongs to a user.

```Ruby
class Post < ApplicationRecord
  belongs_to :user
  # other code...
end
```
---
---

To verify the defined table relationships between the User and Post tables in a Rails application, you can look at the model files.

**User Model (app/models/user.rb):**
ook for a line like **has_many :posts**. This indicates that a single User can be associated with multiple Post records.

**Post Model (app/models/post.rb):**

Look for a line like **belongs_to :user**. This indicates that each Post record is associated with a single User.
---

#### 13) 


#### 15) Implementing a comprehensive email validation in the Cruddur Rails application

Using an authentication **gem** like **Devise** provides a robust solution. Devise includes its own email validation, along with many other features for user authentication.


To use Devise, add it to your **cruddur/gemfile**. Preferably at the top of the Gemfile:

```ruby
# Implementing user authentication and authorization feature
gem 'devise'
```

**Install the Gem:** After saving the Gemfile, go back to the terminal, ensure you're in the Crudur project's root directory (where the Gemfile is located), and run the following command to install Devise and any other pending gems:

```bash
bundle install
```

Then, run bundle install to install the gem. After that, you can install Devise in the Cruddur app and generate the user model with Devise:

```bash
rails generate devise:install
rails generate devise User
```

This will create a new User model with Devise's default configurations, which include email validation. Then, if needed, the Cruddur can be customized with Devise's settings to suit the needs of the Cruudr app.

**Migrate the Database:** If the Devise generator created any new migration files (like for adding new columns to your User model), run the following command:

```bash
rails db:migrate
```

This process will integrate Devise into your Rails Cruddur application. Ensure that your terminal session is in the correct directory, and that you have correctly edited and saved the Gemfile.