#include <iostream>
#include "display.h"

namespace X11
{

  display::failed_to_open::failed_to_open(const std::string& _name):failure
		           (
			    "XOpenDisplay failed to open " + _name +  " display"
			   )
  {
  }						     

  display::display(const char* _name)
  {
    if((D = XOpenDisplay(_name)) == NULL)
      throw display::failed_to_open(_name == NULL ? "DISPLAY environment variable":_name);
    std::cout << "ServerVendor:\t" << ServerVendor(D) << std::endl;
    std::cout << "VendorRelease:\t" << VendorRelease(D) << std::endl;
  }

  display::~display()
  {
    XCloseDisplay(D);
  }

}


