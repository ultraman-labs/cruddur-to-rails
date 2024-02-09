class Post < ApplicationRecord
  validates :name, presence: true
  validates :description, presence: true

  # Association with user
  belongs_to :user
end
