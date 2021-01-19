```python
import numpy as np
```


```python
#1.將下列清單(list1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")
```


```python
a=array1
```


```python
array1 = np.array(range(30))
```


```python
a.ravel(order='F')
a.reshape((5,6))
```




    array([[ 0,  1,  2,  3,  4,  5],
           [ 6,  7,  8,  9, 10, 11],
           [12, 13, 14, 15, 16, 17],
           [18, 19, 20, 21, 22, 23],
           [24, 25, 26, 27, 28, 29]])




```python
#2.呈上題的array，找出被6除餘1的數的索引
```


```python
np.where(a%6==1)
```




    (array([ 1,  7, 13, 19, 25], dtype=int64),)




```python

```
