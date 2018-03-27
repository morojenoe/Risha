namespace risha{
namespace data_structures{

template<class T>
class SegmentTree {
public:
  template<class InputIt>
  SegmentTree(InputIt first, InputIt last) {
    auto interval_length = std::distance(first, last);
    this->n = 1;
    while (n < interval_length)
      this->n *= 2;
    
    tree.resize(2*n);
    
    for (size_t i = 0; first != last; ++i, ++first) {
      tree[n + i] = T(*first);
    }
    for (size_t i = n - 1; i > 0; --i) {
      tree[i] = tree[i*2] + tree[i*2 + 1];
    }
  }

  T get(size_t left, size_t right) {
    return get(1, left + 1, right + 1, 1, n);
  }

  template<class T2>
  void modify(size_t id, const T2 &value) {
    modify(1, id + 1, 1, n, value);
  }
  
  vector<T> tree;
  size_t n;

private:
  T get(size_t v, size_t i, size_t j, size_t l, size_t r) {
    if (i > r || l > j) {
      return T();
    }
    if (l <= i && j <= r) {
      return tree[v];
    }
    auto mid = (l + r) / 2;
    return get(v*2, i, j, l, mid) + get(v*2 + 1, i, j, mid + 1, r);
  }

  template<class T2>
  void modify(size_t v, size_t id, size_t l, size_t r, const T2 &value) {
    if (l == r) {
      
      return;
    }
    auto mid = (l + r) / 2;
    if (id <= mid) {
      modify(v*2, id, l, mid, value);
    } else {
      modify(v*2 + 1, id, mid + 1, r, value);
    }
    tree[v] = tree[v*2] + tree[v*2 + 1];
  }
};

}
}
