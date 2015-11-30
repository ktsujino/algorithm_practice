#include <algorithm>
#include <vector>
#include <iostream>

template <class Iter>
int partition(Iter data, int l, int h) {
  int p = h;
  int fh = l; // fh=fist high
  for(int i = l; i < h; i++) {
    if(data[i] <= data[p]) {
      std::swap(data[i], data[fh]);
      fh++;
    }
  }
  std::swap(data[fh], data[p]);
  return fh;
}

template <class Iter, class T>
bool quickSelect(Iter data, int l, int h, int k, T &item) {
  if(h < l) return false;
  int p = partition(data, l, h);
  if(p == k) {
    item = data[p];
    return true;
  }
  if(p < k) {
    return quickSelect(data, p+1, h, k, item);
  }else {
    return quickSelect(data, l, p-1, k, item);
  }
}

int main() {
  std::vector<int> v;
  for(int i = 0; i < 100; i+=2) {
    v.push_back(i);
  }
  int out;
  if(quickSelect(v, 0, v.size(), 2, out)) {
    std::cout << out << std::endl;
  }else {
    std::cout << "Fail" << std::endl;
  }
}

