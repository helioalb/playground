class HashAsParameterExample
  def initialize(a:, b:, c:)
    @a = a
    @b = b
    @c = c
  end

  def show
    puts "#{@a} #{@b} #{@c}"
  end
end

example = HashAsParameterExample.new(a: 1, b: 2, c: 3)
example.show

# The example below doesn't works
# hash = { a: 1, b: 2, c: 3 }
# example = HashAsParameterExample.new(hash)
# example.show

