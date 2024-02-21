# Creating Testing Web Page After Successful Login 

To create a new testing page that users navigate to after successful login, you'll need to set up a new route, controller action, and view. Let's create a simple "dashboard" page as an example:

## 1) Create a New Controller:

You can create a new controller (e.g., DashboardsController) using the Rails generator command:

```bash
rails generate controller Dashboards show
```

This command will create a new controller with a show action and the corresponding view.

## 2) Define a Route:

In **config/routes.rb**, define a route to the new action:

```ruby
Rails.application.routes.draw do
  # Other routes...
  
  get 'dashboard', to: 'dashboards#show'
end
```

## 3) Create the View:

In app/views/dashboards, edit the show.html.erb file to include some basic content:

```erb
<h1>Cruddur</h1>
<p>Welcome To Your Cruddur Dashboard!</p>
```

## 4) Redirect After Login:

To redirect users to this page after a successful login, override the after_sign_in_path_for method in your ApplicationController:

```ruby
class ApplicationController < ActionController::Base
  protected

  def after_sign_in_path_for(resource)
    dashboard_path
  end
end
```