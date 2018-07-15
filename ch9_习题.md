1, 对于闵可夫斯基距离 $(\sum_{u=1}^n|x_{iu}-x_{ju}|^p)^{\frac1p}$，显然满足非负性，同一性和对称性。
设 $x_i$,，$x_j$，$x_k$：
$dist_{mk}(x_i, x_j)=(\sum_{u=1}^n|x_{iu}-x_{ju}|^p)^{\frac1p}$

$dist_{mk}(x_i, x_k)=(\sum_{u=1}^n|x_{iu}-x_{ku}|^p)^{\frac1p}$

$dist_{mk}(x_j, x_k)=(\sum_{u=1}^n|x_{ju}-x_{ku}|^p)^{\frac1p}$

$p\geq1$时，$(\sum|x_iu-x_ku|^p)^{\frac1p}+(\sum|x_ju-x_ku|^p)^{\frac1p} \geq (\sum|x_iu-x_ju|^p)^{\frac1p}$，直递性成立；

$p\leq1$时，$(\sum|x_iu-x_ku|^p)^{\frac1p}+(\sum|x_ju-x_ku|^p)^{\frac1p} \leq (\sum|x_iu-x_ju|^p)^{\frac1p}$，直递性不成立；

当$p\to\infty$, $\sum_{u=1}^n(\frac{|x_iu-x_ju|}{\max_u|x_iu-x_ju|})^p=1$
$\lim_{p\to\infty}(\sum_{u=1}^n|x_iu-x_ju|^p)^{\frac1p}=(\max_u|x_iu-x_ju|)\lim_{p\to\infty}(\sum_{u=1}^n(\frac{|x_iu-x_ju|}{\max_u|x_iu-x_ju|})^p)^{\frac1p}=\max_u|x_iu-x_ju|$;

3, k-means得到的是局部最优解，不是全局最优解。

5， 连接性：假设xi为核心对象，由于xj可以由xi密度可达。则存在核心对象xk，使得xi与xk密度直达，xk与xj密度直达。由于xk是核心对象，则xk与xi密度直达。且密度直达是密度可达的子集，所以xk与xj密度可达，xk与xi密度可达，所以xi与xj密度相连。

6， 对于所有分类都有一个可以包含所有类内样本的最小圆。最小距离是扩大半径直到遇到第一个其他类的点时合并这两个类；最大距离是扩大半径直到包含另一个其他类的全部样本时合并这两个类

7， k-means，DBSCAN，AGNES是凸聚类;高斯混合聚类能产生非凸聚类

9， 对于混合属性中的连续属性，可以用闵可夫斯基距离作为度量；对于非连续属性可以使用海明距离进行度量。
