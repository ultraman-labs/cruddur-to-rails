
## Section 1: Initial settings for Gitpod and Rails

#### Setting up .gitpod.yml so that the Gitpod environment is ready to run Rails for each new workspace instantiantion.
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