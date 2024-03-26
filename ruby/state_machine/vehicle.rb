require 'state_machines'

class Vehicle
  state_machine initial: :parked do
    event :ignite do
      transition parked: :idling
    end

    states.each do |state|
      self.state(state.name, :value => state.name.to_sym)
    end
  end
end

v = Vehicle.new     # => #<Vehicle:0xb71da5f8 @state=:parked>
v.ignite!           # => true
v.state             #=> :idling
