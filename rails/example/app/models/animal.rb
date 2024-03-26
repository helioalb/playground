class Animal < ApplicationRecord
  after_create -> { puts 'Animal created' }
end
