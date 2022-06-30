from mypkg.mymath import fact,fizzbuzz,fib
from mypkg.greet import hello

# __all__変数で、パッケージを作成下側がfrom パッケージ名 import * で
# 何を読み込ませたいか
__all__ = ["fact", "fizzbuzz", "fib","hello"]
