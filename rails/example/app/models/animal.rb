class Animal < ApplicationRecord
  after_create -> { puts 'Animal created' }

  validates :name, presence: true
  before_validation :ensure_name_has_a_value

  private

  def ensure_name_has_a_value
    self.name = 'Unkwown' if name.blank?
  end
end
