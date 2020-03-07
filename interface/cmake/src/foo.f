
      subroutine add(x, y, n)
      double precision x(*), y(*)
      integer n
      integer i

      do i = 1, n
         y(i) = y(i) + x(i)
      end do
      return

      end
