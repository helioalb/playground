#include <iostream>

int main() {
  int integer = 12;
  double decimal = 12.99;
  char letter = 'A';
  std::string phrase = "String is inside of namespace std";
  bool isValid = true;

  if (isValid) {
    std::cout <<
      "int: " << integer << "\n" <<
      "double: " << decimal << "\n" <<
      "char: " << letter << "\n" <<
      "std::string: " << phrase << "\n";
  }

  return 0;
}
