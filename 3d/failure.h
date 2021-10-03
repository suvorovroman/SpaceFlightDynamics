#include <stdexcept>

class failure:public std::runtime_error
{
public:

  failure(const std::string& _what):std::runtime_error(_what){}
  
};
