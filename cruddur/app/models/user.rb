class User < ApplicationRecord
  # Devise modules
  devise :database_authenticatable, :registerable, :recoverable, :rememberable, :validatable

  # Validation
  validates :name, presence: true

  # Association with posts
  has_many :posts
end
