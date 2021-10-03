#include <iostream>
#include "instance.h"
#include "display.h"

extern int enter_instance_display(int (*_entry)(display& _d, instance& _i), instance& _i);

int entry(display& _d, instance& _i)
{
  std::cout << "entry(display&, instance&)" << std::endl;
  return 0;
}

int entry(instance& _i)
{
  return enter_instance_display(entry, _i);
}

