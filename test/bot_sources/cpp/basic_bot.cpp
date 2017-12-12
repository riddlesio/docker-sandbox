#ifndef __BASIC_BOT__
#define __BASIC_BOT__

#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const vector<string> explode(const string& s, const char& c)
{
	string buff{""};
	vector<string> v;
	
	for(auto n:s)
	{
		if(n != c) buff+=n; else
		if(n == c && buff != "") { v.push_back(buff); buff = ""; }
	}
	if(buff != "") v.push_back(buff);
	
	return v;
}


int main() {
  char line[256];

  while (!cin.eof()) {   
    
    cin.getline(line, 256);
    vector<string> command{explode(line, ' ')};

    if (command.size() == 0 || command.at(0) != "action") {
      continue;
    }

    int choice = rand() % 3;
    if (choice == 0) {
      cout << "rock" << endl;
    }
    else if (choice == 1) {
      cout << "paper" << endl;
    }
    if (choice == 2) {
      cout << "scissors" << endl;
    }
  }
}

#endif
