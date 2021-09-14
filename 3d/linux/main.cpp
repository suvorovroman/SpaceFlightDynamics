#include "../instance.h"

class local_instance:public instance
{
};

int main(int _argc, const char** _argv)
{
  local_instance i;
  return entry(i);
}
