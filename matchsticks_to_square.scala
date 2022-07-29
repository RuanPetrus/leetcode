object Solution{
    def makesquare(matchsticks: Array[Int]): Boolean = {
      val sorted_matchsticks = matchsticks.sortWith(_>_).reverse.toIndexedSeq.toList
      val side_size = matchsticks.sum / 4

      def check_possible(sticks: List[Int], size: Int, side_size: Int, n: Int = 0): Boolean = {
        if (size == 0 && sticks.length == 0) true 
        else if (sticks.length == 0 || n == sticks.length) false
        else if (size == 0) check_possible(sticks, side_size, side_size, 0)
        else if (sticks.apply(n) <= size) {
          check_possible(sticks.take(n) ::: sticks.drop(n + 1), size - sticks.apply(n), side_size, n)
        } else {
          check_possible(sticks, size, side_size, n + 1)
        }
      }

      if (side_size < sorted_matchsticks.head) false
      else check_possible( sorted_matchsticks, side_size, side_size )
    }

    // println(makesquare(Array(5, 4, 4, 4)))
}

// menor_lado_possível = maior numero array
// Soma / 4 tem que ser = menor_lado_possível
