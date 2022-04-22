class Article < ApplicationRecord

  # ==== INPUT VALIDATION ====
  # Make sure the title is present
  validates :title, presence: true
  # Make sure the body is present and has a minimum length of 10
  validates :body, presence: true, length: { minimum: 10}

end
