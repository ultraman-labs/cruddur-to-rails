# Create a user
user = User.find_or_create_by!(name: 'Ultra-Man', email: 'tony@ultra-labs.com') do |u|
    u.password_digest = 'password' # Replace with a valid password digest
    # Add other necessary user attributes here
  end
  
  # Create posts associated with the created user
  user.posts.find_or_create_by!(name: 'Que pasa vato!', description: 'Somos hermanos!')
  # Add more posts as needed, ensuring to associate them with the user
  