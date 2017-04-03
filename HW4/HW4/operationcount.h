#ifndef OPERATIONCOUNT_H
#define OPERATIONCOUNT_H

using namespace std;

class OperationCount{
public:
  int addFunction = 0;
  int removeFunction = 0;

  void operator+=(const OperationCount& inOps){
    addFunction += inOps.addFunction;
    removeFunction += inOps.removeFunction;
  }
};

#endif
