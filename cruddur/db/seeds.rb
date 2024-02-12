# Create a user
user = User.find_or_create_by!(email: 'tony@ultra-labs.com') do |u|
  u.name = 'Ultra-Man'
  u.password = 'password' # Set a valid password
  u.password_confirmation = 'password' # Confirm the password
end

# Create posts associated with the created user
user.posts.find_or_create_by!(name: 'Que pasa vato!', description: 'Somos hermanos!')
