class User < ApplicationRecord
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
  